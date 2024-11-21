import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# initializing a browser
driver = webdriver.Chrome()

# launch the url

driver.get ("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# expand the browser
driver.maximize_window()

time.sleep(3)

enter_username = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
enter_username.send_keys("Admin")

enter_password = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
enter_password.send_keys("admin123")

# click login button
login_button = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
login_button.click()

time.sleep(5)

# click on admin side nav
admin_nav = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span")
admin_nav.click()

time.sleep(10)
#
# # search for system user
#
# system_user = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input")
# system_user.send_keys("Admin")
#
# # select the user role
# user_role_dropdown = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]")
# user_role_dropdown.click()
#
# time.sleep(20)

click_user_management = driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.oxd-topbar-body-nav-tab.--parent.--visited > span")
click_user_management.click()

click_users = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a")
click_users.click()

time.sleep(3)


click_job = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span")
click_job.click()


job_title = driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.--active.oxd-topbar-body-nav-tab.--parent > span")
job_title.click()

organisation = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span")
organisation.click()

time.sleep(3)


general_information = driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.--active.oxd-topbar-body-nav-tab.--parent > ul > li:nth-child(1) > a")
general_information.click()

time.sleep(5)


qualification = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span")
qualification.click()

time.sleep(3)

skills = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]/a")
skills.click()

time.sleep(3)

# click on PIM
pim = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]")
pim.click()

time.sleep(4)

click_configuration = driver.find_element (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]")
click_configuration.click()


click_leave = driver.find_element (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]")
click_leave.click()

time.sleep(5)

#click entitlements
click_entitlement = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span")
click_entitlement.click()

#click add entitlements
click_add_entitlement = driver.find_element (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]/a")
click_add_entitlement.click()

time.sleep(4)


click_reports = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span")
click_reports.click()


click_configure = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[5]/span")
click_configure.click()

time.sleep(3)

# click on Time side nav

click_time = driver.find_element (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span")
click_time.click()

time.sleep(3)


click_timesheet = driver.find_element (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span")
click_timesheet.click()

#click on attendance

click_attendance = driver.find_element (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span")
click_attendance.click()


click_report = driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(3) > span")
click_report.click()

time.sleep(4)

click_project_reports = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]/a")
click_project_reports.click()

time.sleep(10)

# click on project info
click_project_info = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span/i")
click_project_info.click()

time.sleep(4)


click_customers = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]/a")
click_customers.click()

time.sleep(3)

#click on the recruitment side nav
click_recruitment = driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(5) > a > span")
click_recruitment.click()

time.sleep(5)

# click on my info side nav
click_myinfo = driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(6) > a > span")
click_myinfo.click()

time.sleep(5)

#click on performance side nav
click_performance = driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(7) > a > span")
click_performance.click()

time.sleep(5)

click_configure = driver.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(1) > span")
click_configure.click()


click_kpi = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]/a")
click_kpi.click()

time.sleep(5)

click_reviews = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span")
click_reviews.click()

click_manage_reviews = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a")
click_manage_reviews.click()

time.sleep(5)

#click on dashboard side nav

click_dashboard = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[8]")
click_dashboard.click()

time.sleep(5)


#click on directory side Nav

click_directory = driver.find_element (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[9]")
click_directory.click()

time.sleep(5)

# click on claim side Nav
click_claim = driver.find_element (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[11]")
click_claim.click()

time.sleep(5)

click_configuration = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span")
click_configuration.click()

click_event = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]/a")
click_event.click()

time.sleep(5)

#click on buzz side Nav

click_buzz = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[12]")
click_buzz.click()