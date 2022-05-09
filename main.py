import requests
import os
import schedule
import time
from bs4 import BeautifulSoup

def storeNews():
    count = 1

    # Create new folder called "news"
    path = os.getcwd()
    if not os.path.exists("news"):
        newFolder = "news"
        os.makedirs(newFolder)
    # Navigate to newly created folder called 'news'
    newPath = path + '\\' + 'news'

    # Fetch rss
    url = "https://www.yahoo.com/news/rss"
    resp = requests.get(url)

    soup = BeautifulSoup(resp.content, features="xml")

    # Increments count if previous newsFile already exists
    while os.path.exists(newPath + '\\' + 'newsFile' + str(count) + '.txt'):
        count = count + 1

    # Create file and store rss contents as .txt file in created folder
    # Files will be named newsFile1.txt, newsFile2.txt, newsFile3.txt, etc.
    newsFile = open(newPath + '\\' + 'newsFile' + str(count) + '.txt', 'w+')
    newsFile.write(soup.prettify())
    newsFile.close()

# Schedule to call url every hour
schedule.every().hour.do(storeNews)

# Program runs indefinitely until manually stopped
while True:
    schedule.run_pending()
    time.sleep(1)