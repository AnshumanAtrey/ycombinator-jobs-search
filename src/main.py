"""Y Combinator Jobs Search: the shared job engine (github.com/AnshumanAtrey/ats-jobs-engine) on Y Combinator's Work at a Startup."""
import asyncio

from ats_jobs.engine import main

if __name__ == '__main__':
    asyncio.run(main('ycombinator'))
