# Web-Scraping-From-New-York-Times

This repository demonstrates two ways of crawling webpages from  New York Times archived news websites. 
Actually New York Times provides a bunch of APIs to respond to request calls, but it turned out that it cannot satisfy the authors' needs. Thus, instead, I used two methods (Selenium and Beautifulsoup, Scrapy and JMesPath) to collect and parse the raw data. 

## Advantages and Disadvantages of Selenium and Scrapy
Note that both Selenium and Scrapy are able to handle infinite scrolling pages. An essential difference is that when using Selenium and BeautifulSoup, crawling and parsing are two separate steps which only executes one after another. In other words, it's not until we reach the end of the infinite scrolling webpage do we start parsing the html file and get the desired information. In this way, the risk of failure in the middle of a crawling task is high (due to unstable internet speed, for example) and we have to start from the very beginning. However, Scrapy and JMESpath are capable of crawling and parsing webpage line by line. Moreover, Scrapy automately gives information when it gets stuck. Thus, we can and we know where exactly to restart. 

##
The target of the author is to collect financial news(broadly speaking), from New York Times by companies. A sample webpage looks like this:




Date, headline and summary are desired and sample data are given in the two .txt file        .

## Welcome for any advice for improvement!
I believe that there're many potential improvement in the provided codes to avoid the problems mentioned above.
I hope my code could at least give a hint to solve some of your problems and any advice is welcomed. Thank you!
