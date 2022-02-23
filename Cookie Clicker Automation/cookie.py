from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = "C:\Drivers\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element_by_id("bigCookie")


def get_upgrades():
    try:
        store = driver.find_element_by_css_selector(".crate.upgrade.enabled")
        store.click()
    except:
        pass
    upgradables = driver.find_elements_by_css_selector(
        ".product.unlocked.enabled"
    )
    if len(upgradables) == 0:
        return
    upgradables.sort(reverse=True, key=lambda el: int(
        el.find_element_by_class_name("price").text.replace(",", "")))
    upgradables[0].click()


while True:
    cookie.click()
    get_upgrades()
