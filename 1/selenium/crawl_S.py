from selenium import webdriver
from bs4 import BeautifulSoup
import time

class getName():
    def __init__(self):
        self.driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
        self.url = 'http://45.79.43.178/source_carts/wordpress/wp-admin'
        self.username = 'admin'
        self.password = '123456aA'

    def login(self):
        try:
            driver = self.driver
            driver.get(self.url)
            driver.find_element_by_id('user_login').send_keys(self.username)
            time.sleep(1)
            driver.find_element_by_id('user_pass').send_keys(self.password)
            time.sleep(1)
            driver.find_element_by_name('wp-submit').click()
            time.sleep(2)
            return driver
        except NameError as err:
            print(err)
            exit()

    def getdata(self):
        source = getName.login(self).page_source
        soup = BeautifulSoup(source, 'html.parser')
        UserName = soup.find('span', class_='display-name')
        print(UserName.text.strip())


UserName = getName()
UserName.getdata()
