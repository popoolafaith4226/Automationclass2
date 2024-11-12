import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()
driver.find_element(By.ID, "user-name").send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button").click()

driver.find_element(By.ID, "shopping_cart_container").click()

driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[2]/a[2]").click()

#checkout Information

driver.find_element(By.ID, "first-name").send_keys("Faith")
driver.find_element(By.ID, "last-name").send_keys("Popoola")
driver.find_element(By.ID, "postal-code").send_keys("100004")

driver.find_element(By.XPATH, "//*[@id='checkout_info_container']/div/form/div[2]/input").click()

driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[8]/a[2]").click()

time.sleep(3)






