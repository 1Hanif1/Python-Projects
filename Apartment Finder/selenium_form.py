from selenium import webdriver
from time import sleep
GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdVMFcmamYGwp9IHmOAMryLsDipNqJK9Mat3bhKiplU8dfONQ/viewform"


class form_fill:

    def fill_form(self, add, pri, lin):
        self.driver = webdriver.Chrome("C:/Drivers/chromedriver.exe")
        self.driver.get(GOOGLE_FORM)
        sleep(5)
        addr = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
        price = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

        addr.send_keys(add)
        price.send_keys(pri)
        link.send_keys(lin)
        sleep(5)

        submit = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        submit.click()

        pass


form_fill()
