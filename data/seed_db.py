from app.database import init_db, add_job

if __name__ == "__main__":
    init_db()
    job_id = add_job("Junior Data Analyst", "Required skills: Python, SQL, Pandas, Excel, Git")
    print(f"Created sample job {job_id}")
