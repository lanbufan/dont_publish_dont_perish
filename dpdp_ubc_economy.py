import pandas as pd

# Data for the CSV
data = {
    "Name": [
        "Amartya Lahiri", "Brian R Copeland", "Claudio Ferraz", "David Green", "Erik Snowberg",
        "Felipe Valencia Caicedo", "Florian Hoffmann", "Giovanni Gallipoli", "Gorkem Bostanci", "Heather Sarsons",
        "Henry Siu", "Hiro Kasahara", "Jamie McCasland", "Jesse Perla", "Katherine Wagner",
        "Kevin Milligan", "Kevin Song", "Li Hao", "Marit Rehavi", "Matt Lowe",
        "Mauricio Drelichman", "Michael Devereux", "Michael Peters", "Michal Szkup", "Munir Squires",
        "Nathan Nunn", "Nicole Fortin", "Patrick Baylis", "Patrick Francois", "Paul Beaudry",
        "Paul Schrimpf", "Philip Solimine", "Raffaele Saggio", "Reka Juhasz", "Sam Hwang",
        "Sam Norris", "Sergei Severinov", "Siwan Anderson", "Terry Moon", "Thomas Lemieux",
        "Torsten Jaccard", "Vadim Marmer", "Victor Couture", "Viktoriya Hnatkovska", "Vitor Farinha Luz",
        "Wei Li", "Clive Chapple", "Jonathan Graves", "Marina Adshade", "Angela Redish",
        "David Donaldson", "Donald Paterson", "Gordon R Munro", "Hugh M Neary", "John Helliwell",
        "Margaret Slade", "Mukesh Eswaran", "Nancy Gallini", "Paul Bradley", "Robert Evans",
        "Ronald A. Shearer", "Russell Uhler", "W Erwin Diewert", "W. Craig Riddell", "Ke Xu",
        "Kevin Leyton-Brown", "Anichul Khan", "Chowdhury Shameem Mahmoud", "Emrul Hasan", "Catherine Douglas",
        "Geoffrey Newman", "Michael Vaney", "Ratna Shrestha", "Robert Gateman"
    ],
    "Title": [
        "Professor", "Professor", "Professor", "Professor", "Canada Excellence Research Chair",
        "Assistant Professor", "Associate Professor", "Professor", "Assistant Professor", "Associate Professor",
        "Professor", "Professor", "Assistant Professor", "Associate Professor", "Assistant Professor",
        "Professor | Director, Vancouver School of Economics", "Professor", "Professor", "Associate Professor", "Assistant Professor",
        "Professor | Director of Undergraduate Studies (Faculty and Academic)", "Professor (on leave)", "Professor", "Associate Professor", "Assistant Professor",
        "Professor", "Professor", "Assistant Professor", "Professor (on leave)", "Professor",
        "Associate Professor", "Postdoctoral Fellow", "Assistant Professor", "Assistant Professor", "Assistant Professor",
        "Assistant Professor", "Associate Professor", "Professor", "Assistant Professor", "Professor",
        "Assistant Professor", "Professor | Graduate Program Director", "Associate Professor", "Associate Professor", "Associate Professor",
        "Associate Professor", "Associate Professor of Teaching", "Assistant Professor of Teaching | Director of Undergraduate Studies (Curriculum and Students)", "Assistant Professor of Teaching", "Professor Emeritus",
        "Professor Emeritus", "Professor Emeritus", "Professor Emeritus", "Professor Emeritus", "Professor Emeritus",
        "Professor Emeritus", "Professor Emeritus", "Professor Emeritus", "Professor Emeritus", "Professor Emeritus",
        "Professor Emeritus", "Professor Emeritus", "Professor Emeritus", "Professor Emeritus", "Visiting Professor",
        "Associate Member", "Lecturer", "Lecturer", "Lecturer", "Sessional Lecturer (Continuing)",
        "Sessional Lecturer (Continuing)", "Sessional Lecturer (Continuing)", "Sessional Lecturer (Continuing)", "Sessional Lecturer (Continuing)"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

df.to_csv('dpdp_ubc_economic.csv')
