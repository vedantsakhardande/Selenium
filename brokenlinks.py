import requests
from selenium import webdriver

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:\\chromedriver.exe')
driver.get('https://google.co.in/')
links = driver.find_elements_by_css_selector("a")
for link in links:
    r = requests.head(link.get_attribute('href'))
    print(link.get_attribute('href'), r.status_code)

# from selenium import webdriver
# chrome_driver_path = "C:\\chromedriver.exe"
# driver=webdriver.Chrome(chrome_driver_path)
# import requests
# for link in links:
#     r = requests.head(link)
#     if r.status_code!=404:
#          driver.get(link)
#     else:
#           print(str(link) + " isn't available.")