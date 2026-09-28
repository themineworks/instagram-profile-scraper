# Instagram Profile Scraper: Followers, Post Count, No Login

Scrape public Instagram profiles: followers, following, bio, verified status, external links, and recent posts. No login or cookies required. Pay per profile delivered, and failed results are never charged.

**Run it on Apify:** [apify.com/themineworks/instagram-profile-scraper](https://apify.com/themineworks/instagram-profile-scraper)
**Docs, FAQ and pricing:** [themineworks.com/actors/instagram-profile-scraper](https://themineworks.com/actors/instagram-profile-scraper/)

**Price:** From $1.20 per 1,000 profiles on Apify's higher plans ($2.00 on the free plan). Failed and empty results are never charged.

## What it returns

* Followers, following, bio, verified status
* Recent posts with engagement metrics
* External links and contact info extracted
* No login, no cookies, no API key
* Failed lookups are never charged

## Quick start

You need a free [Apify account](https://console.apify.com/sign-up) and its API token (Settings, API & Integrations).

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("themineworks/instagram-profile-scraper").call(run_input={
    "usernames": [
        "nasa",
        "natgeo"
    ]
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### Node.js

```bash
npm install apify-client
```

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: 'YOUR_APIFY_TOKEN' });
const run = await client.actor('themineworks/instagram-profile-scraper').call({
    "usernames": [
        "nasa",
        "natgeo"
    ]
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL

One request that runs the actor and returns the results in the response (for runs under 5 minutes):

```bash
curl -X POST "https://api.apify.com/v2/acts/themineworks~instagram-profile-scraper/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"usernames": ["nasa", "natgeo"]}'
```

### Command line

This repo includes ready-made clients that save results to JSON and CSV:

```bash
python3 instagram_profile_scraper.py --token YOUR_APIFY_TOKEN --usernames "nasa,natgeo"
node instagram_profile_scraper.mjs --token YOUR_APIFY_TOKEN --usernames "nasa,natgeo"
```

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `usernames` | array |  | Instagram usernames to scrape (without the @) |
| `includePosts` | boolean | `false` | Kept for compatibility |
| `maxPosts` | integer | `500` | No longer used |
| `includePostDetails` | boolean | `false` | Add the exact publish time, caption, coauthor usernames, video URL and video duration to each reel (up to 50… |
| `allowBrowserFallback` | boolean | `true` | When the fast HTTP tiers can't resolve a username, this actor tries once more with a real (residential-proxy)… |
| `username` | string |  | Convenience field for scraping just one profile |
| `maxDays` | integer |  | No longer used |

## Output

One row per result, as JSON, CSV, Excel or through the API.

| Field | Type | Description |
|---|---|---|
| `username` | string | Instagram username |
| `full_name` | ['string', 'null'] | Display name of the account |
| `biography` | ['string', 'null'] | Profile bio text |
| `followers` | ['integer', 'null'] | Number of followers |
| `following` | ['integer', 'null'] | Number of accounts followed |
| `posts_count` | ['integer', 'null'] | Total number of posts |
| `is_verified` | ['boolean', 'null'] | Whether the account is verified |
| `is_private` | ['boolean', 'null'] | Whether the account is private |
| `is_business` | ['boolean', 'null'] | Whether the account is a business account |
| `category` | ['string', 'null'] | Business category of the account |
| `profile_pic_url` | ['string', 'null'] | URL of the profile picture |
| `external_url` | ['string', 'null'] | External link in the profile bio |
| `user_id` | ['string', 'null'] | Instagram internal user ID |
| `profile_url` | ['string', 'null'] | Full URL to the Instagram profile |
| `source` | string | Scraping tier that produced this record (graphql, html-og, browser) |
| `scraped_at` | string | ISO 8601 timestamp of when the record was scraped |
| `posts_included` | ['integer', 'null'] | Number of this profile's recent posts also delivered as their own rows in this run (Model B: each post is a… |
| `latestReels` | ['array', 'null'] | The profile's most recent reels, nested in this row (not billed separately) |
| `median_play_count` | ['integer', 'null'] | Median play count of the non-pinned reels in latestReels |
| `reels_status` | ['string', 'null'] | ok, none (no reels), private, unavailable (restricted or gated for logged-out viewers), blocked, partial, or… |
| `reels_note` | ['string', 'null'] | Plain-language explanation whenever reels_status is not ok or none |
| `post_details_status` | ['string', 'null'] | With includePostDetails: ok, partial, blocked or route_broken |
| `_type` | ['string', 'null'] | "post" for a flattened recent-post row; absent for a profile row |
| `profile_username` | ['string', 'null'] | Set on post rows only, the profile this post belongs to |
| `shortcode` | ['string', 'null'] | Post row only, Instagram post shortcode |
| `url` | ['string', 'null'] | Post row only, direct post URL |
| `caption` | ['string', 'null'] | Post row only, post caption |
| `like_count` | ['integer', 'null'] | Post row only, like count |
| `comment_count` | ['integer', 'null'] | Post row only, comment count |
| `is_video` | ['boolean', 'null'] | Post row only, whether the post is a video |

## Use it from an AI agent

The actor works as a tool in Claude, Cursor or any MCP client through Apify's MCP server:

```
https://mcp.apify.com/?tools=themineworks/instagram-profile-scraper
```

## FAQ

### Does this scraper require an Instagram login or API key?

No. The scraper accesses publicly visible Instagram profile pages without any login, cookies, or Meta API credentials.

### What data does each profile return?

Username, full name, bio, follower count, following count, post count, verified status, external link, business category, and the most recent posts with like and comment counts.

### Can I scrape private Instagram accounts?

No. Only public profiles are accessible without authentication. Private accounts are not visible to unauthenticated requests.

### Is there an official Instagram API?

Meta offers the Instagram Graph API but it requires a Facebook app approval, business account connection, and is limited to accounts you own or manage. For scraping third-party public profiles, no official API exists.

### What is the pricing model?

Pay per profile delivered. Failed lookups on private or deactivated accounts are never charged.

### How much does the Instagram Profile Scraper cost?

From $1.20 per 1,000 profiles on Apify's higher plans ($2.00 on the free plan). Failed and empty results are never charged. You can cap what a single run may spend with the maximum cost setting on Apify.

### Can I export the results to CSV or Excel?

Yes. Every run saves to an Apify dataset you can download as JSON, CSV, Excel or XML, or read through the API. The Python and Node clients in this repo also write the results to local files.

### Can I run it on a schedule?

Yes. Save your input as a task on Apify and attach a schedule, or call the API from your own cron job. Scheduled runs are billed the same way as manual ones.

## Related scrapers

* [Threads Scraper](https://themineworks.com/actors/threads-scraper/): Meta Threads data that returns actual data
* [Reddit Scraper](https://themineworks.com/actors/reddit-scraper/): Free Reddit data with full comment trees
* [LinkedIn Post Scraper](https://themineworks.com/actors/linkedin-post-search/): Search LinkedIn posts by keyword without login

Part of [The Mine Works](https://themineworks.com/): 151 pay-per-result scrapers with no login and no browser setup on your side.

## License

MIT © The Mine Works
