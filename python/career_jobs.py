"""All open jobs from company career sites (Greenhouse, Lever, Ashby, Workable, SmartRecruiters, Workday...) -> jobs.csv

Usage: APIFY_TOKEN=... python career_jobs.py stripe.com huggingface.co https://jobs.lever.co/palantir
Actor: https://apify.com/murch1k/career-site-jobs-scraper ($3 per 1,000 jobs)
"""
import csv
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("murch1k/career-site-jobs-scraper").call(run_input={
    "companies": sys.argv[1:] or ["huggingface.co", "https://boards.greenhouse.io/stripe"],
    "keywords": ["engineer", "data"],      # title filter, empty = all jobs
    "postedWithinDays": 30,
    "maxResults": 200,                     # hard cost cap
    "includeDescription": False,
})
cols = ["companyName", "title", "location", "isRemote", "salaryText", "postedAt", "url"]
with open("jobs.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
    w.writeheader()
    for job in client.dataset(run["defaultDatasetId"]).iterate_items():
        w.writerow(job)
print("saved jobs.csv")
