import pandas as pd

def top_locations(df):
    return df['location'].value_counts().head(10)


def top_roles(df):
    return df['title'].value_counts().head(10)


def top_companies(df):
    return df['company'].value_counts().head(10)


def remote_jobs(df):
    # Check if 'Remote' appears in location
    remote_count = df['location'].str.contains("remote", case=False, na=False).sum()
    non_remote = len(df) - remote_count

    return pd.Series({
        "Remote": remote_count,
        "Non-Remote": non_remote
    })


def salary_availability(df):
    available = df['salary'].apply(lambda x: x not in ["", "Not Specified", None]).sum()
    not_available = len(df) - available

    return pd.Series({
        "Salary Provided": available,
        "Not Provided": not_available
    })