import requests
from bs4 import BeautifulSoup

URL = 'https://be.linkedin.com/jobs/search?keywords=Software%20Engineer&location=Brussels%2C%20Brussels%20Region%2C%20Belgium&geoId=100432943&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0 '
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find('ul', class_='jobs-search__results-list')
job_elems = content.find_all(class_='result-card__contents')
python_elems = content.find_all('h3', string=lambda text: 'Python' in text)


def jobs():
    for job_elem in job_elems:
        title_elem = job_elem.find('h3')
        employer_elem = job_elem.find(class_='result-card__subtitle')
        location_elem = job_elem.find(class_='job-result-card__location')

        if None in (title_elem, location_elem, employer_elem):
            continue
        print(title_elem.text.strip())
        print(employer_elem.text.strip())
        print(location_elem.text.strip())
        print()


def pythonjobs():
    for title_elem in python_elems:
        job_elem = title_elem.parent
        employer_elem = job_elem.find(class_='result-card__subtitle')
        location_elem = job_elem.find(class_='job-result-card__location')

        if None in (title_elem, location_elem, employer_elem):
            continue
        print(title_elem.text.strip())
        print(employer_elem.text.strip())
        print(location_elem.text.strip())
        print()


#jobs()
pythonjobs()


print(f'{len(job_elems)} jobs found')
print(f'{len(python_elems)} python jobs found')
