from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
URL = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=106300413&keywords=python%20developer&location=Maharashtra%2C%20India&sortBy=R"
EMAIL = "YOUR LINKEDIN EMAIL"
PASS = "YOUR LINKEDIN PASSWORD"
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get(URL)
driver.maximize_window()
sleep(3)
sign_in = driver.find_element_by_css_selector("a.nav__button-secondary")
sign_in.click()
sleep(3)
uname = driver.find_element_by_id("username")
pword = driver.find_element_by_id("password")
uname.send_keys(EMAIL)
pword.send_keys(PASS)
pword.send_keys(Keys.ENTER)
sleep(3)
all_jobs = driver.find_elements_by_class_name("job-card-container")
for job in all_jobs:
    job.click()
    sleep(1)
    save_btn = driver.find_element_by_class_name("jobs-save-button")
    save_btn.click()
    sleep(1)
