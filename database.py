import pandas as pd

#load the CSV
df = pd.read_csv("criminal_records.csv")

#Search Functions

def search_name(name):
    return df[df["First_Name"].str.lower() == name.lower()]


def search_case(case):
    return df[df["Case_ID"].astype(str) == str(case)]


#Analysis function
def duplicate_cases():
    return df[df.duplicated(subset="Case_ID", keep="first")]


def missing_values():
    return df.isna().sum()


def crime_types():
    return (
        df.groupby("Crime_Type")["Case_ID"]
        .count()
        .reset_index(name="Total Cases")
    )


def case_status():
    return (
        df.groupby("Case_Status")["Case_ID"]
        .count()
        .reset_index(name="Total Cases")
    )


def open_cases():
    return (
        df[df["Case_Status"] == "Open"]
        .sort_values("Case_ID", ascending=False)
        .head(10)
    )


def officer_workload():
    return (
        df.groupby("Officer_Assigned")["Case_ID"]
        .count()
        .reset_index(name="Cases Assigned")
    )


def average_age():
    return df["Age"].mean()


def evidence():
    return (
        df.groupby("Suspect_ID")["Evidence_Count"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index(name="Evidence Count")
    )