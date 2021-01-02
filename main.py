from random import randint
from typing import Text, Type
from PyQt5 import QtCore, QtGui, QtWidgets
import xlwt
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


def saveContacts(validNumbers):
    import xlwt
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
    for idx , num in enumerate(validNumbers):
        try:
            teext = str(num)
            sheet.write(idx, 0, teext)
        except AttributeError:
            pass

    wbk.save('WAContact.xls')



if __name__ == "__main__":
    import LoadFile 
    listNumbers = LoadFile.CSVloadNumbers('set_1 _2000.csv')['Mobile Number']

    option  = Options()
    # option.add_argument('headless')
    option.add_argument("--incognito")
    delay = 30
    print(listNumbers[:5])
    input("Press enter to start checking")
    driver = webdriver.Chrome("chromedriver.exe", options=option)

    isValid = []

    sleep(10)
    for idx , num in enumerate(listNumbers):

        
        driver.get("https://whatsapptools.net/check-numbers")
        
        sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/canvas")
        
        import bs4
        html_source = driver.page_source  
        soup = bs4(html_source, 'html.parser')
        divs = soup.find('div', {"class":"_1pw2F"})
        print(divs.attrs["data-ref"])





        driver.find_element_by_xpath("/html/body/div/div/div/div/div/select/option[text()='India +91']").click()
        sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/div/div/input").clear()
        sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/div/div/input").send_keys(num)
        sleep(2)
        
        driver.find_element_by_xpath("/html/body/div/div/button").click()
        
        
        res = str(driver.find_element_by_xpath("/html/body/div/div/p").text)
        sleep(10)
        print(idx,num + " : result : " + res)
        if(res == 'Exists on WhatsApp!'):
            isValid.append(num)
        else:
            continue
        sleep(2)

    saveContacts(isValid)
    driver.close()
    # driver.find_("email").send_keys("abhishek.gupta1608@toppr.in")  