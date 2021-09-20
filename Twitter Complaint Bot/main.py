from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_URL = 'https://twitter.com/?logout=1624085788294'
TWITTER_EMAIL = '****************'
TWITTER_USERNAME = '**********'
TWITTER_PW = '*****************4'

CHROME_DRIVER_PATH = 'C:/Python/Udemy 100 Days of Code/chromedriver'

SPEEDTEST_URL = 'https://www.speedtest.net/'

class InternetSpeedTwitterBot():

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.up = 0
        self.down = 0


    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        #Click the GO button to start the speed test
        time.sleep(3)
        go_button = self.driver.find_element_by_css_selector('.start-button a')
        go_button.click()
        #Wait 60 seconds until test completes, then retrieve the download and upload speeds
        time.sleep(60)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text


    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        #Click the Login Button
        time.sleep(3)
        login_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
        login_button.click()
        #Enter Credentials and Sign in
        time.sleep(3)
        email = self.driver.find_element_by_name('session[username_or_email]')
        email.send_keys(TWITTER_USERNAME)
        pw = self.driver.find_element_by_name('session[password]')
        pw.send_keys(TWITTER_PW)
        submit = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
        submit.click()
        #Tweet
        time.sleep(3)
        text_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        text_box.send_keys(f'Hey Optimum, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up? ')
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        tweet_button.click()
        time.sleep(15)



bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()

bot.driver.quit()
