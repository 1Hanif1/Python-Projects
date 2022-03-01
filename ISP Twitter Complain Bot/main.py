from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class InternetSpeedTwitterBot:
    def __init__(self, down, up, uname, pword) -> None:
        self.driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")
        self.down = down
        self.up = up
        self.uname = uname
        self.pword = pword

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

        if int(down_speed.text.split(".")[0]) < self.down or int(up_speed.text.split(".")[0]) < self.up:
            self.down_speed = down_speed.text
            self.up_speed = up_speed.text
            return True
        return False

    def tweet_at_provider(self):
        # log in
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(5)
        uname = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        uname.send_keys(self.uname)
        uname.send_keys(Keys.ENTER)

        sleep(5)

        pword = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        pword.send_keys(self.pword)
        pword.send_keys(Keys.ENTER)

        sleep(5)

        tweet = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')

        tweet.click()

        tweet.send_keys(
            f"Hey Internet service provider. My speed is less than what was promised. Expected DownSpeed: 50mbps and UpSpeed: 50mbps\n Actual DownSpeed:{self.down_speed}mbps and UpSpeed:{self.up_speed}mbps")

        sleep(5)

        tweet_btn = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')

        tweet_btn.click()

        # send tweet
        # close
        pass


bot = InternetSpeedTwitterBot(
    50, 10, "YOUR TWITTER USERNAME", "YOUR TWITTER PASSWORD")
if bot.get_internet_speed():
    bot.tweet_at_provider()
