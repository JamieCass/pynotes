# importing necessary classes
# from different modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

driver_loc = ChromeDriverManager().install()
browser = webdriver.Chrome(driver_loc)
chrome_options = webdriver.ChromeOptions()

prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)


# open facebook.com using get() method
browser.get('https://www.facebook.com/')

# user_name or e-mail id
username = "littlelegend13@homtail.co.uk"

# getting passowrd from text file
# with open('test.txt', 'r') as myfile:
    # password = myfile.read().replace('\n', '')
password = input()

print("Let's Begin")

element = browser.find_elements_by_xpath('//*[@id ="email"]')
element[0].send_keys(username)

print("Username Entered")

element = browser.find_element_by_xpath('//*[@id ="pass"]')
element.send_keys(password)

print("Password Entered")

# logging in
log_in = browser.find_elements_by_id("u_0_b")
log_in[0].click()

print("Login Successful")

browser.get('https://www.facebook.com/events/birthdays/')

feed = 'Happy Birthday!'

element = browser.find_elements_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div/div')

cnt = 0

for el in element:
    cnt += 1
    element_id = str(el.get_attribute('id'))
    XPATH = '//*[@id ="' + element_id + '"]'
    post_field = browser.find_element_by_xpath(XPATH)
    post_field.send_keys(feed)
    post_field.send_keys(Keys.RETURN)
    print("Birthday Wish posted for friend" + str(cnt))

# Close the browser
browser.close()
