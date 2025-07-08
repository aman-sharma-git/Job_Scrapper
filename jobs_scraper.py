import requests
from bs4 import BeautifulSoup

def get_job_listings(limit=20):
    query = (
        "Entry-level Data Analyst OR MIS Executive "
        "site:linkedin.com/jobs OR site:wellfound.com "
        "OR site:internshala.com OR site:workindia.in "
        "OR site:indeed.com OR site:glassdoor.com"
    )
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}&num=30"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)

    print("🔍 Response Status:", res.status_code)
    if "Our systems have detected unusual traffic" in res.text:
        print("⚠️ Google is blocking this bot with a CAPTCHA. Try using SerpAPI or Bing API.")
        return []

    soup = BeautifulSoup(res.text, "html.parser")
    links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if any(site in href for site in [
            "linkedin.com/jobs", "wellfound.com", "internshala.com", 
            "workindia.in", "indeed.com", "glassdoor.com"
        ]):
            link = href.split("&")[0].replace("/url?q=", "")
            if link not in links:
                links.append(link)
        if len(links) >= limit:
            break

    print("🔗 Found links:")
    for link in links:
        print(link)

    jobs = [{"title": "Data Analyst Role", "company": "Startup", "link": link} for link in links]
    return jobs
