
import requests
import os

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def job_exists(link):
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    data = {"filter": {"property": "Link", "url": {"equals": link}}}
    res = requests.post(url, headers=headers, json=data)
    return res.json().get("results", []) != []

def add_jobs_to_notion(jobs, date):
    added = 0
    for job in jobs:
        if job_exists(job["link"]):
            continue
        data = {
            "parent": {"database_id": DATABASE_ID},
            "properties": {
                "Job Title": {"title": [{"text": {"content": job["title"]}}]},
                "Company": {"rich_text": [{"text": {"content": job["company"]}}]},
                "Link": {"url": job["link"]},
                "Date": {"date": {"start": date}},
                "Apply Status": {"select": {"name": "Not Applied"}}
            }
        }
        res = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)
        if res.status_code == 200:
            added += 1
    return added
