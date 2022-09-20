from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.lambdatest.com/selenium-playground/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()
current_url = driver.current_url
print(current_url)
assert "https://www.lambdatest.com/selenium-playground/simple-form-demo" in current_url

var1 = "Welcome to LambdaTest"
driver.find_element(By.ID, "user-message").send_keys(var1)
time.sleep(2)
driver.find_element(By.ID, "showInput").click()
message=driver.find_element(By.ID, "message").text
assert "Welcome to LambdaTest" in message
