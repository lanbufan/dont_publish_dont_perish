
import pandas as pd
import spacy
import pycountry
import re

# Load the SpaCy model for Named Entity Recognition (NER)
nlp = spacy.load("en_core_web_sm")

# List of country names and common abbreviations
country_aliases = {
    "USA": "United States",
    "U.S.A.": "United States",
    "U.S.": "United States",
    "UK": "United Kingdom",
    "U.K.": "United Kingdom",
    "England": "United Kingdom",
    "South Korea": "Korea, Republic of",
    "North Korea": "Korea, Democratic People's Republic of",
    "Russia": "Russian Federation",
    "Viet Nam": "Vietnam",
    "Iran": "Iran, Islamic Republic of",
    "UAE": "United Arab Emirates"
}

# Extend pycountry data with common aliases
country_lookup = {country.name: country.name for country in pycountry.countries}
country_lookup.update(country_aliases)

# Function to extract country from a given location string
def extract_country(location):
    # Check for country in parentheses
    country_in_parentheses = re.search(r'\((.*?)\)', location)
    if country_in_parentheses:
        country_abbr = country_in_parentheses.group(1).strip().upper()
        if country_abbr in country_aliases:
            return country_aliases[country_abbr]

    # Use SpaCy to process the location
    doc = nlp(location)
    found_entities = [ent.text for ent in doc.ents if ent.label_ in {"GPE", "LOC"}]

    for entity in found_entities:
        entity_normalized = entity.strip().title()
        if entity_normalized in country_lookup:
            return country_lookup[entity_normalized]
        # Check if any part of the entity matches a known country
        for country in country_lookup:
            if country in entity_normalized:
                return country_lookup[country]

    # Additional fallback for abbreviations directly in the text
    for part in location.split():
        part_normalized = part.strip().upper()
        if part_normalized in country_aliases:
            return country_aliases[part_normalized]

    return "Unknown"

# Load the data
file_path = 'repec_rank_economics_institutions_2024.csv'
data = pd.read_csv(file_path, encoding='latin-1')

# Clean column names
data.columns = [col.strip() for col in data.columns]

# Apply the function to the location column
data['PhDCountry'] = data['location'].apply(extract_country)

# Save the updated dataframe to a new CSV file
output_file_path = 'repec_rank_economics_institutions_2024_with_countries.csv'
data.to_csv(output_file_path, index=False)

# Display the first few rows to verify the new column
print(data[['location', 'PhDCountry']].head())

