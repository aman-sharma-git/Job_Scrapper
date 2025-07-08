
import os
import requests

def get_job_listings(limit=20):
    SERP_API_KEY = os.getenv(8edd20da55ce2e23e3b857d6381969e2179bc0a15a9533e09f7d85acd284fc23)
    if not SERP_API_KEY:
        print("❌ SERP_API_KEY not found in environment variables.")
        return []

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
