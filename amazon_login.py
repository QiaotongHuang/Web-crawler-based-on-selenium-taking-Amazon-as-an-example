import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from settings import LOGIN_URL, TIMEOUT, EMAIL, PASSWORD

options = Options()
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17")
options.add_argument("--start-maximized")  # Maximize the browser window
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option("prefs", 
                                {"profile.default_content_setting_values.notifications": 2 
                                }) 

driver = webdriver.Chrome(
# WEB_DRIVER_LOCATION, 
    options=options)
driver.get(LOGIN_URL)

# login to Amazon
time.sleep(TIMEOUT)
login = driver.find_element(By.ID, 'ap_email')
login.send_keys(EMAIL)
login.send_keys(Keys.ENTER)

submit = driver.find_element(By.ID, 'ap_password')
submit.send_keys(PASSWORD)
submit.send_keys(Keys.ENTER)

# search Kindle Store in Amazon
search_bar = driver.find_element(By.ID, 'twotabsearchtextbox')
search_bar.send_keys('Kindle Store')
search_bar.send_keys(Keys.ENTER)