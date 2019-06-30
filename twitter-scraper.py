from selenium import webdriver


def getQuery(query):
    url = f'https://twitter.com/search-home?q={query}'
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.find_element_by_xpath(
        '//*[@id="timeline"]/div/div[2]/div[1]').click()
    html_source = driver.page_source.encode('utf-8')
    return html_source


def get_tweets(html_source):
    pass


getQuery('kabir singh')
