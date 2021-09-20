from selenium import webdriver
from time import sleep
from threading import Thread

driver = webdriver.Chrome('C:/Python/Udemy 100 Days of Code/chromedriver')
driver.get('https://orteil.dashnet.org/cookieclicker/')

cookie = driver.find_element_by_id('bigCookie')
count = driver.find_element_by_id('cookies')
products = driver.find_elements_by_css_selector('#products')
for product in products:
    item = product.get_attribute('id')
    print(item)

# def click():
#     while True:
#         cookie.click()
#
# t = Thread(target=click)
# t.daemon = True
#
# def purchase():
#     sleep(5)
#     for iditem.click()
#
# t1 = Thread(target=purchase)
# t1.daemon=True
#
# t.start()
# t1.start()
#
# sleep(60)
# print(count.text)

driver.quit()