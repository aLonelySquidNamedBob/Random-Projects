import requests
from bs4 import BeautifulSoup
import time

starttime = time.time()

URL = 'https://www.monster.be/en/jobs/search/?q=Software-Developer&where=Brussels__2C-Brussels'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')


def findjobs():
    job_elems = results.find_all('section', class_='card-content')

    for job_elem in job_elems:
        title_elem = job_elem.find('h2', class_='title')
        company_elem = job_elem.find('div', class_='company')
        location_elem = job_elem.find('div', class_='location')
        time_elem = job_elem.find('time')
        if None in (title_elem, company_elem, location_elem):
            continue
        print(title_elem.text.strip())
        print(company_elem.text.strip())
        print(location_elem.text.strip())
        print(time_elem.text.strip())
        print()


def findpythonjobs():
    python_jobs = results.find_all('h2', string=lambda text: "python" in text.lower())
    print(len(python_jobs))

    for p_job in python_jobs:
        link = p_job.find('a')['href']
        print(p_job.text.strip())
        print(f"Apply here: {link}\n")


findpythonjobs()

endtime = time.time() - starttime
print(endtime)
