# Y Combinator Jobs Scraper & API - Work at a Startup, YC Jobs

Y Combinator jobs scraper and API: search every open job at YC startups on Work at a Startup, YC's job board, live by job title, role, city, country or region, YC batch, visa terms, pay, equity, team size and posting date, and get each job's title, company, YC batch, places, remote or office, salary and equity as shown and as numbers, visa terms, years of experience, team size, company stage and its exact posting date, newest first. Turn on full details for the description as text and HTML.

Use it as a Work at a Startup API or YC jobs API with no login and no API key, a workatastartup.com and ycombinator.com/jobs scraper, or a daily YC startup job feed from the Apify Console, the Apify API, Python, JavaScript, n8n, Make or an AI agent over MCP, and export JSON, CSV or Excel. It reads the job list of every YC company that is hiring (1,500 companies, 6,300+ open jobs on 2026-11-10) at the moment of your run. Available as an [Apify Actor](https://apify.com/anshumanatrey/ycombinator-jobs-search). $0.000019 per job, the same with full details, and $0.015 per run start at the default 1 GB.

**Use it from an AI assistant:**

- **Claude** (claude.ai and the desktop app): [Add Y Combinator Jobs to Claude](https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Y%20Combinator%20Jobs&connectorUrl=https%3A%2F%2Fmcp.apify.com%3Ftools%3Danshumanatrey%2Fycombinator-jobs-search), click Continue, sign in to Apify, Allow, and ask in plain words.
- **Claude Code:** `claude mcp add --transport http ycombinator-jobs-search "https://mcp.apify.com?tools=anshumanatrey/ycombinator-jobs-search"`, then run `/mcp` to sign in to Apify.
- **Codex:** `codex mcp add ycombinator-jobs-search --url "https://mcp.apify.com?tools=anshumanatrey/ycombinator-jobs-search"`, then `codex mcp login ycombinator-jobs-search`.
- **Any other MCP client:** `https://mcp.apify.com?tools=anshumanatrey/ycombinator-jobs-search`, signed in with Apify or an `Authorization: Bearer <APIFY_TOKEN>` header.

## What does it do?

- **Every open YC job, live.** It reads YC's company directory for every company that is hiring, then each company's job list: 6,316 jobs at 1,500 companies on 2026-11-10, against the 6,323 Work at a Startup counted itself that hour (608 of 608 jobs sampled from its own role pages and search were found).
- **The exact posting date, newest first.** YC's job cards say "3 days" or "over 1 year". Each job's own page states the moment it was posted, and this actor reads it for every row it saves. YC numbers its jobs in posting order (every open job since 2021; 5 of 6,189 from 2019 and 2020 are out of order), so the newest come first and a short list costs only the pages it opens.
- **The last month by default.** 86% of the jobs open on YC were posted more than 30 days ago, some 8 years ago, so Posted in the last (`postedWithin`) starts at 30 days. Pick any time to get them all.
- **YC's own filters.** Role (engineering, design, sales, product, operations, and kinds such as backend or machine learning), YC batch (W25, Summer 2024, or 2025 for a whole year), visa terms (sponsors a visa, no visa needed, US only), minimum pay in US dollars, equity only, team size and company stage.
- **Pay and equity as numbers.** Pay is shown on 4 of 5 YC jobs: you get YC's text ("$150K - $190K", "EUR 60K - 80K", "$50 - $80 / hourly") and the numbers with their currency and period. Equity comes as text and as low and high percentages.
- **Places by any name.** A city, a country (US jobs written as US, United States or USA), a region (Europe, APAC, LatAm), Worldwide, the Bay Area, SF or NYC; a job remote in a country is found by that country. Type a place with the title, such as product manager in new york, and it is read as the place.
- **Checks job links.** Paste ycombinator.com or workatastartup.com job links, and each comes back open with the job, closed or not found.

## How is it different from other Y Combinator job scrapers?

The five Y Combinator job actors with the most users in the last 30 days on 2026-11-10, from the Store's own search (7 searches: ycombinator, y combinator, yc jobs, work at a startup, workatastartup, yc startup jobs, yc companies), as their own READMEs describe them:

| | This actor | nomad-agent | parsebird | memo23 | automation-lab |
|---|---|---|---|---|---|
| Jobs read | Every hiring YC company's list, live | Work at a Startup, at most 200 a run | Every company page | YC's role and place pages (20 to 37 jobs each) | The 20 jobs on ycombinator.com/jobs |
| Posting date | Exact, from each job's YC page | To the hour | Not stated | From the job page | YC's words ("3 days") |
| Newest first | Yes | Yes | Not stated | No | No |
| YC batch, visa, pay, equity, team size, stage | All six, as filters and on every row | Not as filters | As fields | As fields; batch and size for companies | Batch as a filter |
| Places | Cities, countries, regions, Worldwide, Bay Area | Countries and cities | Location text | Location text | Location text |
| Job links checked | Yes | No | No | Job page links | No |

- **The exact date.** Other actors give YC's rounded words ("about 1 month") or a date worked out from them. nomad-agent's README sample dates job 109851 on 2026-10-13; that job's own YC page says 2026-09-14. This actor reads the page.
- **Newest first without reading everything twice.** Job numbers rise with posting, so the newest jobs that match are opened first and the run stops once it holds your number of jobs.
- **Filters YC job seekers use.** Visa sponsorship, YC batch, minimum pay, equity, team size and stage are filters here, not only columns to sort later.
- **Clean, flat rows.** Pay and equity as numbers next to YC's text, places as text, no nested company or founder objects to unpack.
- **Exactly the number you asked for.** Number of jobs (`maxJobs`) is the number of rows you get, newest first, and you pay per row delivered.

## When should I use it?

- **Job seekers:** new YC startup jobs by title, role, place, visa and pay, every morning, with the exact posting time.
- **Recruiters and talent teams:** which YC companies hire for a role right now, at what pay and equity, by batch and team size.
- **Sales and investors:** YC companies hiring as a buying or growth signal, with their batch, stage and team size.
- **Data teams and AI agents:** one clean feed of YC's jobs through the API or MCP.

## How much does it cost to scrape Y Combinator jobs?

Pay per event: $0.019 per 1,000 jobs, the same with full details, plus $0.015 per run at the default 1 GB. Apify's free $5 monthly credit covers about 29,000 jobs in runs of 100. Platform usage is included, and there is no monthly fee.

| Event | Price | When it is charged |
|---|---|---|
| Job | $0.000019 | One saved job, and one checked link that is closed or not found |
| Job with details | $0.000019 | One saved job with full details on: the job's page is read for its date anyway, so details cost no more |
| Run start | $0.015 per GB of memory | Charged by Apify when a run starts: once up to 1 GB and once more for each extra GB, so $0.015 at the default 1 GB |

Y Combinator Jobs Scraper's Apify Store header shows the lowest discount-tier price, the GOLD price: $0.014 per 1,000 jobs. FREE and BRONZE users (Apify's Free and Starter plans) pay $0.000019 a job, SILVER (Scale) $0.000016, and GOLD (Business) and the enterprise tiers $0.000014, with full details or without. Each price is what a job costs on Apify at that plan's own rates, measured on Apify runs, plus a markup of 100% on the Free plan that falls to 80% on the enterprise tiers. The run start is a flat fee on every plan, $0.015 per GB of memory, and the header never shows it: it pays for reading the job lists of 1,500 companies, which every run does.

| Run (Free and Starter price, default memory) | Cost |
|---|---|
| 100 newest jobs | $0.017 |
| 100 jobs with full details | $0.017 |
| 1,000 jobs | $0.034 |
| Every open job, about 6,200 | $0.13 |

## How does the price compare with other Y Combinator scrapers?

Every actor on the Apify Store whose title names Y Combinator, YC or Work at a Startup, that returns job rows, and that had 5 or more users in the last 30 days, from the Store's own search on 2026-11-10 (7 searches, 412 actors read), ordered by users. Free-plan prices from each actor's current pricing.

| Actor | Users, 30 days | Per job | Start fee | What it reads |
|---|---|---|---|---|
| nomad-agent/ycombinator-was-scraper | 136 | $0.0001 | none | Work at a Startup, at most 200 jobs a run, each with its description; skips jobs already delivered |
| parsebird/yc-jobs-scraper | 64 | $0.00199 | $0.00005 | Every company page, with each job's detail page |
| memo23/y-combinator-scraper | 63 | $0.001, +$0.001 extra data | $0.008 | YC's role and place pages, and the company directory |
| scrapesage/ycombinator-scraper | 37 | $0.003, $0.004 a company | none | The company directory with founders and open jobs |
| automation-lab/ycombinator-jobs-scraper | 37 | $0.000045 | $0.00575 | The jobs embedded on ycombinator.com/jobs |
| antishock/workatastartup-jobs-scraper | 14 | $0.004 | $0.002 | Work at a Startup with company and founders |
| santamaria-automations/workatastartup-scraper | 11 | $0.003, $0.005 with details | $0.001 | Work at a Startup; posting date always empty |
| hipersoft/yc-jobs-scraper | 9 | $0.003 | $0.00005 | Every open job, with how long ago it was posted |
| benthepythondev/yc-jobs-scraper | 5 | $0.003 | $0.00005 | Work at a Startup by role or keyword |
| This actor | new | $0.000019, the same with details | $0.015 per GB | Every hiring YC company's jobs, live, with exact dates |

Where others are cheaper: this actor's run start, $0.015, is the highest in the table, because every run reads the job lists of all 1,500 hiring YC companies. On the Free and Starter plans, a run of fewer than about 185 jobs costs less on nomad-agent, which has no start fee and returns at most 200 jobs a run; on the Scale and Business plans, nomad-agent costs less for every run it can do; and automation-lab's 20 jobs cost less there. From 8 jobs a run, this actor costs less than each of the other seven, and per job it costs the least of all. Where others do more: nomad-agent gives every row its description at its base price and skips jobs you already received; memo23, scrapesage and parsebird add founders and company profiles; scrapesage and memo23 read the whole company directory, hiring or not.

## Which inputs does it take?

Nothing is required. Type a job title and press Start, or press Start with the form empty for the newest jobs of every kind.

| Field | What it does |
|---|---|
| Job titles to find (`searchTerms`) | One per line. A job matches when its title has every word: frontend also finds Front-End. A place typed with the title (product manager in new york) is read as the place. A YC job link is checked; a company link searches that company |
| Where the job is (`location`) | Cities, countries or regions: San Francisco, New York, United States, India, Europe, Worldwide, Bay Area. Remote alone asks for remote jobs; next to a city it changes nothing |
| Remote or office (`workType`) | remote, hybrid or onsite. A job that lists a Remote place, such as Remote (US), is remote |
| Posted in the last (`postedWithin`) | 24 hours, 3, 7, 14 or 30 days (the default), any time, or your own period such as 48 hours |
| Job role (`role`) | engineering, design, product, science, sales, marketing, support, operations, recruiting, finance, legal, or a kind of engineering: backend, frontend, full-stack, machine-learning, ai-engineer, data-science, devops, mobile, hardware, robotics |
| Experience (`experienceYears`) | Your years: 3, a range such as 2-5, 5+ or fresher. Keeps the jobs whose minimum is at or below them; internships count as 0 |
| YC batch (`batch`) | W25, S24, F26, P25 (Spring), Summer 2024, or a year such as 2025 |
| Company stage (`companyStage`) | early, growth or public |
| Team size (`teamSize`) | 1-10, 11-50, 51-200, 201-1000, 1000+, or your own range |
| Minimum pay, USD (`minSalaryUsd`) | US dollars a year, such as 150000; hourly and monthly pay count as a year's |
| Only with equity (`withEquity`) | Keeps the jobs that show an equity range |
| Visa terms (`visa`) | will-sponsor, not-required or us-only |
| Number of jobs (`maxJobs`) | How many, newest first: 100 by default, 0 for every match |
| Full details (`includeDetails`) | Adds the description as text and HTML, whether the job offers equity, and the city, state and country of its first place, at the same price |
| Leave out words (`excludeTerms`) | Drops jobs whose title has these words, such as senior or intern |
| Job type (`employmentType`) | full-time, contract or intern |
| Wider match (`searchDescriptions`) | Also keeps jobs whose description holds your words; slower, as each job that can match is opened |
| Only these companies (`companies`) | YC company names (Airbnb, Retool), a company link, or a `companySlug` |
| Job links to check (`jobUrls`) | ycombinator.com or workatastartup.com job links, to check whether they are still open, instead of searching |

Example input:

```json
{
  "searchTerms": ["software engineer", "founding engineer"],
  "location": ["San Francisco", "New York"],
  "visa": ["will-sponsor"],
  "minSalaryUsd": 150000,
  "postedWithin": "30 days",
  "maxJobs": 100
}
```

## What does the output look like?

One row per job, newest first. These rows are from a local run on 2026-11-10 at 10:38 UTC: software engineer in San Francisco, the last 30 days, 13 jobs saved in 26 s. A job with several places shows the first in `location` and the others in `otherLocations`, so a London job that also hires in San Francisco is a San Francisco match.

| Job title (`title`) | Company name (`company`) | YC batch (`batch`) | Main location (`location`) | Pay as shown (`salary`) | Equity as shown (`equity`) | Posted on (`postedAt`) |
|---|---|---|---|---|---|---|
| Software Engineer, Data Platform | Preload | F26 | San Francisco, CA | $150K - $225K | 0.25% - 1.50% | 2026-11-10 03:34 |
| Forward Deployed Software Engineer | Encord | W21 | London |  |  | 2026-11-04 21:50 |
| Software Engineer | Reflex | W23 | San Francisco, CA, US | $130K - $175K | 0.10% | 2026-11-04 20:51 |
| Founding Engineer, Software | Fort | W26 | San Francisco, CA, US | $130K - $210K | 0.30% - 1.20% | 2026-11-03 19:48 |
| Staff Software Engineer, Fulfillment Expansion | Whatnot | W20 | San Francisco, CA | $230K - $290K |  | 2026-11-03 15:20 |

One row as JSON:

```json
{
  "title": "Software Engineer, Data Platform",
  "company": "Preload",
  "location": "San Francisco, CA",
  "otherLocations": [],
  "workType": "onsite",
  "employmentType": "full-time",
  "department": "Engineering",
  "salary": "$150K - $225K",
  "postedAt": "2026-11-10T03:34:40Z",
  "jobUrl": "https://www.ycombinator.com/companies/preload/jobs/7hbolpR-software-engineer-data-platform",
  "applyUrl": "https://account.ycombinator.com/authenticate?continue=https%3A%2F%2Fwww.workatastartup.com%2Fapplication%3Fsignup_job_id%3D121721&defaults%5BsignUpActive%5D=true&defaults%5Bwaas_company%5D=36510",
  "status": "open",
  "platform": "ycombinator",
  "companySlug": "preload",
  "companyWebsite": "https://preload.ai",
  "jobId": "121721",
  "checkedAt": "2026-11-10T10:38:17+00:00",
  "experienceMin": 2,
  "experienceMax": null,
  "batch": "F26",
  "roleType": "Backend",
  "equity": "0.25% - 1.50%",
  "equityMin": 0.25,
  "equityMax": 1.5,
  "visa": "US citizenship/visa not required",
  "schoolYear": null,
  "skills": ["Python", "Distributed Systems"],
  "companyOneLiner": "Sensorimotor context for physical AI",
  "teamSize": 3,
  "companyStage": "early",
  "industry": "B2B",
  "workAtAStartupUrl": "https://www.workatastartup.com/jobs/121721",
  "salaryMin": 150000,
  "salaryMax": 225000,
  "salaryCurrency": "USD",
  "salaryPeriod": "year"
}
```

Full details add `description`, `descriptionHtml`, `offersEquity`, `city`, `region` (the state) and `country` with `countryCode`. A checked link that is closed comes back with its `status` and link, and the other fields empty. A run also writes an `OUTPUT` record: how many jobs it read, how many matched and were saved, any notes on how your input was read, and the calls made.

## How fast is it?

About 40 seconds at the default 1 GB. Measured on Apify on 2026-11-10 (build 1.0.2): the form as it opens (100 newest jobs) took 39 s and 1,612 calls; software engineer 47 s; founding engineer in San Francisco 41 s; 50 sales jobs in New York with full details 45 s; every YC filter at once 41 s; 1,000 jobs 78 s; and every open job, 6,189 of them, 279 s (22 jobs a second, 217 MB of memory). A word searched in descriptions takes longer, since each job that can match is opened: rust took 97 s and 2,806 calls for 12 jobs. Most of a run is reading 1,500 company job lists, 32 at a time, which is CPU-bound: at 512 MB the same searches took 61 to 94 s for 11% less cost, and at 2 GB software engineer took 21 s for two start events.

## Common questions

### Is Work at a Startup the same as Y Combinator's job board?

Yes. Work at a Startup (workatastartup.com) is the job board Y Combinator runs for its companies, and the jobs on ycombinator.com/jobs and on each company's ycombinator.com page are the same jobs. Y Combinator Jobs Scraper reads them through ycombinator.com, where each job's page states its posting date, and gives each row both links.

### Which posting date does it use?

Y Combinator Jobs Scraper uses the posting date each job's own YC page states (`datePosted`), to the second, for the order and for Posted in the last (`postedWithin`). YC's job cards show only words such as "about 1 month"; the actor uses those words to skip jobs that cannot be in your period and opens the rest. A job's number on YC grows with posting, so jobs come newest first.

### Why does it find fewer jobs than Work at a Startup counts?

Work at a Startup counts every open job, 6,323 on 2026-11-10, and 86% of them were posted more than a month ago: the default period, 30 days, keeps about 870. Pick any time to search them all. Y Combinator Jobs Scraper also keeps a job posted twice by one company, with the same title at the same place, once (the newest), which leaves about 6,200. A run that saves no job says why, and how to loosen it: founding engineer in batch W12 says "415 jobs had your words but not your other filters: the YC batch alone left out 415. To see them, clear YC batch."

### How do places work?

Y Combinator Jobs Scraper reads YC's location text: an office ("San Francisco, CA, US"), a country ("US", "IN") or a remote place ("Remote (US; CA)", remote in the US or Canada). A country finds the jobs in it and the jobs remote in it; a region (Europe, APAC, LatAm, EMEA) finds the jobs in its countries; Worldwide finds jobs open anywhere. Older YC jobs name only a city ("New York City", "SF"): their own page gives the country, and the actor opens it when a place filter needs it. SF, NYC and the Bay Area find the names YC writes.

### How do I get only jobs that sponsor a visa, or above a salary?

Pick will-sponsor in Visa terms (`visa`) for jobs whose company sponsors a US visa, or not-required for jobs that need no US citizenship or visa, such as jobs outside the US. Type a yearly amount in US dollars in Minimum pay, USD (`minSalaryUsd`): 150000 keeps the jobs whose pay range reaches $150K; hourly and monthly pay count as a year's, and jobs paid in another currency are left out.

### How do I search one YC batch?

Type the batch in YC batch (`batch`): W25 for Winter 2025, S24 for Summer 2024, F26 for Fall 2026, P25 (or X25) for Spring 2025, or a year such as 2025 for all its batches. Every row also carries its company's batch in `batch`.

### Does it need a login or an API key?

Y Combinator Jobs Scraper needs no YC account and no API key: it reads the same public pages any visitor's browser reads. You need only an Apify account. Applying to a job takes a YC account, through the job's `applyUrl`.

### Does it work on Apify's free plan?

Y Combinator Jobs Scraper works on Apify's free plan, which pays $0.000019 a job plus the $0.015 run start at the default 1 GB. The free $5 monthly credit pays for about 29,000 jobs in runs of 100, at $0.017 a run.

### How often should I run it?

Running Y Combinator Jobs Scraper once a day keeps a job feed fresh: set Posted in the last (`postedWithin`) to 24 hours and Number of jobs (`maxJobs`) to 0 to get every YC job of the day for your titles and places. On 2026-11-10, each weekday of the two weeks before still had 20 to 60 open jobs posted that day. Set it up under Schedules in Apify Console, and match rows on `jobId` to skip jobs you already have.

### How do I get every job of one company?

Type the company's name in Only these companies (`companies`), such as Airbnb or Retool, or paste its ycombinator.com link, set Posted in the last (`postedWithin`) to any time and Number of jobs (`maxJobs`) to 0. Y Combinator Jobs Scraper finds the company in YC's directory and reads only its jobs.

### How do I check a list of job links?

Paste ycombinator.com job links (ycombinator.com/companies/.../jobs/...) or Work at a Startup job links (workatastartup.com/jobs/123456) into Job links to check (`jobUrls`), one per line, instead of searching. An open job comes back with all its fields; a job the company no longer lists comes back closed; a link whose company or job YC does not know comes back not found. Work at a Startup answers a closed job and an unknown number the same way, so its links come back open or not found.

### How do I call it from the API, Python, JavaScript, n8n or an AI agent?

Y Combinator Jobs Scraper runs from the Apify API, Python, JavaScript, n8n, Make or an AI agent over MCP. Each way uses your Apify token (Apify Console, Settings, API & Integrations) and takes the input as JSON keyed by the field names, such as `searchTerms` and `maxJobs`.

**API.** One call runs the actor and returns its rows (Apify waits up to 300 seconds; for runs of thousands of jobs, use a client below):

```bash
curl -X POST "https://api.apify.com/v2/acts/anshumanatrey~ycombinator-jobs-search/run-sync-get-dataset-items" \
  -H "Authorization: Bearer <YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"searchTerms": ["software engineer"], "location": ["San Francisco"]}'
```

**Python** (`pip install apify-client`):

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("anshumanatrey/ycombinator-jobs-search").call(run_input={"searchTerms": ["software engineer"]})
for row in client.dataset(run.default_dataset_id).iterate_items():  # apify-client 3+; on 2.x use run["defaultDatasetId"]
    print(row["title"], row["company"], row["batch"], row["location"], row["salary"], row["postedAt"], row["jobUrl"])
```

**JavaScript** (`npm install apify-client`):

```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: '<YOUR_APIFY_TOKEN>' });
const run = await client.actor('anshumanatrey/ycombinator-jobs-search').call({ searchTerms: ['software engineer'] });
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) console.log(row.title, row.company, row.batch, row.location, row.salary, row.postedAt, row.jobUrl);
```

**n8n and Make.** In n8n, add the Apify node, pick Run an Actor and get dataset, choose this actor and paste the input JSON: the rows come out as n8n items. In Make, the Apify app's Run an Actor and Get Dataset Items modules do the same.

**AI agents (MCP).** Add `https://mcp.apify.com?tools=anshumanatrey/ycombinator-jobs-search` to your MCP client and sign in with Apify, or send `Authorization: Bearer <YOUR_APIFY_TOKEN>`. The agent gets this actor as a tool and sees every input field by its JSON key.

### Am I charged for closed jobs?

Y Combinator Jobs Scraper charges for a closed job only when you paste its link to check. A search returns open jobs only, and a pasted link that turns out closed is one Job row, because it was checked and answered.

### Is it legal to use?

Y Combinator Jobs Scraper reads public job postings, the pages any visitor sees without logging in. It is not affiliated with Y Combinator or Work at a Startup. You are responsible for how you use the data, including YC's terms and the privacy laws that apply to you.

## Limitations

- Every run reads the job list of every YC company that is hiring (1,500 lists) before it opens any job, so even a small search takes about half a minute; naming companies in Only these companies (`companies`) reads only theirs.
- It finds the companies YC's directory marks as hiring: 6,316 jobs of the 6,323 Work at a Startup counted on 2026-11-10.
- YC's job cards date jobs in words ("about 1 month"). A job is opened for its exact date when its words leave it possibly inside your period, so a search with few matches opens the jobs just past the period too, to be sure.
- YC states a minimum experience only ("3+ years"), so `experienceMax` is empty except for internships, and 165 jobs (3%) state none: an Experience (`experienceYears`) filter leaves those out.
- Pay is shown on about 4 of 5 jobs. An amount that cannot be a year's pay (a placeholder such as $1, or $120 typed for $120K) stays in `salary` as YC shows it, with no numbers.
- Minimum pay compares jobs paid in US dollars only; there is no currency conversion.
- A job posted twice by one company with the same title at the same place is delivered once, the newest.
- YC numbers its jobs in posting order, and this actor opens the jobs that can match in that order. Every open job since 2021 follows it; 5 of the 6,189 open on 2026-11-10, posted in 2019 and 2020, are a few days to months out of order, so a search reaching back to 2020 can keep one and leave out the other where Number of jobs (`maxJobs`) cuts.
- Applying to a job takes a YC account; the actor never signs in.

## Who maintains it?

Built and maintained by **Anshuman Atrey** ([@AnshumanAtrey](https://github.com/AnshumanAtrey)), who publishes a portfolio of data and OSINT actors on Apify Store. For a feature request or a bug, message [LinkedIn](https://linkedin.com/in/anshumanatrey) (fastest), open an issue on the GitHub repo, or write through [atrey.dev](https://atrey.dev).

## Sibling actors

| Actor | What it searches |
|---|---|
| [Greenhouse Jobs Scraper](https://apify.com/anshumanatrey/greenhouse-jobs-search) | Jobs from every company on Greenhouse, searched live |
| [Lever Jobs Scraper](https://apify.com/anshumanatrey/lever-jobs-search) | Jobs from 2,300+ companies on Lever (jobs.lever.co), searched live |
| [Ashby Jobs Scraper](https://apify.com/anshumanatrey/ashby-jobs-search) | Jobs from every company on Ashby (jobs.ashbyhq.com), searched live |
| [Workday Jobs Scraper](https://apify.com/anshumanatrey/workday-job-search) | Jobs from every company on Workday (myworkdayjobs.com), searched live |
| [SmartRecruiters Jobs Scraper](https://apify.com/anshumanatrey/smartrecruiters-jobs-search) | Jobs from 2,900+ companies on SmartRecruiters, searched live |
| [Workable Jobs Scraper](https://apify.com/anshumanatrey/workable-job-search) | Jobs from every company on Workable, in one search |
| [Deel Jobs Scraper](https://apify.com/anshumanatrey/deel-jobs-search) | Jobs from every company on Deel ATS (jobs.deel.com), with pay |
| [Naukri Jobs Scraper](https://apify.com/anshumanatrey/naukri-jobs-search) | Jobs on naukri.com, India's largest job board, with salary and experience |

For the people behind a company: [LinkedIn Profile Finder](https://apify.com/anshumanatrey/linkedin-harvester) turns an email into a public LinkedIn profile.

## Documentation

- Apify Store: https://apify.com/anshumanatrey/ycombinator-jobs-search
- GitHub repo: https://github.com/AnshumanAtrey/ycombinator-jobs-search (MIT license, see [LICENSE](LICENSE))
- The engine behind it: https://github.com/AnshumanAtrey/ats-jobs-engine

## Last updated

2026-11-10 (version 1.0)
