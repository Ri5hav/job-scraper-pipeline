import requests
import pandas as pd

def scrape_jobs():
    url = "https://remotive.com/api/remote-jobs"

    response = requests.get(url)
    data = response.json()

    jobs = []

    for job in data["jobs"]:
        jobs.append({
            "title": job["title"],
            "company": job["company_name"],
            "location": job["candidate_required_location"],
            "salary": job["salary"]
        })

    df = pd.DataFrame(jobs)

    return df