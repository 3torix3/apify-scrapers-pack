# Apify Scrapers Pack — Scraper APIs for RAG, LangChain & MCP AI Agents

**30 ready-to-use web scraper APIs** with copy-paste **Python** and **Node.js** examples: YouTube transcripts for RAG,
**RAG web search**, website-to-Markdown, career-site jobs, contact extraction, Google Maps leads, Amazon, TikTok and more.
Every scraper runs on [Apify](https://apify.com) — no servers, no proxies, no browser to maintain — and plugs straight into
**LangChain**, **LlamaIndex**, **n8n / Make / Zapier**, or any **MCP client** (Claude Desktop, Claude Code, Cursor, VS Code) via the
**Apify MCP server**.

> **Start free:** the Apify Free plan includes monthly platform credits, which cover thousands of results from these
> pay-per-result scrapers ($1.50–$3 per 1,000). No credit card needed to try. You only pay for results you receive —
> failed pages, private videos and duplicates are not charged.

**Keywords:** free scraper API · RAG web search · LangChain scrapers · MCP server Apify · YouTube transcript API ·
website to markdown · web scraping for LLM · AI agent tools · lead generation API · jobs API.

---

## Contents
- [Quick start (Python / Node.js)](#quick-start)
- [Use as tools for AI agents (MCP)](#use-as-tools-for-ai-agents-mcp)
- [LangChain & RAG](#langchain--rag)
- [Scraper catalog](#scraper-catalog)
- [Examples in this repo](#examples-in-this-repo)
- [FAQ](#faq)


## Dedicated repos

- [youtube-transcripts-for-rag](https://github.com/3torix3/youtube-transcripts-for-rag) — YouTube transcripts: Python, JS, LangChain, LlamaIndex, n8n, MCP
- [career-site-jobs-api](https://github.com/3torix3/career-site-jobs-api) — jobs from Greenhouse, Lever, Ashby, Workday… career sites
- [website-contact-extractor](https://github.com/3torix3/website-contact-extractor) — emails, phones and socials from a list of domains

## Quick start

1. Create a free account at [apify.com](https://console.apify.com/sign-up) and copy your API token
   (Console → Settings → API & Integrations).
2. `export APIFY_TOKEN=<your token>`
3. Run an example:

```bash
# Python
pip install -r python/requirements.txt
python python/youtube_transcripts_rag.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Node.js (18+)
cd node && npm install
node youtube-transcripts.mjs "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

The pattern is the same for every scraper — call the Actor, read its dataset:

```python
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("torix33/rag-web-search").call(run_input={"queries": ["best vector database 2026"], "maxResultsPerQuery": 5})
for page in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(page["title"], page["url"], len(page["markdown"]))
```

No SDK? One HTTP call returns the results directly:

```bash
curl -X POST "https://api.apify.com/v2/acts/torix33~rag-web-search/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" -d '{"queries": ["langchain vs llamaindex"], "maxResultsPerQuery": 5}'
```

## Use as tools for AI agents (MCP)

The hosted **Apify MCP server** exposes any of these scrapers as tools to Claude, Cursor, VS Code or any MCP client.
Copy [`mcp/claude_desktop_config.json`](mcp/claude_desktop_config.json):

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=torix33/rag-web-search,torix33/website-to-markdown,torix33/youtube-transcript-scraper",
      "headers": { "Authorization": "Bearer <APIFY_TOKEN>" }
    }
  }
}
```

Now ask your agent: *"Search the web for the latest pgvector benchmarks and summarise them with sources"* — it calls
**RAG Web Search** and gets clean Markdown back.

## LangChain & RAG

```python
from langchain_apify import ApifyActorsTool
tools = [ApifyActorsTool("torix33/rag-web-search"), ApifyActorsTool("torix33/youtube-transcript-scraper")]
# pass `tools` to create_react_agent(...) / LangGraph
```

Full examples: [`python/langchain_agent.py`](python/langchain_agent.py) (agent with tools) and
[`python/youtube_transcripts_rag.py`](python/youtube_transcripts_rag.py) (transcripts → chunks → vector store).
For a whole documentation site use **Website to RAG Chunks** — it returns heading-aware chunks with token counts
and content hashes, ready for Pinecone, Qdrant, Weaviate, Chroma or pgvector.

## Scraper catalog

All scrapers: pay per result, no login, no API keys for the target sites, exports to JSON / CSV / Excel, schedules and webhooks.

### 🤖 AI, LLM & RAG

| Scraper | What you get | Price |
|---|---|---|
| [RAG Web Search](https://apify.com/torix33/rag-web-search) | Web search API for AI agents and RAG: top results with full page content as clean Markdown. Region, time range, char limits | $3 / 1,000 results |
| [Website to Markdown for LLM & RAG](https://apify.com/torix33/website-to-markdown) | Convert web pages or whole websites to clean Markdown for LLMs, RAG and AI agents. Readability extraction, sitemap crawl, fast HTTP | $3 / 1,000 pages |
| [Website to RAG Chunks](https://apify.com/torix33/website-to-rag-chunks) | Crawl a website or docs into LLM-ready Markdown chunks with heading paths, token counts and content hashes for Pinecone, Qdrant, pgvector | $3 / 1,000 pages |
| [YouTube Transcript Scraper](https://apify.com/torix33/youtube-transcript-scraper) | Download YouTube transcripts in bulk: videos, Shorts, channels, playlists and search. Timestamps, SRT, auto-translate. No API key | $5 / 1,000 transcripts |
| [Keyword Research](https://apify.com/torix33/keyword-research-autocomplete) | Free-style keyword research tool: Google, YouTube, Amazon, Bing & DuckDuckGo autocomplete suggestions, questions, intent tags | $3 / 1,000 keywords |
| [Google Trends Scraper](https://apify.com/torix33/google-trends-scraper) | Google Trends API alternative: interest over time, interest by region, related queries & topics, Trending Now for any country | $3 / 1,000 results |
| [Substack Scraper](https://apify.com/torix33/substack-scraper) | Scrape Substack newsletters, subscriber counts, authors and posts with full article text. Search, categories, leaderboards | $3 / 1,000 results |

### 💼 Jobs data

| Scraper | What you get | Price |
|---|---|---|
| [Career Site Jobs Scraper](https://apify.com/torix33/career-site-jobs-scraper) | Scrape every open job from company career sites: Greenhouse, Lever, Ashby, Workable, SmartRecruiters, Workday & more. One clean schema | $6 / 1,000 jobs |
| [LinkedIn Jobs Scraper](https://apify.com/torix33/linkedin-jobs-scraper) | Scrape LinkedIn job postings without login: title, company, salary, full description, seniority, applicants. All LinkedIn filters | $3 / 1,000 jobs |
| [StepStone Jobs Scraper](https://apify.com/torix33/stepstone-jobs-scraper) | Scrape StepStone job ads in Germany, Austria, Belgium and the Netherlands: salary, full description, company, location | $2.5 / 1,000 jobs |
| [Dice Jobs Scraper](https://apify.com/torix33/dice-jobs-scraper) | Scrape Dice.com tech jobs: salary, full description, contract/C2C, remote, recruiter vs direct hire, visa sponsorship | $2.5 / 1,000 jobs |
| [Remote Jobs Aggregator](https://apify.com/torix33/remote-jobs-aggregator) | Collect remote jobs from 7 boards in one clean, deduplicated feed: keywords, location, posted-within filters. Ideal for job sites & alerts | $2 / 1,000 jobs |

### 🎯 B2B lead generation

| Scraper | What you get | Price |
|---|---|---|
| [Website Contact Details Extractor](https://apify.com/torix33/website-contact-details-extractor) | Extract emails, phone numbers and social profiles from any list of websites. One row per domain, Cloudflare-protected emails decoded | $3 / 1,000 websites |
| [Google Maps Scraper](https://apify.com/torix33/google-maps-scraper) | Scrape Google Maps businesses: name, address, phone, website, rating, reviews count, plus emails and social links from their websites | $3 / 1,000 places |
| [Website Tech Stack Detector](https://apify.com/torix33/website-tech-stack-detector) | Detect the tech stack of any website: CMS, e-commerce platform, analytics, CRM, live chat, hosting and email provider (MX) | $2 / 1,000 websites |
| [LinkedIn Company Scraper](https://apify.com/torix33/linkedin-company-scraper) | Scrape LinkedIn company pages without login: industry, company size, HQ, founded, website, followers, employee count, similar companies | $3 / 1,000 companies |
| [Google Play Scraper](https://apify.com/torix33/google-play-scraper) | Scrape Google Play apps with developer email, website and address, ratings and unlimited reviews. Any country | $3 / 1,000 apps + $0.8 / 1,000 reviews |
| [App Store Scraper](https://apify.com/torix33/app-store-scraper) | Scrape Apple App Store apps, developer portfolios, ratings and reviews from many countries. ASO research | $2 / 1,000 apps + $0.8 / 1,000 reviews |

### 🛒 E-commerce

| Scraper | What you get | Price |
|---|---|---|
| [Amazon Product Scraper](https://apify.com/torix33/amazon-product-scraper) | Scrape Amazon.com search results, categories and product pages: price, rating, reviews count, Best Sellers Rank, specs, real US ZIP pricing | $3 / 1,000 products |
| [Amazon Best Sellers Scraper](https://apify.com/torix33/amazon-bestsellers-scraper) | Scrape Amazon Best Sellers top 100 for any category and subcategory: rank, ASIN, price, rating, reviews. Real US prices | $3 / 1,000 products |
| [AliExpress Scraper](https://apify.com/torix33/aliexpress-scraper) | Scrape AliExpress search and category results: price, exact orders sold, rating, shipping, store. Filters for price, free shipping, Choice | $3 / 1,000 products |
| [Shopify Store Scraper](https://apify.com/torix33/shopify-store-scraper) | Scrape any Shopify store: all products, variants, SKUs, prices, compare-at prices, stock and images. Daily price monitoring with "updated since" | $2 / 1,000 results |

### 📺 Social media, video & news

| Scraper | What you get | Price |
|---|---|---|
| [YouTube Scraper](https://apify.com/torix33/youtube-scraper) | Scrape YouTube search results, channels, playlists, videos and Shorts: views, exact likes, comments, chapters, hashtags. No API key | $2.5 / 1,000 videos |
| [YouTube Comments Scraper](https://apify.com/torix33/youtube-comments-scraper) | Scrape YouTube comments and replies from videos, Shorts, channels and playlists. Likes, pinned, hearted flags. No API quota | $1.5 / 1,000 comments |
| [YouTube Channel Scraper](https://apify.com/torix33/youtube-channel-scraper) | Scrape YouTube channels: subscribers, total views, video count, country, joined date, links. Discover channels by keyword. No API key | $3 / 1,000 channels |
| [Google News Scraper](https://apify.com/torix33/google-news-scraper) | Scrape Google News by keyword, topic and date range. Resolves news.google.com links to real publisher URLs. Any language & country | $2 / 1,000 articles |
| [Telegram Channel Scraper](https://apify.com/torix33/telegram-channel-scraper) | Scrape public Telegram channels without login: posts, views, reactions, media, links and channel info. Full history or since a date | $2 / 1,000 posts |
| [Pinterest Scraper](https://apify.com/torix33/pinterest-scraper) | Scrape Pinterest pins, boards, profiles and search results: images, outbound links, saves, followers, monthly views. No login | $2 / 1,000 results |
| [Threads Profile Scraper](https://apify.com/torix33/threads-profile-scraper) | Scrape Threads (Meta) profiles without login: followers, bio, verified, engagement rate, average likes and latest posts | $3 / 1,000 profiles + $1 / 1,000 posts |
| [TikTok Profile Scraper](https://apify.com/torix33/tiktok-profile-scraper) | Scrape TikTok profiles: exact followers, likes, video count, engagement, bio link and emails, verified & TikTok Shop flags. No login | $3 / 1,000 profiles |

## Examples in this repo

| File | What it shows |
|---|---|
| [`python/youtube_transcripts_rag.py`](python/youtube_transcripts_rag.py) | YouTube transcripts → overlapping chunks → JSONL for any vector DB |
| [`python/langchain_agent.py`](python/langchain_agent.py) | LangChain/LangGraph agent with RAG Web Search + YouTube transcripts as tools |
| [`python/career_jobs.py`](python/career_jobs.py) | All open jobs from Greenhouse, Lever, Ashby, Workday… career sites → CSV |
| [`python/contact_extractor.py`](python/contact_extractor.py) | Emails, phones and socials for a list of company websites → CSV |
| [`node/youtube-transcripts.mjs`](node/youtube-transcripts.mjs) | Same transcript flow in Node.js |
| [`node/career-jobs.mjs`](node/career-jobs.mjs) | Career-site jobs in Node.js |
| [`node/contacts.mjs`](node/contacts.mjs) | Website contact extraction in Node.js |
| [`mcp/claude_desktop_config.json`](mcp/claude_desktop_config.json) | MCP config for Claude Desktop / Cursor / VS Code |

## FAQ

**Is this a free scraper API?** The scrapers are pay-per-result, but Apify's Free plan gives monthly credits, so small
projects and testing usually cost nothing. There is no subscription on the scrapers themselves.

**Do I need proxies or a headless browser?** No. Each Actor handles HTTP, retries and proxies on Apify's side.

**Can my AI agent call these directly?** Yes — through the Apify MCP server (above), LangChain's `langchain-apify`
package, or a plain HTTP call from any agent framework (OpenAI tools, CrewAI, LlamaIndex, n8n AI agent).

**Is scraping legal?** These Actors only read publicly available data. You are responsible for complying with the target
site's terms and with data-protection laws (GDPR, CCPA) — especially for personal data such as contact details.

**Something broken or missing?** Open an issue here or on the Actor's *Issues* tab in Apify Store.

## License

Example code: MIT. The scrapers run on the Apify platform under their Store terms.
