from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

serv_obj = Service("C:/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.lambdatest.com/selenium-playground/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Input Form Submit").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='seleniumform']/div[6]/button").click()

driver.find_element(By.XPATH, "//*[@id='seleniumform']/div[6]/button").click()
msg=driver.find_element(By.XPATH, "//input[@id='name']").get_attribute(name="validationMessage")
print(msg)
assert "Please fill out this field." in msg
time.sleep(2)

driver.find_element(By.NAME, "name").send_keys("ABC")
time.sleep(1)
driver.find_element(By.ID, "inputEmail4").send_keys("ABc@example.com")
time.sleep(1)
driver.find_element(By.ID, "inputPassword4").send_keys("SSS")
time.sleep(1)
driver.find_element(By.ID, "company").send_keys("uuu")
time.sleep(1)
driver.find_element(By.ID,"websitename").send_keys("fff")
time.sleep(1)
country=Select(driver.find_element(By.NAME,"country"))
country.select_by_visible_text("India")
time.sleep(1)
driver.find_element(By.ID, "inputCity").send_keys("hhh")
time.sleep(1)
driver.find_element(By.ID,"inputAddress1").send_keys("kkk")
time.sleep(1)
driver.find_element(By.ID,"inputAddress2").send_keys("lll")
time.sleep(1)
driver.find_element(By.ID,"inputState").send_keys("ppp")
time.sleep(1)
driver.find_element(By.ID,"inputZip").send_keys("77777")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='seleniumform']/div[6]/button").click()

message2=driver.find_element(By.XPATH,"//*[@id='__next']/div/section[3]/div/div/div[2]/div").text
assert "Thanks for contacting us, we will get back to you shortly." in message2
