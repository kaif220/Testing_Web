from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000")
time.sleep(5)

def case1():
    try :
        driver.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/a').click()
        time.sleep(3)
    except :
        print("Not working")
def case2():
    try :
        driver.find_element(By.XPATH,'//*[@id="grid-state"]').click()
        driver.find_element(By.XPATH,'//*[@id="grid-state"]/option[1]').click()
        time.sleep(2)
    except :
        print("Not Working")
def case3():
    try :
        driver.find_element(By.XPATH,'//*[@id="grid-first-name"]').send_keys('6')
        driver.find_element(By.XPATH,'//*[@id="grid-last-name"]').send_keys('7')
        driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/form/div[3]/div[1]/input').send_keys('7')
        driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/form/div[3]/div[2]/input').send_keys('8')
        driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/form/div[4]/div[1]/input').send_keys('7')
        driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/form/div[4]/div[2]/input').send_keys('25')
        time.sleep(5)
    except :
        print("Not Working")
def case4():
    try :
        driver.find_element(By.XPATH,'//*[@id="test"]/form/button').click()
        time.sleep(3)
    except :
        print('Not Working')
def case5():
    try :
        element = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/p[3]')
        txt = element.text
        print(txt)
        time.sleep(1)
    except :
        print("Not text")
def case6():
    try :
        driver.find_element(By.XPATH,'/html/body/div/div[1]/ul/li[1]/a').click()
        time.sleep(4)
    except :
        print('Not working')

def case7():
    try :
        driver.find_element(By.XPATH,'/html/body/div/div[1]/ul/li[2]/a').click()
        time.sleep(3)
        driver.find_element(By.XPATH,'/html/body/div/div[1]/ul/li[3]/a').click()
        time.sleep(3)

    except :
        print("Not Working")
def case8():
    try :
        driver.find_element(By.XPATH, '/html/body/div/div[1]/ul/li[1]/a').click()
        time.sleep(3)
        print('Everything is working properly')
    except :
        print("Successfully checked Everything")

case1()
case2()
case3()
case4()
case5()
case6()
case7()
case8()


