from googlesearch import search
import re
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def scrape_linkedins(source_id, limit=5):
    linkedin_results = set()
    appends = [' CEO', ' Founder']

    for append in appends:
        pattern = re.compile(r"(?:https?:)?\/\/(?:[\w]+\.)?linkedin\.com\/in\/(?P<permalink>[\w\-\_À-ÿ%]+)\/?")
        for j in search(source_id + append, tld="co.in", num=limit, stop=limit, pause=2):
            if pattern.search(j):
                linkedin_results.add(j)
    return linkedin_results




class Operator:
    def __init__(self, source_id, linkedin_url, first_name=None, last_name=None, role=None, email=None, phone=None, location=None):
        self._source_id = source_id
        self._first_name = first_name
        self._last_name = last_name
        self._role = role
        self._linkedin_url = linkedin_url
        self._email = email
        self._phone = phone
        self._location = location


def operator_search(source_id):
    linkedin_profiles = scrape_linkedins(source_id)
    for profile in linkedin_profiles:
        try:
            print(profile)
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()
            driver.implicitly_wait(2)
            driver.get(profile)

            driver.implicitly_wait(2)
            page_source = driver.page_source

            soup = BeautifulSoup(page_source, 'lxml')
            print(soup)

            name_xpath = '//h1[@class="top-card-layout__title"]'
            name = driver.find_element_by_xpath(name_xpath)
            print(name.text)


            driver.close()

        except:
            pass


#operator_search('praxisschool school management praxipower')
