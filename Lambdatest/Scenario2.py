from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
serv_obj = Service("C:/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.lambdatest.com/selenium-playground/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Drag & Drop Sliders").click()
time.sleep(2)

elem=driver.find_element(By.XPATH,"//*[@id='slider3']/div/input" )
ActionChains(driver).drag_and_drop_by_offset(elem,120, 0).perform()

slidder=driver.find_element(By.XPATH,"//*[@id='rangeSuccess']").text
assert "95" in slidder