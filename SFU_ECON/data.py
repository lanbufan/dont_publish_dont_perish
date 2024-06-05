import pandas as pd

# Data as a dictionary for the Economics Department at Simon Fraser University
data_sfu = {
    "Name": [
        "Victor Aguiar", "Douglas Allen", "Bertille Antoine", "Fernando Aragon Sanchez",
        "Chris Bidner", "Serena Canaan", "David Cox", "Eliav Danziger", "Minjie Deng",
        "Sepideh Fotovatian", "David Freeman", "Jane Friesen", "Michael Gilraine", "Lucas Herrenbrueck",
        "Alexander Karaivanov", "Kenneth Kasa", "Anke Kessler", "Dongwoo Kim", "John Knowles",
        "Brian Krauth", "Shih En Lu", "Christoph Luelfesmann", "Steeve Mongrain", "Pierre Mouganie",
        "Gordon Myers", "Krishna Pendakur", "Luba Petersen", "Marie Rekkas", "Arthur Robson",
        "Martin Santamaria", "Nicolas Schmitt", "Kevin Schnepel", "Xiaoting Sun", "Simon Woodcock"
    ],
    "Rank": [
        "Associate Professor", "Professor", "Professor, Graduate Chair", "Professor, Undergraduate Chair",
        "Associate Professor", "Assistant Professor", "University Lecturer", "Assistant Professor", "Assistant Professor",
        "Lecturer", "Associate Professor", "Professor", "Assistant Professor", "Associate Professor",
        "Professor", "Professor", "Professor, Department Chair", "Assistant Professor", "Professor",
        "Associate Professor", "Associate Professor", "Professor", "Professor", "Assistant Professor",
        "Professor", "Professor, Associate Chair", "Associate Professor", "Associate Professor", "Professor",
        "Senior Lecturer", "Professor", "Associate Professor", "Assistant Professor", "Associate Professor"
    ],
    "PhD School": [
        "Brown University", "University of Washington", "Université de Montréal", "London School of Economics",
        "University of British Columbia", "University of California, Santa Barbara", "Queen's University", "Princeton University",
        "University of Rochester", "Monash University", "University of British Columbia", "University of Toronto",
        "University of Toronto", "University of California, Davis", "University of Chicago", "University of Chicago",
        "University of Bonn", "University College London", "University of Rochester", "University of Wisconsin",
        "Harvard University", "University of Bonn", "Queen's University", "Texas A&M University, College Station (TAMU)",
        "McMaster University", "University of California, Berkeley", "University of California, Santa Cruz", "University of Toronto",
        "Massachusetts Institute of Technology", "University of Chicago", "University of Toronto", "University of California, Santa Barbara",
        "University of California, Los Angeles", "Cornell University"
    ],
    "Office Ext": [
        "N/A", "(778) 782-3445", "N/A", "N/A", "N/A", "(778) 782-5376", "N/A", "N/A", "N/A",
        "N/A", "N/A", "N/A", "N/A", "(778) 782-4805", "N/A", "N/A", "(778) 782-3443", "(778) 782-7092", "N/A",
        "N/A", "N/A", "(778) 782-8504", "N/A", "(778) 782-5378", "N/A", "N/A", "N/A", "N/A", "N/A",
        "(778) 782-9395", "N/A", "N/A", "N/A", "(778) 782-4524"
    ],
    "Email": [
        "vaguiarl@sfu.ca", "allen@sfu.ca", "baa7@sfu.ca", "faragons@sfu.ca",
        "cbidner@sfu.ca", "scanaan@sfu.ca", "dcox@sfu.ca", "edanzige@sfu.ca", "minjied@sfu.ca",
        "sfotovat@sfu.ca", "dfa19@sfu.ca", "friesen@sfu.ca", "gilraine@sfu.ca", "herrenbrueck@sfu.ca",
        "akaraiva@sfu.ca", "kkasa@sfu.ca", "akessler@sfu.ca", "dongwook@sfu.ca", "jaknowle@sfu.ca",
        "bkrauth@sfu.ca", "shihenl@sfu.ca", "cluelfes@sfu.ca", "mongrain@sfu.ca", "pmougani@sfu.ca",
        "gmmyers@sfu.ca", "pendakur@sfu.ca", "lubap@sfu.ca", "mrekkas@sfu.ca", "robson@sfu.ca",
        "msantama@sfu.ca", "schmitt@sfu.ca", "kschnepe@sfu.ca", "xsa46@sfu.ca", "swoodcoc@sfu.ca"
    ],
    "Office Location": [
        "WMC 4653", "WMC 2670", "WMC 3633", "WMC 3639",
        "WMC 3641", "WMC 2680", "WMC 2660", "WMC 3637", "WMC 2678",
        "WMC 3657", "(Not provided)", "WMC 1697", "WMC 3639", "WMC 4657",
        "WMC 3625", "WMC 2666", "WMC 4667", "WMC 2668", "WMC 2676",
        "WMC 3631", "WMC 4661", "WMC 2658", "WMC 2662", "WMC 2686",
        "WMC 4663", "WMC 4655", "WMC 3629", "WMC 3643", "WMC 4670",
        "WMC 2672", "WMC 4665", "WMC 2664", "WMC 3627", "WMC 4659"
    ]
}

# Create DataFrame
df_sfu = pd.DataFrame(data_sfu)

# Save to CSV
csv_file_path_sfu = "sfu_economics_faculty.csv"
df_sfu.to_csv(csv_file_path_sfu, index=False)

