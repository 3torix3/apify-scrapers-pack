// Open jobs from company career sites (Greenhouse, Lever, Ashby, Workable, SmartRecruiters, Workday…).
// Usage: APIFY_TOKEN=... node career-jobs.mjs stripe.com huggingface.co
// Actor: https://apify.com/murch1k/career-site-jobs-scraper ($6 per 1,000 jobs)
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const companies = process.argv.slice(2);
const run = await client.actor('murch1k/career-site-jobs-scraper').call({
    companies: companies.length ? companies : ['huggingface.co', 'https://boards.greenhouse.io/stripe'],
    keywords: ['engineer', 'data'],
    postedWithinDays: 30,
    maxResults: 200,
    includeDescription: false,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.table(items.map(({ companyName, title, location, isRemote, url }) => ({ companyName, title, location, isRemote, url })));
