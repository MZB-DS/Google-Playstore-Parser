from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")
import re
import pandas as pd
import xlrd
from tqdm import tqdm
from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as uReq
import urllib.parse

options = Options()
options.headless = True #This will help to open our browser in the background

input_df = pd.read_excel("input_appstoreurl.xlsx") # Enter the name of your input file. Please refer the sample input file in the repository for the format.

output_df_list = []

for rows_num in tqdm(range(0, input_df.shape[0])):
    app_creator_name = input_df["Company Name"][rows_num]
    app_website_name = input_df["Website"][rows_num]
    url = input_df["PlaystoreURL"][rows_num]

    uClient = uReq(url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    company_url = ""
    for link in page_soup.findAll('a', attrs={'class': 'hrTbp R8zArc'}):
        company_name = str(link).split(">")[1].split("<")[0]
        company_name = company_name.replace("&amp;","&")
        company_name = urllib.parse.quote_plus(company_name)
        company_url = "https://play.google.com/store/apps/developer?id="+company_name
        break

    print("{}:".format(company_url))

    browser = webdriver.Firefox(executable_path = 'geckodriver',options=options)
    try:
        browser.get(company_url)
    except:
        print("Issue with the company url: {}".format(company_url))
        browser.quit()
        continue
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    html_source=browser.page_source

    browser.quit()

    page_soup = BeautifulSoup(html_source, 'html.parser')
    apps_by_developer = []
    for link in page_soup.findAll('a', attrs={'class': 'poRVub'}):
        url_link = str(link.get('href'))
        apps_by_developer.append(str("https://play.google.com" + url_link))

    apps_by_developer = set(apps_by_developer)

    apps_by_developer=list(apps_by_developer)
    apps_by_developer_list = []
    for i in apps_by_developer:
        output_df_list.append([app_creator_name,app_website_name,i])

    print(apps_by_developer)
    print("\n")

    output_df = pd.DataFrame(output_df_list ,columns = ["Company Name","Website","PlayStore Urls"]) # Rename column names for your output file here

    output_df.to_excel("appstoreurl_output.xlsx",index=False) # Enter the name of your desrired output file here
