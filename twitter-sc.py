import csv
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver



options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.get('https://twitter.com/search?q=something&src=typd')
code = driver.page_source.encode('utf-8')



def read_html():
    fileName = 'something.html'
    with open(fileName, 'r') as doc:
        sauce = doc.read()
        sauce.replace('\n', '')
    return sauce


def parse_html(sauce):
    soup = bs(sauce, 'lxml')
    soup.find_all('li', class_='js-stream-item.stream-item stream-item')


def main(resp):
    # resp = requests.get('https://twitter.com/search?q=something&src=typd').content
    soup = bs(resp, 'lxml')
    something = soup.find_all('div', class_='js-tweet-text-container')
    hey = [txt.text for txt in something]
    hey = [td.replace('\n', '') for td in hey]
    # something = soup.div['class']
    for hello in hey:
        print(f'{hello} \n\n')

def toCsv(tweet):
    with open('tweets.csv', 'w') as doc:
        tweetWriter = csv.writer(doc)
        tweetWriter.writerow((tweet,))
        print('Wrote a tweet to csv file.')
    



if __name__ == '__main__':
    main(code)
    driver.close()
