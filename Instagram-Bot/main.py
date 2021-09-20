from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import time

CHROME_DRIVER_PATH = 'C:/Python/Udemy 100 Days of Code/chromedriver'
INSTAGRAM_URL = 'https://www.instagram.com/'
SIMILAR_ACCT = 'tech_with_tim'
USERNAME = 'rpy22918593'
PASSWORD = 'ShakeWaitmp4'

class InstaFollower():

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)


    def login(self):
        self.driver.get(INSTAGRAM_URL)
        #Enter Credentials and Login
        time.sleep(3)
        user = self.driver.find_element_by_name('username')
        user.send_keys(USERNAME)
        pw = self.driver.find_element_by_name('password')
        pw.send_keys(PASSWORD)
        submit = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        submit.click()
        time.sleep(3)
        #Instagram will ask to save info--> CLick 'Not Now'
        not_now_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_button.click()
        time.sleep(3)
        #Instagram will ask to turn on notifications--> CLick 'Not Now'
        notifications_button = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notifications_button.click()



    def find_followers(self):
        self.driver.get(f'{INSTAGRAM_URL}{SIMILAR_ACCT}')
        time.sleep(3)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
        followers.click()

        time.sleep(3)
        fbody = self.driver.find_element_by_class_name('isgrP')

        for i in range(10):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fbody)
            time.sleep(2)


    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector('li button')
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                time.sleep(2)
                cancel = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel.click()




insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()

time.sleep(10)
insta.driver.quit()