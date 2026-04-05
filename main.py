from src.scrape import scrape_jobs
from src.clean import clean_data
from src.db import save_to_db, get_top_locations

from src.transform import (
    top_locations,
    top_roles,
    top_companies,
    remote_jobs,
    salary_availability
)

from src.visualize import plot_bar, plot_pie

import pandas as pd


def main():
    print("🔄 Fetching data from API...")
    df = scrape_jobs()

    print("🧹 Cleaning data...")
    df = clean_data(df)

    print("💾 Saving to database...")
    save_to_db(df)

    print("📊 Running SQL query...")
    data = get_top_locations()

    df_sql = pd.DataFrame(data, columns=["location", "count"])
    df_sql.set_index("location", inplace=True)

    print("\nTop Locations (SQL):")
    print(df_sql)

    print("\n📊 Generating insights...")

    locations = top_locations(df)
    roles = top_roles(df)
    companies = top_companies(df)
    remote = remote_jobs(df)
    salary = salary_availability(df)

    print("\n📈 Visualizing data...")

    plot_bar(locations, "Top Job Locations")
    plot_bar(roles, "Top Job Roles")
    plot_bar(companies, "Top Hiring Companies")
    plot_pie(remote, "Remote vs Non-Remote Jobs")
    plot_pie(salary, "Salary Availability")

    print("\n✅ Pipeline completed!")


if __name__ == "__main__":
    main()