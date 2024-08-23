import pandas as pd
import csv
from data_input import (
    get_company,
    get_position,
    get_location,
    get_date,
    get_status,
    get_description,
)

FILE_NAME = "job_data.csv"
COLUMNS = ["company", "position", "location", "applied_date", "status", "description"]


def init_csv():
    try:
        pd.read_csv(FILE_NAME)
    except FileNotFoundError:
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(FILE_NAME, index=False)


def add_job(company, position, location, applied_date, status, description):
    new_entry = {
        "company": company,
        "position": position,
        "location": location,
        "applied_date": applied_date,
        "status": status,
        "description": description,
    }

    with open(FILE_NAME, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=COLUMNS)
        writer.writerow(new_entry)
    print("Job added successfully.")


def update_job(company, position, location, applied_date, status, description):
    new_entry = [company, position, location, applied_date, status, description]

    with open(FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    for i, row in enumerate(rows):
        if any(company in cell for cell in row) and any(
            position in cell for cell in row
        ):
            rows[i] = new_entry

    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Job updated successfully.")


def get_job(company):
    df = pd.read_csv(FILE_NAME)

    mask = df["company"] == company.lower()
    filtered_df = df.loc[mask]

    if filtered_df.empty:
        print(f"No job found for company {company}.")
    else:
        print(filtered_df)


def job_exists(company, position):
    df = pd.read_csv(FILE_NAME)

    mask = (df["company"] == company.lower()) & (df["position"] == position.lower())
    filtered_df = df.loc[mask]

    if filtered_df.empty:
        return False
    else:
        return True


def get_jobs_by_status():
    status = get_status()
    df = pd.read_csv(FILE_NAME)

    mask = df["status"] == status.lower()
    filtered_df = df.loc[mask]

    if filtered_df.empty:
        print(f"No jobs found with status {status}.")
    else:
        print(filtered_df)


def add_entry():
    init_csv()
    company = get_company().lower()
    position = get_position().lower()
    date = get_date(
        "Enter the application date (dd-mm-yyyy) or press enter for today's date: ",
        allow_default=True,
    )

    location = get_location().lower()
    status = get_status().lower()
    description = get_description().lower()

    if job_exists(company, position):
        update_job(company, position, location, date, status, description)
    else:
        add_job(company, position, location, date, status, description)


def main():
    while True:
        print("\nJOB TRACKER")
        print("\n1. Add or update a job entry")
        print("2. View all jobs by status")
        print("3. View specific job")
        print("4. Exit")
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            get_jobs_by_status()
        elif choice == "3":
            name = input("Enter company name: ")
            get_job(name)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
