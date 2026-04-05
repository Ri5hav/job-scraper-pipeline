def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna("Not Specified")

    # Clean text fields
    df['title'] = df['title'].str.strip()
    df['company'] = df['company'].str.strip()
    df['location'] = df['location'].str.strip()

    return df