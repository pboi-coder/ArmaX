Project

Forensic Criminal Records Data Processor

Think of it as an internal police analyst tool, not a criminal investigation tool. Its purpose is to organize, clean, and summarize records, similar to the record management systems used by many police departments.

Repository Structure
forensic-criminal-records/

│
├── data/
│   └── criminal_records.csv
│
├── src/
│   ├── cleaning.py
│   ├── statistics.py
│   ├── search.py
│   └── reports.py
│
├── notebook/
│   └── exploration.ipynb
│
├── README.md
└── requirements.txt
Example Dataset Columns
Case_ID
Suspect_ID
First_Name
Last_Name
Age
Gender
City
Crime_Type
Crime_Severity
Evidence_Count
Officer_Assigned
Case_Status
Date_Opened
Date_Closed
Fingerprint_Match
DNA_Match

Use fictional/synthetic records rather than real personal data.

Things your program should do
#Load the CSV
#Find duplicate case IDs
#Detect missing information
#Count cases by crime type
#Count open vs closed cases
#Find oldest active cases
#Find officers with the most assigned cases
#Average suspect age
Highest evidence count
Search by suspect name
Search by case ID
Sort by severity
Sort by evidence count
Generate a short text report

Pandas Concepts You'll Practice
read_csv()
DataFrames
Series
Boolean indexing
loc
iloc
sort_values()
value_counts()
describe()
isna()
duplicated()
unique()
NumPy statistics
Git Commit Ideas
Initial project structure

Created synthetic criminal database

Implemented CSV loading

Added duplicate detection

Added missing data report

Implemented crime statistics

Added officer workload analysis

Refactored project into modules

Completed README