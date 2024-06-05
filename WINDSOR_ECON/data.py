import pandas as pd

# Data as a dictionary for the Economics Department at the University of Windsor
data_windsor = {
    "Name": [
        "Sang-Chul Suh", "Marcelo Aarestrup Arbex", "Steven Chen", "Tarek Jouini",
        "Dingding Li", "Jay Rhee", "Nurlan Turdaliev", "Christian Trudeau", "Yuntong Wang", "Yahong Zhang"
    ],
    "Rank": [
        "Professor, Department Head", "Professor", "Assistant Professor", "Associate Professor",
        "Associate Professor, Director, MA Programs", "Professor, Undergraduate Advisor",
        "Professor, Director, MAEP Program", "Professor", "Professor", "Assistant Professor"
    ],
    "Office Location": [
        "6105 Lambton Tower", "7113 Lambton Tower", "6116 Lambton Tower", "6113 Lambton Tower",
        "6112 Lambton Tower", "6117 Lambton Tower", "7109 Lambton Tower", "7112 Lambton Tower",
        "6109 Lambton Tower", "7111 Lambton Tower"
    ],
    "Office Ext": [
        "2368", "2389", "2389", "2381", "2383", "2385", "(Not provided)", "2374", "2382", "2406"
    ],
    "Email": [
        "scsuh@uwindsor.ca", "arbex@uwindsor.ca", "Ruoyu.Chen@uwindsor.ca", "tjouini@uwindsor.ca",
        "dli@uwindsor.ca", "jayrhee@uwindsor.ca", "nurlan@uwindsor.ca", "trudeauc@uwindsor.ca",
        "yuntong@uwindsor.ca", "yzhang@uwindsor.ca"
    ],
    "Research Areas": [
        "Social Choice Theory, Game Theory, Microeconomic Theory",
        "Macroeconomics, Fiscal and Monetary Economics, Informal Activities, Tax Evasion",
        "Environmental and Energy Economics, Urban Economics, Developmental Economics",
        "Econometrics, Finite Sample and Simulation-Based Inference, Macroeconomics, Monetary Economics",
        "Econometrics, Nonparametric Econometrics",
        "International Economics, Monetary Economics, Quantitative Methods",
        "Monetary Economics, Macroeconomics, Game Theory",
        "Microeconomics, Game Theory, Industrial Organization",
        "Microeconomic Theory, Game Theory, Cost Sharing",
        "Macroeconomics, Monetary Economics, Labour Economics"
    ]
}

# Create DataFrame
df_windsor = pd.DataFrame(data_windsor)

# Save to CSV
csv_file_path_windsor = "windsor_economics_faculty.csv"
df_windsor.to_csv(csv_file_path_windsor, index=False)
