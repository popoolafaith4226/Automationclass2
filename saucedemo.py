import time

from selenium import webdriver
from selenium.webdriver.common.by import By


#initializing the browser
driver = webdriver.Chrome()

#launching the url
driver.get("https://www.saucedemo.com/v1/")

#expanding the browser
driver.maximize_window()

enter_username = driver.find_element(By.ID, "user-name")
enter_username.send_keys("standard_user")


enter_password = driver.find_element(By.ID, "password")
enter_password.send_keys("secret_sauce")

click_login_button = driver.find_element(By.ID, "login-button")
click_login_button.click()

time.sleep(5)

#Add items to cart
add_to_cart = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button")
add_to_cart.click()

#Add second item to cart
add_to_cart = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[3]/button")
add_to_cart.click()

#Add third item to cart
add_to_cart = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[3]/button")
add_to_cart.click()

#add fourth item to card
add_to_cart = driver.find_element(By.XPATH,"//*[@id='inventory_container']/div/div[4]/div[3]/button")
add_to_cart.click()

#add fifth item to cart
add_to_cart = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[5]/div[3]/button")
add_to_cart.click()

#add sixth item to cart
add_to_cart = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[6]/div[3]/button")
add_to_cart.click()


#click on the shopping cart
shopping_cart = driver.find_element(By.ID, "shopping_cart_container")
shopping_cart.click()

time.sleep(5)

#click the checkout button
checkout_button = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[2]/a[2]")
checkout_button.click()


#checkout Information

first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("Faith")

last_phone = driver.find_element(By.ID, "last-name")
last_phone.send_keys("Popoola")

postal_code = driver.find_element(By.ID, "postal-code")
postal_code.send_keys("100004")

continue_button = driver.find_element(By.XPATH, "//*[@id='checkout_info_container']/div/form/div[2]/input")
continue_button.click()

finish_button = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[8]/a[2]")
finish_button.click()

time.sleep(3)






