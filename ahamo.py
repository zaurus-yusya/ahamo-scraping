import os
import time
from selenium import webdriver

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

#LINE message api 設定
LINE_CHANNEL_ACCESS_TOKEN = os.environ['ACCESSTOKEN']
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def lambda_handler(event, context):
    start = time.time()

    URL = 'https://ahamo.com/store/pub/application/contract/index.html?useType=0&orderDiv=03&representModelCode=004Bj&modelCode=004Bj'

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--single-process")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--window-size=880x996")
    options.add_argument("--no-sandbox")
    options.add_argument("--homedir=/tmp")
    options.binary_location = "/opt/headless/python/bin/headless-chromium"

    browser = webdriver.Chrome(
        executable_path="/opt/headless/python/bin/chromedriver",
        chrome_options=options
    )

    browser.get(URL)
    
    time.sleep(2)
    
    browser.execute_script("window.scrollTo(0, 500)") 
    
    time.sleep(2)

    browser.find_element_by_xpath("//*[@id=\"B-149\"]/section[1]/div/main/label[6]/div").click()
    
    time.sleep(2)
    
    try:
        element = browser.find_element_by_xpath("//*[@id=\"B-149\"]/section[2]/div/main/label[3]/div[2]/span")
        line_bot_api.broadcast(TextSendMessage(text='ないよ'))
    except:
        line_bot_api.broadcast(TextSendMessage(text='ある！！！！！！！\nhttps://ahamo.com/store/pub/application/contract/index.html?useType=0&orderDiv=03&representModelCode=004Bj&modelCode=004Bj'))
        
    time.sleep(3)
    
    browser.close()

    return