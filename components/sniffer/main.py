from selenium import webdriver  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import numpy as np
import time

class Sniffer():
    def __init__(self):
        super(self).__init__()
 
    def get_new_coins(self):
        self.NEW_URI = 'https://tokensniffer.com/tokens/new'

        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        options.add_argument("--enable-javascript")
        driver = webdriver.Firefox(options=options)
        driver.get(self.NEW_URI)
        
        coins = self.get_coins(driver)

    
    def get_coins(driver):
        coins_list = driver.find_elements_by_class_name('notranslate')

        
 
    def run(self):
        
