# PriceScraper Script

***
## Before Scraping Data:
 Check if the site allows scraping according to its /robots.txt file. 

 For information on how to read these files, click [here](https://www.promptcloud.com/blog/how-to-read-and-respect-robots-file/).


## Script Summary:
 This script allows the user to monitor product prices on web pages. It gets the price every three days to check if it's within your ideal price range. If it's at that range, it will send you an email notifying you of this. 
 
 It is easily customizable; you can adjust the timed intervals between its request, price range, email type, as well as various other components to your liking. 

## Note on Gmail Usage:
If you want the script to send the notification into your Gmail, you have to either obtain an App password for two-step authentication and place it into the mailServer.login password parameter or enable 'allow less secure apps' for your account.

## Issues
1. Doesn't work on prices for sites such as Amazon or Target. Return None values.
2. This app has to run in the background to work. This could be remedied if the user has another server to run it on. However, that costs money to maintain it.


## MISCELLANEOUS COMMENTS:
## Possible Improvements:
 1. This application could be made cleaner if ES6 with Node.js was used instead.
 2.TBA

# Potential Ideas 
I wanted to add a feature in the scraper that would rotate the user's proxies and the user-agents so he or she would not get their IP banned accidentally. I had to have both because rotating user-agents without switching IPs could get your address blocked from the site faster than if you hadn't switched done the loop.
The problem was getting a reliable proxy without having to spend money. There is a multitude of free proxy servers on the web but most don't use HTTPS and gives the person monitoring your connection access to your data. 
There are no proxy servers or VPNs on the web that are really 'free' because maintaining them cost money which the server managers either get through selling your data or other shady practices.
