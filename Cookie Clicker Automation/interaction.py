# Practiced form filling using selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = "C:\Drivers\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")
fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
login = driver.find_element_by_css_selector(".btn")

fname.send_keys("Hanif")
lname.send_keys("Barbhuiya")
email.send_keys("yourname@example.com")
login.click()
