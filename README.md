# Web-Scraping-From-New-York-Times

This repository demonstrates two ways of crawling webpages from  New York Times archived news websites. 
Actually New York Times provides more than [Times APIs](https://developer.nytimes.com/) to respond to request calls, but it turned out that it cannot satisfy my specific needs. Thus, instead, I used two methods -- [Selenium](https://selenium-python.readthedocs.io/) and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [Scrapy](https://scrapy.org/) and [JMESPath](http://jmespath.org/), to collect and parse the raw webpage. 

<img src = "New York Times APIs At A Glance.png" height = "400">
The picture above is from https://developer.nytimes.com/.

## Description of the Scraping Task
The target of the author is to collect financial news(broadly speaking), from New York Times by companies. A sample webpage looks like this:

<img src = "Sample Webpage.jpg" height = "400">

Date, headline and summary are desired and sample data are given in the two txt file [microsoft.txt](../blob/master/microsoft.txt) and [general-motors.txt](../blob/master/general-motors.txt).
After successfully installing the Scrapy package, open a terminal and go to the directory where the created scrapy robot is stored and run $ scrapy crawl gmbot, the spider will start working. Check the official reference document here https://docs.scrapy.org/en/latest/topics/commands.html.

## Comparison of Selenium and Scrapy
Note that both Selenium and Scrapy are able to handle infinite scrolling pages. An essential difference is that when using Selenium and BeautifulSoup, crawling and parsing are two separate steps which only executes one after another. In other words, it's not until we reach the end of the infinite scrolling webpage do we start parsing the html file and get the desired information. In this way, the risk of failure in the middle of a crawling task is high (due to unstable internet speed, for example) and we have to start from the very beginning. However, Scrapy and JMESpath are capable of crawling and parsing webpage line by line. Moreover, Scrapy automately gives information when it gets stuck. Thus, we can and we know where exactly to restart. 


## Welcome for any advice for improvement!
I hope my code could at least give a hint to solve some of your problems.
I believe that there're many potential improvement in the provided codes to avoid the problems mentioned above. 
Any advice is more than welcomed. Thank you!

