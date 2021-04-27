from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
import pandas as pd
import lxml
import re
import json





class Capterra_Source:
    def __init__(self, capterra_name, capterra_type=None, capterra_url=None, capterra_description=None, capterra_countries=None,
                 capterra_employees=None, capterra_reviews=None, capterra_review_rating=None,
                 capterra_pricing_options=None, capterra_users=None, capterra_logo_filepath=None):
        self._capterra_name = capterra_name
        self._capterra_type = capterra_type
        self._capterra_url = capterra_url
        self._capterra_description = capterra_description
        self._capterra_countries = capterra_countries
        self._capterra_employees = capterra_employees
        self._capterra_reviews = capterra_reviews
        self._capterra_review_rating = capterra_review_rating
        self._capterra_pricing_options = capterra_pricing_options
        self._capterra_users = capterra_users
        self._capterra_logo_filepath = capterra_logo_filepath

    def get_name(self):
        return self._capterra_name

    def get_url(self):
        return self._capterra_url

    def get_type(self):
        return self._capterra_type

    def get_description(self):
        return self._capterra_description

    def get_countries(self):
        return self._capterra_countries

    def get_employees(self):
        return self._capterra_employees

    def get_reviews(self):
        return self._capterra_reviews

    def get_rating(self):
        return self._capterra_review_rating

    def get_pricing_options(self):
        return self._capterra_pricing_options

    def get_users(self):
        return self._capterra_users

    def get_logo_filepath(self):
        return self._capterra_logo_filepath


def crawl_capterra(url):

    sources = []
    URL = url

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    driver.get(URL)
    driver.implicitly_wait(10)

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'lxml')
    for elem in soup('script', text=re.compile('SSR_BRIDGE_DATA')):
        string = elem.decode_contents()
        capterra_string = (string.split(' = ', 1)[1])
        capterra_dict = json.loads(capterra_string)

        for item in capterra_dict['pageData']['categoryData']['products']:
            capterra_name = item['product_name']
            capterra_type = url.split('/')[3]
            capterra_url = item['product_url']
            capterra_description = item['long_desc']
            capterra_countries = item['countries']
            capterra_employees = item['filter_options']['employees']
            capterra_reviews = item['total_reviews']
            capterra_review_rating = item['rating']
            capterra_pricing_options = item['filter_options']['pricing_options']
            capterra_users = item['filter_options']['users']
            capterra_logo_filepath = item['logo_filepath']

            capterra_source = Capterra_Source(capterra_name, capterra_type, capterra_url, capterra_description, capterra_countries,
                                              capterra_employees, capterra_reviews, capterra_review_rating,
                                              capterra_pricing_options, capterra_users, capterra_logo_filepath)
            print(capterra_type)
            sources.append(capterra_source)

    driver.close()

    return sources

def find_capterra_categories():
    category_urls = []
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    driver.get('https://www.capterra.com/')
    driver.implicitly_wait(10)

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'lxml')
    mylists = soup.find_all("ul", {"class": "nb-bg-white"})
    for item in mylists:
        category_urls.append(item.find('a').attrs['href'])

    return category_urls

