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

Uses fictional/synthetic records rather than real personal data.
