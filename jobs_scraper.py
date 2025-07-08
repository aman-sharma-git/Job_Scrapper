import os
import requests

def get_job_listings(limit=20):
    SERP_API_KEY = os.getenv(7108af40d4ee89599e5acb4d538d042769e5b990d1a967c33421595fd9de8276)
    query = "Entry-level Data Analyst OR MIS Executive site:linkedin.com/jobs OR site:wellfound.com OR site:internshala.com OR site:workindia.in OR site:indeed.com OR site:glassdoor.com"

    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERP_API_KEY,
        "num": 30
    }

    res = requests.get(url, params=params)
    data = res.json()

    links = []
    if "organic_results" in data:
        for result in data["organic_results"]:
            link = result.get("link")
            if link and any(site in link for site in [
                "linkedin.com/jobs", "wellfound.com", "internshala.com", 
                "workindia.in", "indeed.com", "glassdoor.com"
            ]):
                if link not in links:
                    links.append(link)
            if len(links) >= limit:
                break

    print("🔗 Found job links via SerpAPI:")
    for link in links:
        print(link)

    jobs = [{"title": "Data Analyst Role", "company": "Startup", "link": link} for link in links]
    return jobs
