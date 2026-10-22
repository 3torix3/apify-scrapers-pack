// Emails, phones and social profiles for a list of websites (one row per domain).
// Usage: APIFY_TOKEN=... node contacts.mjs apify.com crawlee.dev
// Actor: https://apify.com/torix33/website-contact-details-extractor ($3 per 1,000 websites, failed sites free)
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const sites = process.argv.slice(2);
const run = await client.actor('torix33/website-contact-details-extractor').call({
    websites: sites.length ? sites : ['https://apify.com', 'https://crawlee.dev'],
    maxPagesPerSite: 6,
    sameDomainEmailsOnly: true,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.table(items.map(({ domain, primaryEmail, primaryPhone }) => ({ domain, primaryEmail, primaryPhone })));
