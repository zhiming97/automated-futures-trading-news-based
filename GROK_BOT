import undetected_chromedriver as uc
from undetected_chromedriver import Chrome
from selenium.webdriver.common.keys import Keys
import re
import time
import random
import json
import requests


#Open MEXC exchange in google chrome
options = uc.ChromeOptions()
options.headless = False

browser = uc.Chrome(options=options, use_subprocess=True)

# Execute JavaScript to open a new tab
browser.execute_script("window.open('about:blank', '_blank');")
firsttab = browser.switch_to.window(browser.window_handles[0])
browser.get("https://futures.mexc.com/exchange/GROK_USDT") # go to the MEXC Exchange

# Switch to the second tab 
secondtab = browser.switch_to.window(browser.window_handles[-1])
browser.get("https://twitter.com/elonmusk") #go to X

# ----------------------------------------------------------------------------
# #Actions on Browser
# browser.close()
# browser.quit()
def scrapetweets():
    while True:
        try:
            # tweets = browser.find_elements('xpath','//div[@data-testid="tweetText"]')
            # tweet = (tweets[0].text).replace('\n', ' ')
            # return tweet
            tweets = browser.find_elements('xpath','//div[@class="css-175oi2r r-eqz5dr r-16y2uox r-1wbh5a2"]')
            tweet = (tweets[1].text).replace('\n', ' ')
            processedtweet = (((tweet.split('·'))[1]).lower())
            return processedtweet
            break
        except Exception as e:
            print(f"Error occured while scraping. Reintiating scaping process in 10 minutes")                      
            time.sleep(600)
            browser.refresh()
            time.sleep(10)

def longnow():
    longbutton = browser.find_element('xpath','//button[@class="ant-btn ant-btn-default pages-contract-handle-component-index-longBtn"]')
    longbutton.click()

def shortnow():
    shortbutton = browser.find_element('xpath','//button[@class="ant-btn ant-btn-default pages-contract-handle-component-index-shortBtn"]')
    shortbutton.click()

def inputquantity():
    quantity = browser.find_elements('xpath','//input[@class="ant-input"][@type="text"]')
    quantity[0].send_keys(1280000) #set the number of quanity that you would like to long/short


#  ----------------------------------------------------------------------------
# Execution part

keywords = [" grok "," @grok ", " grok", " @grok", "grokai"," grokai ","grōk"," grokk "]

x= 0
while x<5000:
    browser.refresh()
    print(f"Refreshing browser..please wait for 7 seconds")
    time.sleep(7)
    elonpost = scrapetweets()
    elonpost

    if elonpost:
        if any(i in elonpost for i in keywords):
            browser.switch_to.window(browser.window_handles[0]) #Go to the exchange
            time.sleep(1)
            inputquantity() # input the quantity
            time.sleep(1)
            longnow() # Click Long action button

            time.sleep(60)
            inputquantity() # input the quantity again
            time.sleep(1)
            shortnow() #Close the Trade
            time.sleep(1)
            break
        else:
            print('Keyword "Grok" not found.Reinitiating whole process flow...Wait for 15-30 seconds before restarting')
            time.sleep(random.uniform(15,30))
            
    x = x+1
    print(x)

