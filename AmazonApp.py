
#allows app to access URL,pull data,send mail, and set timed intervals

import requests
from bs4 import BeautifulSoup
import smtplib
import time

#Doesn't work for some websites. Always check their /robots.txt page beforehand
URL = "page with the product price"

# Allows me to get information from my browser

UA = {User-Agent: "Your User Agent"}

def scrapePrice():
    #query string 'headers' parameter to interact with website
    page = requests.get(URL, headers=UA)
    #pass lxml as parser or the html.parser if you don't want to install it. Doesn't work with bad html.
    soup0 = BeautifulSoup(page.content, 'lxml')
    soup1 = BeautifulSoup(soup0.prettify(), 'lxml')

    #change up id or points of references. Use inspect if using chrome.
    title = soup1.find(id="title").get_text()
    rawPrice = soup1.find(id="price").get_text()
    price = int(rawPrice.split("."))
    
    #change the numbers as needed for your ideal price range
    if price < 123:
       sendMail()

    print(price)
    print(title.strip())

    if price > 123:
       sendMail()


def sendMail():
    #connects to gmail server
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)

    #establishes connection
    mailServer.ehlo()

    #encrypts connection
    mailServer.starttls()
    mailServer.ehlo()
    
    #Actual user and pass if 'allow less secure apps' for gmail. If you did two step authentication, you can generate a password to put in. Other mail types might require the same procedure as gmail.
    mailServer.login('myuser', 'mypass')

    mailSubject = "It's at your ideal price"

    #link to productPage
    mailBody = 'Link to product page'

    # f or format allows me to insert subject. Kinda like JavaScript.
    message = f"Subject: {mailSubject}\n\n{mailBody}"
    
    #parameters are (from,to,content)
    mailServer.sendmail('fromEmail', 'toEmail', message)
    mailServer.quit()

# Checks Every Three Days.
while True:
    scrapePrice()
    time.sleep(60*60*24*3)