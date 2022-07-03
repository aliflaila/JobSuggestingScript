import requests 
from IPython.display import display, HTML
from bs4 import BeautifulSoup #web scraping
import re #Regular Expression pattern matching
import pandas as pd
import sys #for argument parsing
import re
url = "https://remoteok.com/api"
wanted_tags = ["python","data analysis","data engineer","remote"]
r = requests.get(url)
job_results = r.json()
keys = ['date', 'company', 'position', 'tags', 'location', 'url','description']
date_posted = []
company = []
tg = []
loc = []
apply_here = []
description = []
for job in job_results:
    job = {k: v for k, v in job.items() if k in keys}
    if job:
        tags = job.get('tags')
        tags = {tag.lower() for tag in tags}
        if tags.intersection(wanted_tags):
            date_posted.append(job['date'])
            company.append(job['company'])
            tg.append(job['tags'])
            loc.append(job['location'])
            apply_here.append(job['url'])
            job['description']=re.sub('<[^<]+?>', '', job['description'])
            description.append(job['description'])
agg = {'date_posted':date_posted,'company':company,'tags':tg,'location':loc,'apply_here':apply_here}
job_dataframe = pd.DataFrame(agg)
print("Hello Alifia! Good Morning, Check out the below jobs:)")
HTML('''
        <style>
            .job_dataframe tbody tr:nth-child(even) { background-color: orange; }
        </style>
        ''' + job_dataframe.to_html(classes="job_dataframe",render_links=True))
