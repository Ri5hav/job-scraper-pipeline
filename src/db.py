import sqlite3

def create_connection():
    conn = sqlite3.connect("data/jobs.db")
    return conn

def save_to_db(df):
    conn = create_connection()
    df.to_sql("jobs", conn, if_exists="replace", index=False)
    conn.close()

def get_top_locations():
    conn = create_connection()

    query = """
    SELECT location, COUNT(*) as count
    FROM jobs
    GROUP BY location
    ORDER BY count DESC
    LIMIT 10
    """

    result = conn.execute(query).fetchall()
    conn.close()

    return result