import undetected_chromedriver as uc
from undetected_chromedriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time
import random
import json
import requests
import re
import concurrent.futures


#Open MEXC exchange in google chrome (browser)
options = uc.ChromeOptions()
options.headless = False

#open the browser in a specific size (To allow pyautogui to refresh the page if the tab crashes due to running out of memory)
browser = uc.Chrome(options=options, use_subprocess=True)
browser.set_window_position(400,0)
browser.set_window_size(1300,1050)

# Execute JavaScript to open a new tab
browser.execute_script("window.open('about:blank', '_blank');")
firsttab = browser.switch_to.window(browser.window_handles[0])
browser.get("https://futures.mexc.com/exchange/GROK_USDT")

secondtab = browser.switch_to.window(browser.window_handles[-1])
browser.get("https://twitter.com/elonmusk")
time.sleep(4)

#Open another exchange in a different google chrome (browser1)
options1 = uc.ChromeOptions()
options1.headless = False

browser1 = uc.Chrome(options=options1, use_subprocess=True)
browser1.set_window_position(400,0)
browser1.set_window_size(1100,850)
browser1.get("https://futures.mexc.com/exchange/GROK_USDT")

# ----------------------------------------------------------------------------

#  ----------------------------------------------------------------------------
# Function part (functions for mexc exchange) (browser)

def scrapetweets():
    while True:
        try:
            pinornopiinned = browser.find_elements('xpath','//div[@data-testid="socialContext"]')
            tweets = browser.find_elements('xpath','//div[@class="css-175oi2r r-eqz5dr r-16y2uox r-1wbh5a2"]')
            if pinornopiinned:
                tweet = (tweets[1].text).replace('\n', ' ')
                print('Pinned post present, gonna capture the 2nd post')
            else:
                tweet = (tweets[0].text).replace('\n', ' ')
                print('No pinned post, gonna capture the 1st post')
            processedtweet = (((tweet.split('·'))[1]).lower()) 
            processedtweet
            return processedtweet
            break
        except Exception as e:
            send_alert("Error occured while scraping. Reintiating scaping process in 10 minutes. Keep Calm !")  
            print(f"Error occured while scraping. Reintiating scaping process in 2 minutes.")                      
            time.sleep(10)
            refresh_button_x=490
            refresh_button_y=60
            pyautogui.moveTo(refresh_button_x, refresh_button_y, duration=1)
            time.sleep(1)
            pyautogui.click()
            send_alert("Page refreshed. Should be no problem now")
            time.sleep(7)

def longnow():
    longbutton = browser.find_element('xpath','//button[@class="ant-btn ant-btn-default component_longBtn__BBkFR"]')
    longbutton.click()

def shortnow():
    shortbutton = browser.find_element('xpath','//button[@class="ant-btn ant-btn-default pages-contract-handle-component-index-shortBtn"]')
    shortbutton.click()

def inputquantity():
    quantity = browser.find_elements('xpath','//div[@class="ant-slider-handle"]')
    offset =  310
    actions = ActionChains(browser)
    actions.click_and_hold(quantity[0]).move_by_offset(offset, 0).release().perform()

def settpmanual():
    closebutton = browser.find_elements('xpath','//div[@class="handle_vInner__IXFRx"]//span')
    limitbutton = browser.find_elements('xpath','//div[@class="EntrustTabs_tabs__FLhYk"]//span')
    closebutton[1].click()
    limitbutton[4].click()

def input_tp_priceandsettpprice():

    priceinputbox = browser.find_elements('xpath','//input[@class="ant-input"][@type="text"]')
    closelongbutton = browser.find_elements('xpath','//button[@class="ant-btn ant-btn-default component_shortBtn__s8HK4"]')

    #1st TP Price
    priceinputbox[1].send_keys('Backspace') #clear the price input box
    priceinputbox[1].send_keys(float(getentryprice())*1.04) # input the TP price when price more than entry by 5%
    print(f"TP Price set to {float(getentryprice())*1.04}")
    priceinputbox[2].send_keys(getcurrentposition()/4)
    print(getcurrentposition()/3) # input the quantity to close the long
    closelongbutton[1].click() # press the "Close Long" button
    time.sleep(2)
    
    #2nd TP Price
    priceinputbox[1].send_keys('Backspace') #clear the price input box
    priceinputbox[1].send_keys(float(getentryprice())*1.05) # input the TP price when price more than entry by 6%
    print(f"TP Price 2 set to {float(getentryprice())*1.05}")
    priceinputbox[2].send_keys(getcurrentposition()/4)
    print(getcurrentposition()/3) # input the quantity to close the long
    closelongbutton[1].click() # press the "Close Long" button
    time.sleep(2)

    #3rd TP Price
    priceinputbox[1].send_keys('Backspace') #clear the price input box
    priceinputbox[1].send_keys(float(getentryprice())*1.06) # input the TP price when price more than entry by 6%
    print(f"TP Price 3 set to {float(getentryprice())*1.06}")
    priceinputbox[2].send_keys(getcurrentposition()/4)
    print(getcurrentposition()/3) # input the quantity to close the long
    closelongbutton[1].click() # press the "Close Long" button
    time.sleep(2)

    #4th TP Price
    priceinputbox[1].send_keys('Backspace') #clear the price input box
    priceinputbox[1].send_keys(float(getentryprice())*1.07) # input the TP price when price more than entry by 6%
    print(f"TP Price 4 set to {float(getentryprice())*1.07}")
    priceinputbox[2].send_keys(getcurrentposition()/4)
    print(getcurrentposition()/2) # input the quantity to close the long
    closelongbutton[1].click() # press the "Close Long" button
    time.sleep(2)

def input_tp_priceandsettppricev2():

    priceinputbox = browser.find_elements('xpath','//input[@class="ant-input"][@type="text"]')
    closelongbutton = browser.find_elements('xpath','//button[@class="ant-btn ant-btn-default component_shortBtn__s8HK4"]')

    #1st TP Price
    priceinputbox[1].send_keys('Backspace') #clear the price input box
    priceinputbox[1].send_keys(float(getentryprice())*1.05) # input the TP price when price more than entry by 5%
    print(f"TP Price set to {float(getentryprice())*1.05}")
    priceinputbox[2].send_keys(getcurrentposition()/2)
    print(getcurrentposition()/3) # input the quantity to close the long
    closelongbutton[1].click() # press the "Close Long" button
    time.sleep(2)

    #2nd TP Price
    priceinputbox[1].send_keys('Backspace') #clear the price input box
    priceinputbox[1].send_keys(float(getentryprice())*1.06) # input the TP price when price more than entry by 6%
    print(f"TP Price set to {float(getentryprice())*1.06}")
    priceinputbox[2].send_keys(getcurrentposition()/2)
    print(getcurrentposition()/3) # input the quantity to close the long
    closelongbutton[1].click() # press the "Close Long" button
    time.sleep(2)

def setstoploss():
    entry_price = float(getentryprice())
    stoplossprice = entry_price*1.007
    add_stop_loss_btn = browser.find_element('xpath', '//div[@class="TpslRecordAndBtn_addBtn__l43BX"]')

    # Actions
    add_stop_loss_btn.click() #Click add stop loss button
    time.sleep(2)
    #Input price and take action
    stop_loss_price_box = browser.find_elements('xpath', '//span[@class="ant-input-affix-wrapper"]')
    input_stop_loss_price = browser.find_elements('xpath', '//span//input[@class="ant-input"][@type="text"]')
    confirmbtn = browser.find_elements('xpath', '//button[@type="button"][@class="ant-btn ant-btn-primary ant-btn-lg"]')
    stop_loss_price_box[1].click() #Click on the stop loss box
    input_stop_loss_price[1].send_keys(stoplossprice) #input the stop loss price
    time.sleep(3)
    confirmbtn[0].click() #Click Confirm
    print(f"Stop loss sucessfully placed at {stoplossprice}. Entry Price is {entry_price}")

def getcurrentposition():
    entry_position = browser.find_elements('xpath', '//td[@class="ant-table-cell"]')
    position = entry_position[1].text.replace(',','')
    position = float(position[:-5])
    return position

def getentryprice():
    entry_price = browser.find_elements('xpath', '//td[@class="ant-table-cell"]')
    entry_price = entry_price[2].text
    return entry_price

def getbest_askprice():
    bestsellprice = browser.find_elements('xpath','//div[@class="pages-contract-market-market-price pages-contract-market-market-sell"]')
    askprice = bestsellprice[5].text #get the current best asking price
    return askprice

def getcurrentfairprice():
    fairprice = browser.find_elements('xpath', '//td[@class="ant-table-cell"]')
    askprice = fairprice[3].text #get the current best asking price
    return askprice

def checkpositionentrytime():
    timeee = re.findall(r'\d',elonpost[:4])
    timing = int(''.join(timeee))
    return timing

def longgrok_mexc():
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(1)
    inputquantity()
    longnow()
    send_alert('LONGED GROK !!')
    time.sleep(1)

    #set TP price 1 and 2
    settpmanual()
    time.sleep(3)
    timing = checkpositionentrytime()
    if timing in range(0,16):
        input_tp_priceandsettppricev2()
        print(f"v2 TP activated")
    else:
        input_tp_priceandsettpprice()
        print(f"v1 TP activated")

# -------------------------------------------------------------------------
# To send messages/alerts to the user via telegram

def send_alert(message):

    apiToken = "Your API Token"
    chatID = 'Your Telegram ChatID'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

# -------------------------------------------------------------------------
# Defining functions for another google chrome browser (browser1)
def longnow1():
    longbutton = browser1.find_element('xpath','//button[@class="ant-btn ant-btn-default component_longBtn__BBkFR"]')
    longbutton.click()

def shortnow1():
    shortbutton = browser1.find_element('xpath','//button[@class="ant-btn ant-btn-default pages-contract-handle-component-index-shortBtn"]')
    shortbutton.click()

def inputquantity1():
    quantity = browser1.find_elements('xpath','//div[@class="ant-slider-handle"]')
    offset =  310
    actions = ActionChains(browser1)
    actions.click_and_hold(quantity[0]).move_by_offset(offset, 0).release().perform()

def settpmanual1():
    closebutton = browser1.find_elements('xpath','//div[@class="handle_vInner__IXFRx"]//span')
    limitbutton = browser1.find_elements('xpath','//div[@class="EntrustTabs_tabs__FLhYk"]//span')
    closebutton[1].click()
    limitbutton[4].click()

def input_tp_priceandsettpprice1():

    priceinputbox = browser1.find_elements('xpath','//input[@class="ant-input"][@type="text"]')
    closelongbutton = browser1.find_elements('xpath','//button[@class="ant-btn ant-btn-default component_shortBtn__s8HK4"]')

    #1st TP Price
    priceinputbox[1].send_keys('Backspace') #clear the price input box
    priceinputbox[1].send_keys(float(getentryprice1())*1.04) # input the TP price when price more than entry by 4%
    print(f"TP Price set to {float(getentryprice1())*1.04}")
    priceinputbox[2].send_keys(getcurrentposition1()/4)
    print(getcurrentposition1()/3) # input the quantity to close the long
    closelongbutton[1].click() # press the "Close Long" button
    time.sleep(2)
    
    #2nd TP Price
    priceinputbox[1].send_keys('Backspace') #clear the price input box
    priceinputbox[1].send_keys(float(getentryprice1())*1.05) # input the TP price when price more than entry by 5%
    print(f"TP Price 2 set to {float(getentryprice1())*1.05}")
    priceinputbox[2].send_keys(getcurrentposition1()/4)
    print(getcurrentposition1()/3) # input the quantity to close the long
    closelongbutton[1].click() # press the "Close Long" button
    time.sleep(2)

    #3rd TP Price
    priceinputbox[1].send_keys('Backspace') #clear the price input box
    priceinputbox[1].send_keys(float(getentryprice1())*1.06) # input the TP price when price more than entry by 6%
    print(f"TP Price 3 set to {float(getentryprice1())*1.06}")
    priceinputbox[2].send_keys(getcurrentposition1()/4)
    print(getcurrentposition1()/3) # input the quantity to close the long
    closelongbutton[1].click() # press the "Close Long" button
    time.sleep(2)

    #4th TP Price
    priceinputbox[1].send_keys('Backspace') #clear the price input box
    priceinputbox[1].send_keys(float(getentryprice1())*1.07) # input the TP price when price more than entry by 7%
    print(f"TP Price 4 set to {float(getentryprice1())*1.07}")
    priceinputbox[2].send_keys(getcurrentposition1()/4)
    print(getcurrentposition1()/2) # input the quantity to close the long
    closelongbutton[1].click() # press the "Close Long" button
    time.sleep(2)

def input_tp_priceandsettppricev21():

    priceinputbox = browser1.find_elements('xpath','//input[@class="ant-input"][@type="text"]')
    closelongbutton = browser1.find_elements('xpath','//button[@class="ant-btn ant-btn-default component_shortBtn__s8HK4"]')

    #1st TP Price
    priceinputbox[1].send_keys('Backspace') #clear the price input box
    priceinputbox[1].send_keys(float(getentryprice1())*1.05) # input the TP price when price more than entry by 5%
    print(f"TP Price set to {float(getentryprice1())*1.05}")
    priceinputbox[2].send_keys(getcurrentposition1()/2)
    print(getcurrentposition1()/3) # input the quantity to close the long
    closelongbutton[1].click() # press the "Close Long" button
    time.sleep(2)

    #2nd TP Price
    priceinputbox[1].send_keys('Backspace') #clear the price input box
    priceinputbox[1].send_keys(float(getentryprice1())*1.06) # input the TP price when price more than entry by 6%
    print(f"TP Price set to {float(getentryprice1())*1.06}")
    priceinputbox[2].send_keys(getcurrentposition1()/2)
    print(getcurrentposition1()/3) # input the quantity to close the long
    closelongbutton[1].click() # press the "Close Long" button
    time.sleep(2)

def setstoploss1():
    entry_price = float(getentryprice1())
    stoplossprice = entry_price*1.007
    add_stop_loss_btn = browser1.find_element('xpath', '//div[@class="TpslRecordAndBtn_addBtn__l43BX"]')

    # Actions
    add_stop_loss_btn.click() #Click add stop loss button
    time.sleep(2)
    #Input price and take action
    stop_loss_price_box = browser1.find_elements('xpath', '//span[@class="ant-input-affix-wrapper"]')
    input_stop_loss_price = browser1.find_elements('xpath', '//span//input[@class="ant-input"][@type="text"]')
    confirmbtn = browser1.find_elements('xpath', '//button[@type="button"][@class="ant-btn ant-btn-primary ant-btn-lg"]')
    stop_loss_price_box[1].click() #Click on the stop loss box
    input_stop_loss_price[1].send_keys(stoplossprice) #input the stop loss price
    time.sleep(3)
    confirmbtn[0].click() #Click Confirm
    print(f"Stop loss sucessfully placed at {stoplossprice}. Entry Price is {entry_price}")


def getcurrentposition1():
    entry_position = browser1.find_elements('xpath', '//td[@class="ant-table-cell"]')
    position = entry_position[1].text.replace(',','')
    position = float(position[:-5])
    return position

def getentryprice1():
    entry_price = browser1.find_elements('xpath', '//td[@class="ant-table-cell"]')
    entry_price = entry_price[2].text
    return entry_price

def getbest_askprice1():
    bestsellprice = browser1.find_elements('xpath','//div[@class="pages-contract-market-market-price pages-contract-market-market-sell"]')
    askprice = bestsellprice[5].text #get the current best asking price
    return askprice

def getcurrentfairprice1():
    fairprice = browser1.find_elements('xpath', '//td[@class="ant-table-cell"]')
    askprice = fairprice[3].text #get the current best asking price
    return askprice

def checkpositionentrytime1():
    timeee = re.findall(r'\d',elonpost[:4])
    timing = int(''.join(timeee))
    return timing

def longgrok_mexcmainacc():
    time.sleep(1)
    inputquantity1()
    longnow1()
    time.sleep(1)

    #set TP price 1 and 2
    settpmanual1()
    time.sleep(3)
    timing = checkpositionentrytime1()
    if timing in range(0,16):
        input_tp_priceandsettppricev21()
        print(f"v2 TP activated")
    else:
        input_tp_priceandsettpprice1()
        print(f"v1 TP activated")


#  ----------------------------------------------------------------------------
# Execution part 

keywords = [" grok "]

x= 0
previouspost = ''
while x<7000: #can be set to unlimited
    browser.refresh()
    print(f"Refreshing browser..please wait for 5 seconds")
    time.sleep(5)
    elonpost = scrapetweets()
    elonpost

    #process the tweet another time to only extract the contents
    start_index = elonpost.find('"') + 1
    end_index = elonpost.rfind('"')
    # Extract the middle portion of the tweet
    processedelonpost = elonpost[start_index:end_index][3:-21]
    processedelonpost

    if (processedelonpost != previouspost):
        send_alert(elonpost)
        previouspost = processedelonpost

    if elonpost:
        if any(i in elonpost for i in keywords) and re.search(r'\d+s', elonpost[:4]) and not re.search(r'\breplying to\b', elonpost[4:]):
            #Open positions in two different browsers at the same time (IMPORTANT!!)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future1 = executor.submit(longgrok_mexcmainacc)
                future2 = executor.submit(longgrok_mexc)
            completed_futures, _ = concurrent.futures.wait([future1, future2])

            while True:
                avg_entryprice = float(getentryprice())
                currentfairprice = float(getcurrentfairprice())
                percentagegainz = ((avg_entryprice - currentfairprice)/avg_entryprice)*100
                time.sleep(1)
                print(f"Percentagegainz is {percentagegainz}%")
            
                if percentagegainz <= -3:
                    print('Placing stop loss at entry now')
                    setstoploss()
                    setstoploss1()
                    print(f"Stop Loss placed at entry")
                    send_alert('Stop Loss placed at entry')
                    time.sleep(360)
                    break 
        else:
            print('Keyword "Grok" not found.Reinitiating whole process flow...Wait for 15-30 seconds before restarting')
            time.sleep(random.uniform(18,21))   
    x = x+1
    print(x)


