#!/usr/bin/env python3
"""Followers, bio, and recent posts. No login required. Python, Node.js and cURL clients for the Instagram Profile Scraper on Apify, pay per result.

Command-line client for the themineworks/instagram-profile-scraper actor on Apify: runs it, waits for it
to finish and saves every result as JSON and CSV. Flags map 1:1 to the actor's input.
Free Apify account and API token: https://console.apify.com/sign-up
Docs and pricing: https://themineworks.com/actors/instagram-profile-scraper/
"""
import argparse, csv, json, os, sys
from apify_client import ApifyClient

ACTOR = "themineworks/instagram-profile-scraper"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--token", default=os.environ.get("APIFY_TOKEN"), help="Apify API token (or set APIFY_TOKEN)")
    ap.add_argument("--out", default="results", help="Output basename, writes .json and .csv")
    ap.add_argument("--usernames", help="Comma-separated. Instagram usernames to scrape (without the @)")
    ap.add_argument("--include-posts", action=argparse.BooleanOptionalAction, help="Kept for compatibility")
    ap.add_argument("--max-posts", type=int, help="No longer used")
    ap.add_argument("--include-post-details", action=argparse.BooleanOptionalAction, help="Add the exact publish time, caption, coauthor usernames, video URL and video duration to…")
    ap.add_argument("--allow-browser-fallback", action=argparse.BooleanOptionalAction, help="When the fast HTTP tiers can't resolve a username, this actor tries once more with a real…")
    ap.add_argument("--username", help="Convenience field for scraping just one profile")
    ap.add_argument("--max-days", type=int, help="No longer used")
    a = ap.parse_args()
    if not a.token:
        sys.exit("Provide --token or set APIFY_TOKEN. Free token: https://console.apify.com/sign-up")

    run_input = {}
    if a.usernames: run_input["usernames"] = [s.strip() for s in a.usernames.split(",") if s.strip()]
    if a.include_posts is not None: run_input["includePosts"] = a.include_posts
    if a.max_posts is not None: run_input["maxPosts"] = a.max_posts
    if a.include_post_details is not None: run_input["includePostDetails"] = a.include_post_details
    if a.allow_browser_fallback is not None: run_input["allowBrowserFallback"] = a.allow_browser_fallback
    if a.username is not None: run_input["username"] = a.username
    if a.max_days is not None: run_input["maxDays"] = a.max_days

    client = ApifyClient(a.token)
    print(f"Running {ACTOR} ...")
    run = client.actor(ACTOR).call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    with open(a.out + ".json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    keys = []
    for it in items:
        keys += [k for k in it if k not in keys]
    if items:
        with open(a.out + ".csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
            w.writeheader()
            for it in items:
                w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k, v in it.items()})
    print(f"Done: {len(items)} results saved to {a.out}.json and {a.out}.csv")


if __name__ == "__main__":
    main()
