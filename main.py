
from jobs_scraper import get_job_listings
from notion_utils import add_jobs_to_notion
import datetime

if __name__ == "__main__":
    print("🔍 Searching for jobs...")
    jobs = get_job_listings(limit=15)
    today = datetime.date.today().isoformat()
    added = add_jobs_to_notion(jobs, today)
    print(f"✅ Added {added} new jobs to Notion.")
