# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 00:37:58 2018

@author: LY
"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup,SoupStrainer
import re
import pandas as pd
import time

def scrapeNYT(URL,n): # n represents the number of articles on the URL website

    driver = webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(30)
    driver.get(URL)

    ```
    # Find 'showMoreButton' on the page
    showMoreButton = driver.find_element_by_xpath('//*[@id="latest-panel"]/div[1]/div/div/button')
    # Click the 'showMoreButton'
    showMoreButton.click()
    ```

    # Scroll a page with infinite loading
    # Reference:
    # https://stackoverflow.com/questions/20986631/
    # how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
    # thanks to @Cuong Tran

    SCROLL_PAUSE_TIME = 10

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Soup the entire page
    soup = BeautifulSoup(driver.page_source,'lxml')

    # Get headlines
    headlines = soup.find_all(name = 'h2',attrs={'class':'headline'})
    headline = [headline.get_text().strip("\n ") for headline in headlines][:n]
    print(len(headline))
    print(headline[0])
    print(headline[n-1])

    # Get summaries
    summaries = soup.find_all(name = 'p',attrs={'class':'summary'})
    summary = [summary.get_text()for summary in summaries][:n]
    print(len(summary))
    print(summary[0])
    print(summary[n-1])

    # Get dates
    dates = soup.find_all(name = 'time', attrs ={'class': 'dateline'})
    datePattern = re.compile(r'"([^"]*)"')
    dateTag = [re.findall(datePattern, str(date)) for date in dates]
    date = [date[1][:10] for date in dateTag][:n]
    print(len(date))
    print(date[0])
    print(date[n-1])

    # Create a data frame
    df = pd.DataFrame({'Date': date, 'Headline':headline, 'Summary':summary})

    # End the Selenium browser session
    driver.quit()

    return df

def writeOut(df, fileName):
    with open(fileName,'w',encoding='utf-8-sig') as f:
        df.to_csv(f, sep='\t', index = False)

def main():

    URL = 'https://www.nytimes.com/topic/company/microsoft-corporation'
    n = 6308   # number of news, obtained from the webpage by clicking "latest"
    df2 = scrapeNYT(URL2, n2)
    writeOut(df2,'microsoft-corporation.txt')


if __name__ == "__main__":
    main()
