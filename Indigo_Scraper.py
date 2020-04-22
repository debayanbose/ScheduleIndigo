# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:23:08 2020

@author: debayan.bose
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd

def get_driver():

    options = Options()
    options.set_preference("browser.download.folderList",2)
    options.set_preference("browser.download.dir", 'C:/D backup/')
    options.set_preference("browser.download.manager.showWhenStarting", False)

    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    driver = webdriver.Firefox(options=options,executable_path=r'C:/D Backup/geckodriver.exe')
    return driver
def indigo_schedule():
    url = 'https://www.goindigo.in/information/flight-schedule.html'
    driver=get_driver()
    driver.get(url) 
    element = driver.find_element_by_xpath("//a[@class='btn btn-secondary block dropdown-toggle exportScheduleBtn']")
    element.click()
    venue2  = driver.find_element_by_xpath("//a[@class='dropdown-item excel-btn']")
    venue2.click()
    dfs = pd.ExcelFile('C:\\Users\\debayan.bose\\Downloads\\26-DEC-2019-Download-complete-schedule-alldata.xlsx')
    df = dfs.parse('Sheet1',skiprows=3, na_values=['NA'])
    return df

if __name__ == '__main__':
    mydata = indigo_schedule()