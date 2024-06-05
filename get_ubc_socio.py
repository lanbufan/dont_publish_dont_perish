import pandas as pd

# Data as a dictionary
data = {
    "Name": [
        "Alyssa Alexander", "Amanda Cheong", "Amin Ghaziani", "Amy Hanser", "Andrew Jorgenson",
        "Anna Dawczyk", "Anne Martin-Matthews", "Aryan Karimi", "Carrie Yodanis", "Catherine Corrigall-Brown",
        "Chelsea Freeborn", "Clayton Childress", "David Tindall", "Elic Chan", "Elizabeth Hirsh",
        "Emily Huddart Kennedy", "Ethan Raker", "Gerry Veenstra", "Guy Stecklov", "Jennifer Berdahl",
        "Katherine Lyon", "Kathy Greaves", "Kerry Greer", "Kimberly Huyser", "Laura Nelson",
        "Lindsey Richardson", "Nathanael Lauster", "Neda Maghbouleh", "Neil Armitage", "Oral Robinson",
        "Phyllis Johnson", "Qiang Fu", "Renisa Mawani", "Rima Wilkes", "Sean Lauer",
        "Seth Abrutyn", "Silvia Bartolic", "Sylvia Fuller", "Tony Silva", "Yue Qian"
    ],
    "Rank": [
        "Lecturer", "Assistant Professor", "Professor", "Associate Professor", "Professor",
        "Lecturer", "Professor", "Assistant Professor", "Associate Professor", "Professor and Department Head",
        "Lecturer", "Associate Professor", "Professor", "Lecturer", "Professor",
        "Associate Professor and Associate Head", "Assistant Professor", "Professor", "Professor", "Professor",
        "Assistant Professor of Teaching", "Lecturer", "Associate Professor of Teaching", "Associate Professor", "Assistant Professor",
        "Associate Professor", "Associate Professor", "Associate Professor", "Lecturer", "Lecturer",
        "Associate Professor", "Associate Professor", "Professor", "Professor", "Professor",
        "Associate Professor", "Associate Professor of Teaching", "Professor", "Assistant Professor", "Associate Professor"
    ],
    "PhD School": [
        "North Carolina State University", "Princeton University", "Northwestern University", "University of California-Berkeley", "(Not provided)",
        "University of Guelph", "McMaster University", "University of Alberta", "University of New Hampshire", "University of California-Irvine",
        "University of Alberta", "(Not provided)", "University of Toronto", "University of Toronto", "University of Washington",
        "University of Alberta", "Harvard University", "McMaster University", "University of California-Berkeley", "University of Illinois Champaign-Urbana",
        "University of British Columbia", "Oregon State University", "Indiana University", "University of Texas, Austin", "University of California-Berkeley",
        "University of Oxford", "Brown University", "(Not provided)", "University of Manchester", "University of Saskatchewan",
        "Ohio State University", "Duke University", "University of Toronto", "University of Toronto", "(Not provided)",
        "University of California-Riverside", "University of Texas, Austin", "Rutgers University", "University of Oregon", "Ohio State University"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
csv_file_path = "ubc_sociology_faculty.csv"
df.to_csv(csv_file_path, index=False)
