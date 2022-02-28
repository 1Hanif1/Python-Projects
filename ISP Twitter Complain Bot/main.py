from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class InternetSpeedTwitterBot:
    def __init__(self, down, up) -> None:
        self.driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")
        self.down = down
        self.up = up

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver\
            .find_element_by_xpath(
                xpath='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
            )\
            .click()

        sleep(60)

        down_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        )
        up_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span'
        )

        if int(down_speed) < self.down or int(up_speed) < self.up:
            return True
        return False

    def tweet_at_provider(self):
        # log in
        self.driver.get("https://twitter.com/i/flow/login")
        uname = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        # send tweet
        # close
        pass


bot = InternetSpeedTwitterBot(50, 10)
if bot.get_internet_speed():
    pass
