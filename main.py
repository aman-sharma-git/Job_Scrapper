
from jobs_scraper import get_job_listings
from notion_utils import add_jobs_to_notion
from datetime import date

if __name__ == "__main__":
    print("🔍 Searching for jobs...")
    jobs = get_job_listings()
    today = date.today().strftime("%Y-%m-%d")
    added = add_jobs_to_notion(jobs, today)
    print(f"✅ Added {added} new jobs to Notion.")
