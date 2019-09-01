import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests


# chromedriver = "C:/chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver
# # driver = webdriver.Chrome(chromedriver)
browser = webdriver.Chrome()
browser.get('http://www.gmail.com')

emailElem = browser.find_element_by_css_selector("#identifierId")
emailElem.send_keys('<SENDERS EMAIL>')
emailElem.submit()
signinBtn = browser.find_element_by_css_selector('#identifierNext')
signinBtn.click()
time.sleep(2)

passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys('<PASSWORD>')
passwordElem.submit()
finalsigninBtn = browser.find_element_by_css_selector('#passwordNext')
finalsigninBtn.click()


time.sleep(10)

composeElem = browser.find_element_by_class_name('z0') #this only works half of the time
composeElem.click()

time.sleep(7)

toElem = browser.find_element_by_name("to")
toElem.send_keys('<RECEIVERS EMAIL')

time.sleep(2)

subjElem = browser.find_element_by_name("subjectbox")
subjElem.send_keys('Test Email with selenium')

time.sleep(2)

bodyElem = browser.find_element_by_css_selector("div[aria-label='Message Body']")
bodyElem.send_keys('A test email with selenium')

time.sleep(2)
#:qi#\:qi
# //*[@id=":qd"]
sendElem = browser.find_element_by_css_selector('#\:qi')
sendElem.click()

# sendElem = browser.find_element_by_xpath("div[aria-label='Send &#8234;(Ctrl-Enter)&#8236‬']")
# sendElem.submit()

#! /usr/bin/env python

# import unittest
# from selenium import webdriver

# class TestGmail(unittest.TestCase):

# 	def setUp(self):
# 		self.driver=webdriver.Chrome( executable_path=r'C:\\chromedriver.exe')

# 	def testLogin(self):
# 		driver = self.driver
# 		driver.get('http://www.gmail.com')
# 		self.assertIn('Gmail', driver.title)
# 		loginBox = driver.find_element_by_css_selector("#identifierId")
# 		loginBox.send_keys('vedantsakhardande@gmail.com')
# 		pwBox = driver.find_element_by_class_name('Xb9hP')
# 		pwBox.send_keys('vedantemailer')
# 		signinBtn = driver.find_element_by_id('signIn')
# 		signinBtn.click()

# 	def tearDown(self):
# 		self.driver.quit()

# if __name__ == '__main__':
# 	unittest.main(verbosity=2)
