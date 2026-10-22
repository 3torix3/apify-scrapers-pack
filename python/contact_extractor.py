"""Emails, phones and social profiles for a list of company websites -> contacts.csv (one row per domain)

Usage: APIFY_TOKEN=... python contact_extractor.py apify.com crawlee.dev ...
Actor: https://apify.com/torix33/website-contact-details-extractor ($3 per 1,000 websites, failed sites are free)
Respect GDPR/CAN-SPAM when you use contact data for outreach.
"""
import csv
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("torix33/website-contact-details-extractor").call(run_input={
    "websites": sys.argv[1:] or ["https://apify.com", "https://crawlee.dev"],
    "maxPagesPerSite": 6,
    "sameDomainEmailsOnly": True,
})
with open("contacts.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["domain", "primaryEmail", "emails", "primaryPhone", "linkedin", "twitter"])
    for r in client.dataset(run["defaultDatasetId"]).iterate_items():
        s = r.get("socials") or {}
        w.writerow([r.get("domain"), r.get("primaryEmail"), " ".join(r.get("emails") or []),
                    r.get("primaryPhone"), " ".join(s.get("linkedin") or []), " ".join(s.get("twitter") or [])])
print("saved contacts.csv")
