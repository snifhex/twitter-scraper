import os
import time
from selenium import webdriver


def infinteScroll(driver):
    height = 0
    while height < driver.execute_script("return document.body.scrollHeight"):
        height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    html_source = driver.page_source.encode('utf-8')
    return html_source


def savedHtml(html, query):
    fileName = f"{query}{str(time.process_time_ns())}.html"
    with open(fileName, 'wb') as doc:
        doc.write(html)
    print(f'Saved {fileName}')
    return fileName


def getQuery(query):
    url = f'https://twitter.com/search?q={query}'
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_xpath(
        '//*[@id="timeline"]/div/div[2]/div[1]').click()
    html_source = infinteScroll(driver)
    driver.close()
    return html_source


def get_tweets(fileName):
    with open(fileName, 'rb') as doc:
        source = doc.read()


getQuery('mr robot')
