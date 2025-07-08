
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_job_listings(limit=15):
    query = "Entry-level Data Analyst OR MIS Executive site:linkedin.com/jobs OR site:wellfound.com OR site:internshala.com OR site:workindia.in OR site:indeed.com OR site:glassdoor.com
"
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}&num=25"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "linkedin.com/jobs" in href or "wellfound.com" in href:
            text = a.get_text().lower()
            if "today" in text or "posted today" in text:
                clean_url = href.split("&")[0].replace("/url?q=", "")
                links.append(clean_url)
        if len(links) >= limit:
            break
    jobs = [{"title": "Data Analyst Role", "company": "Startup", "link": link} for link in links]
    return jobs
