// YouTube transcripts for RAG / LLM prompts.
// Usage: APIFY_TOKEN=... node youtube-transcripts.mjs <video|@channel|playlist URL> [...]
// Actor: https://apify.com/murch1k/youtube-transcript-scraper ($5 per 1,000 transcripts)
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const urls = process.argv.slice(2);
const run = await client.actor('murch1k/youtube-transcript-scraper').call({
    urls: urls.length ? urls : ['https://www.youtube.com/watch?v=dQw4w9WgXcQ'],
    maxVideosPerSource: 10,
    languages: ['en'],
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const v of items) console.log(`${v.title} — ${v.wordCount} words\n${v.transcript.slice(0, 300)}…\n`);
