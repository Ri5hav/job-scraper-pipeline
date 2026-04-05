# Job Market Data Pipeline

This project is an end-to-end data pipeline that extracts job listings from a public API, processes the data, and generates insights using SQL and data visualization.

---

## 🚀 Features

* Extracts job data from a REST API (JSON format)
* Cleans and preprocesses data using Pandas
* Stores structured data in SQLite database
* Performs SQL queries to analyze job trends
* Generates insights such as:

  * Top job locations
  * Most in-demand roles
  * Top hiring companies
  * Remote vs non-remote jobs
  * Salary availability
* Visualizes insights using Matplotlib

---

## 🛠️ Tech Stack

* Python
* Pandas
* SQLite (SQL)
* Matplotlib
* Requests (API handling)
* Git & GitHub

---

## 📂 Project Structure

job-scraper-pipeline/
│
├── data/
│   └── jobs.db
│
├── src/
│   ├── scrape.py
│   ├── clean.py
│   ├── transform.py
│   ├── db.py
│   ├── visualize.py
│
├── main.py
├── README.md
└── requirements.txt

---

## ⚙️ How to Run

1. Clone the repository:
   git clone https://github.com/Ri5hav/job-scraper-pipeline.git
   cd job-scraper-pipeline

2. Install dependencies:
   pip install -r requirements.txt

3. Run the pipeline:
   python main.py

---

## 📊 Example Insights

* Identified top hiring locations and companies
* Analyzed demand for different job roles
* Observed trends in remote job availability
* Evaluated salary disclosure patterns

---

## 🧠 Learning Outcomes

* Built an ETL pipeline using Python
* Worked with REST APIs and JSON data
* Applied data cleaning and preprocessing techniques
* Used SQL for data analysis
* Created visualizations for data-driven insights

---

## 🔮 Future Improvements

* Add automation using schedulers
* Build a dashboard using Streamlit or Power BI
* Extend analysis with more datasets

---

## 👤 Author

Rishav Kumar
GitHub: https://github.com/Ri5hav
