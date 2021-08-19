import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# options.add_argument('C:\\Users\\dell\\AppData\\Local\\Google\\Chrome\\User Data\\class_automation')
# options.add_argument("--user-data-dir=chrome-data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://blackboard.snu.edu.in/')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="agree_button"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login-block"]/div/center/a/img').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="userNameInput"]').send_keys("YOUR EMAIL ID HERE")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="nextButton"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="passwordInput"]').send_keys("YOUR PASSWORD HERE")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="submitButton"]').click()
time.sleep(2)

# after login
driver.find_element_by_xpath('//*[@id="base_tools"]/bb-base-navigation-button[3]/div/li/a/ng-switch/div/span').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="course-link-_8000_1"]/h4').click() # AI course
time.sleep(4)
driver.find_element_by_xpath('//*[@id="sessions-list-dropdown"]/span').click() # join session dropdown
time.sleep(1)
driver.find_element_by_xpath('//*[@id="sessions-list"]/li/a/span').click()
time.sleep(35)

driver.find_element_by_xpath('//*[@id="techcheck-modal"]/button').click()
time.sleep(1)


# # message = ""
# for i in range(29):
#     message = message + "."
#     driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
#     driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
#     time.sleep(1)
#
