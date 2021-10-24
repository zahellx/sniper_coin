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
        print("asd")
 
    def get_new_coins(self):
        self.NEW_URI = 'https://tokensniffer.com/tokens/new'

        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        options.add_argument("--enable-javascript")
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(self.NEW_URI)

        
        coins = self.get_coins()

    
    def get_coins(self):
        coins_contracts = {}
        for row_i in range(1, 5):
            coin_row = self.driver.find_element(By.XPATH, f'//*[@id="__next"]/div/main/div[2]/div[3]/table/tbody/tr[{row_i}]')
            coin_name = self.driver.find_element(By.XPATH, f'//*[@id="__next"]/div/main/div[2]/div[3]/table/tbody/tr[{row_i}]/th').text
            coin_symbol = self.driver.find_element(By.XPATH, f'//*[@id="__next"]/div/main/div[2]/div[3]/table/tbody/tr[{row_i}]/td[1]').text
            coin_contract = self.driver.find_element(By.XPATH, f'//*[@id="__next"]/div/main/div[2]/div[3]/table/tbody/tr[{row_i}]/td[2]').text
            coin_added = self.driver.find_element(By.XPATH, f'//*[@id="__next"]/div/main/div[2]/div[3]/table/tbody/tr[{row_i}]/td[3]').text
            coins_contracts[coin_contract] = coin_name
        self.get_fiability(coins_contracts)

    def get_fiability(self, contracts):

        for contract in contracts.keys():
            url = f"https://tokensniffer.com/token/{contract}"
            print(url)
            self.driver.get(url)
            fiability = self.driver.find_elements_by_class_name("Home_container__1EcsU")
            print(fiability.text)

 
    def run(self):
        self.get_new_coins()

sniffer = Sniffer()
sniffer.run()
    
