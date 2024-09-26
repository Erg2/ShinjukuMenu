# Cycle through Shinjuku Station menu selections
# Where menu is longer than the screen, scroll down to end of menu
#
# Erg 9/16/2024
#
# Copyright © Shinjuku Station 2024

import time
import sys
import traceback
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


## TODO if we run into memory problems, try clearing the cache
#driver.execute_cdp_cmd('Storage.clearDataForOrigin', {
#    "origin": '*',
#    "storageTypes": 'all',
#})

## Hack transition - try scrolling right till page off screen, go to next page but scrolled way left and then scroll in?

try:

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=chrome_options)

    #driver = webdriver.Chrome()
    driver.get("https://www.shinjukustationvt.com")
    #print("title:", driver.title)
    pageHeight = driver.execute_script("return document.body.scrollHeight")
    pageWidth = driver.execute_script("return document.body.offsetWidth;")

    #print("Scroll pageHeight", pageHeight, " pageWidth", pageWidth)

    #driver.find_element(By.XPATH, '/html/body').send_keys(Keys.F11)
    driver.fullscreen_window()

    menuDiv = driver.find_element(By.XPATH, '//h2[contains(text(), "Menu")]')
    #print("Menu location", menuDiv.location)

    topOffset = menuDiv.location["y"] - 50


    #menuPos = menuDiv.position["height"]

    cls = "menu-select-labels"

    preDelay = 2          # delay before scroll (if any)
    postDelay = 3.5       # delay after scroll (if any) - note: if no scroll, delays for both

    scrollDelay = .01   # delay per vertical pixel

    # Get all the menu labels (== clickable buttons)
    menuList = driver.find_elements(By.CLASS_NAME, cls)

    menuOffset = menuList[0].location["y"]


    while True:

        # click on each menu
        for menu in menuList:
            #print("start menu")

            menu.click()        # select menu
            #print("Scroll to menu")
            scrollCmd = "window.scrollTo(0, "+ str(topOffset) +")"     # Jump to top of page
            driver.execute_script(scrollCmd)
            time.sleep(preDelay)


            menuDiv = driver.find_element(By.CLASS_NAME, "menu-wrapper")
            #print("Menu size", menuDiv.size)
            menuHeight = menuDiv.size["height"]

            winSize = driver.get_window_size()
            winHeight = winSize["height"]
            #print("winSize", winSize)

            currLine = topOffset

            if winHeight < menuHeight + menuOffset:
                #print("winHeight", winHeight, " < (menuHeight", menuHeight, " + menuOffset", menuOffset, ") = ", menuHeight + menuOffset)
                #pageHeight - winSize["height"]
                #print("topOffset", topOffset, " winHeight", winHeight, " menuHeight", menuHeight, " menuOffset", menuOffset)
                #print("Scroll from", topOffset, " to", (menuHeight + menuOffset) - winHeight)
                for ln in range(topOffset, (menuHeight + menuOffset) - winHeight, 1):
                    #scrollCmd = f'window.scrollBy(0,{ln});'
                    #scrollCmd = "window.scrollTo({top:" + str(ln) + ", behavior:'smooth'})"
                    scrollCmd = "window.scrollTo(0, " + str(ln) + ")"
                    driver.execute_script(scrollCmd)
                    time.sleep(scrollDelay)
                currLine = (menuHeight + menuOffset) - winHeight

            #else:
            #    print("winHeight", winHeight, " >= (menuHeight", menuHeight, " + menuOffset", menuOffset, ")")
            #print("Done menu")

            #print("PostDelay")
            time.sleep(postDelay)

            # Sideways doesn't work, dunno why not
            # print("Scroll siceways 1 to ", pageWidth)
            # for xx in range(1, pageWidth):
            #     scrollCmd = "window.scrollTo("+str(xx)+"," + str(currLine) + ")"
            #     print("scrollCmd", scrollCmd)
            #     driver.execute_script(scrollCmd)
            #     time.sleep(.01)

        #print("done")


except:
    print("Well, that didn't work")
    ex = sys.exception()
    traceback.print_exception(ex)

driver.close()
