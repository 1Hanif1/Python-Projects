from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class InstagramBot:
    def __init__(self, account, uname, pword, limit) -> None:
        self.driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")
        self.account = account
        self.uname = uname
        self.pword = pword
        self.limit = limit
        self.follow()

    def follow(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(3)

        uname = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input'
        )
        pword = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input'
        )

        uname.send_keys(self.uname)
        pword.send_keys(self.pword)
        pword.send_keys(Keys.ENTER)

        sleep(3)

        btn = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div/div/button'
        )
        btn.click()

        sleep(5)

        btn = self.driver.find_element_by_css_selector(
            'button.aOOlW.HoLwm')
        btn.click()

        sleep(5)

        cover = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div'
        )
        cover.click()
        sleep(3)

        search = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input'
        )
        search.click()
        search.send_keys(self.account)
        sleep(2)
        search.send_keys(Keys.ENTER)
        search.send_keys(Keys.ENTER)
        sleep(5)

        followers = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(3)

        accounts = self.driver.find_elements_by_css_selector(
            "body > div.RnEpo.Yx5HN > div > div > div > div.isgrP > ul > div > li")
        limit = 0
        for acc in accounts:
            acc.find_element_by_css_selector('button[type="button"]').click()
            sleep(2)
            limit += 1
            if limit >= self.limit:
                break


InstagramBot("ACCOUNT TO LOOK UP", "INSTA USERNAME", "INSTA PASSWORD", 10)
