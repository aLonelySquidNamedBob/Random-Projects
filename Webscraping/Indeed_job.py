import requests
from bs4 import BeautifulSoup

URL = 'https://www.indeed.com/jobs?q=software+developer&l=New+York%2C+NY'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find(id='resultsBodyContent')
job_elems = content.find_all('div', class_="result")
python_elems = content.find_all(string=lambda text: 'python' in text.lower())

jobs = {}

for i, job_elem in enumerate(job_elems):
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find(class_='company')
    location_elem = job_elem.find('span', class_='location')
    date_elem = job_elem.find('span', class_='date')
    if None in (title_elem, location_elem, company_elem):
        continue
    title = title_elem.text.strip()
    location = location_elem.text.strip()
    date = date_elem.text.strip()
    jobs[f'title {i}'] = title
    jobs[f'location {i}'] = location
    jobs[f'date {i}'] = date

for i in range(len(job_elems)):
    print(jobs[f'title {i}'])
    print(jobs[f'location {i}'])
    print(jobs[f'date {i}'])
    print()

print(f'{len(jobs)//3} jobs found')
