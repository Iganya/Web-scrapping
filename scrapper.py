# Web-scrapping
My webscrapping Journey


import requests
from bs4 import BeautifulSoup as bs

#The url of the site to scrape
URL = "https://realpython.github.io/fake-jobs/"

#Using requests to get the page of the url
page = requests.get(URL)

#Converting to a beautiful Soup Object
soup = bs(page.content, "html.parser")

#Find the specific id to get details from.
results = soup.find(id="ResultsContainer")

#Getting into where the Job available are
job_elements = results.find_all("div", class_="card-content")

def available_Job():
    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        print(title_element.text)
        print(company_element.text)
        print(location_element.text)
        print()
        links = job_element.find_all("a")
        for link in links:
            link_url = link["href"]
            print(f"Apply here: {link_url}\n")
            
available_Job()
