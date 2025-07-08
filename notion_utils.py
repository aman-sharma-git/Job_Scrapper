
import os
import requests

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def job_exists(link):
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    payload = {
        "filter": {
            "property": "Link",
            "url": {
                "equals": link
            }
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    return len(data.get("results", [])) > 0

def add_jobs_to_notion(jobs, today):
    added = 0
    for job in jobs:
        if job_exists(job["link"]):
            continue

        payload = {
            "parent": {"database_id": DATABASE_ID},
            "properties": {
                "Title": {"title": [{"text": {"content": job["title"]}}]},
                "Company": {"rich_text": [{"text": {"content": job["company"]}}]},
                "Link": {"url": job["link"]},
                "Date": {"date": {"start": today}},
                "Apply Status": {"select": {"name": "Not Applied ✅"}}
            }
        }
        url = "https://api.notion.com/v1/pages"
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            added += 1
    return added

