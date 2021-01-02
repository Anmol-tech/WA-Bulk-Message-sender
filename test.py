from bs4 import BeautifulSoup
from random import randint
from typing import Text, Type
from PyQt5 import QtCore, QtGui, QtWidgets
import LoadFile
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, NoAlertPresentException
from time import sleep
from urllib.parse import quote
from sys import platform

if __name__ == "__main__":
    option = Options()
    driver = webdriver.Chrome("chromedriver.exe", options=option)
    print("When Sign is success")
    driver.get("https://web.whatsapp.com")
    sleep(5)
    html_source = driver.page_source  
    soup = BeautifulSoup(html_source, 'html.parser')
    divs = soup.find('div', {"class":"_1PTz1"})
    
    print(divs.attrs)