import tkinter as tk
from tkinter import scrolledtext
import pandas as pd
df = pd.read_csv("criminal_records.csv")

#functions

def display(data):
    results.delete("1.0", tk.END)
    results.insert(tk.END, str(data))

def duplicate_cases():
    display(df[df.duplicated(subset="Case_ID", keep="first")])

def missing_values():
    display(df.isna())

def crime_types():
    display(df.groupby("Crime_Type")["Case_ID"].count())

def case_status():
    display(df.groupby("Case_Status")["Case_ID"].count())

def open_cases():
    display(df[df["Case_Status"] == "Open"].sort_values("Case_ID", ascending=False).head(10))

def officer_workload():
    display(df.groupby("Officer_Assigned")["Case_ID"].count())

def average_age():
    display(df.groupby("Age")["Suspect_ID"].count().mean())

def evidence():
    display(df.groupby("Suspect_ID")["Evidence_Count"].count().sort_values(ascending=False).head(5))

def search_name():
    name = name_entry.get()
    display(df[df["First_Name"].str.lower() == name.lower()])

def search_case():
    case = case_entry.get()
    display(df[df["Case_ID"].astype(str) == case])

#ui

root = tk.Tk()
root.title("Criminal Records Database")
root.geometry("1000x600")

#output
results = scrolledtext.ScrolledText(root, width=100, height=30)
results.grid(row=0, column=2, rowspan=20, padx=10, pady=10)

#search for name
tk.Label(root, text="First Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=0)
tk.Button(root, text="Search Name", command=search_name).grid(row=2, column=0)

#search for case
tk.Label(root, text="Case ID").grid(row=3, column=0)
case_entry = tk.Entry(root)
case_entry.grid(row=4, column=0)
tk.Button(root, text="Search Case", command=search_case).grid(row=5, column=0)

#analysis buttons
tk.Button(root, text="Duplicate Cases", width=20, command=duplicate_cases).grid(row=6, column=0)
tk.Button(root, text="Missing Values", width=20, command=missing_values).grid(row=7, column=0)
tk.Button(root, text="Crime Types", width=20, command=crime_types).grid(row=8, column=0)
tk.Button(root, text="Case Status", width=20, command=case_status).grid(row=9, column=0)
tk.Button(root, text="Top 10 Open Cases", width=20, command=open_cases).grid(row=10, column=0)
tk.Button(root, text="Officer Workload", width=20, command=officer_workload).grid(row=11, column=0)
tk.Button(root, text="Average Age", width=20, command=average_age).grid(row=12, column=0)
tk.Button(root, text="Most Evidence", width=20, command=evidence).grid(row=13, column=0)

root.mainloop()