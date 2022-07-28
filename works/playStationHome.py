import requests
from selenium.webdriver.common.by import By

class PlayStationHomePage():
    def get_home_page_info(self):
        response = requests.get('https://social.playstation.com/jetstream/quicklinks/zh-hant-tw.json')
        return response.json()

    def go_to_home_page(self, driver):
        driver.get("https://www.playstation.com/zh-hant-tw/")

    def go_to_month_page(self, driver):
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[3]/div/div/div/div/div[1]/section/div/div[2]/div/div/div[2]/div/div/div[1]/a/div').click()

    def get_current_page_link(self, driver):
        return driver.current_url
