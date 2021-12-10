from selenium import webdriver  
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get('https://data.gov.in/resources/current-daily-price-various-commodities-various-markets-mandi')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="csv-86943"]/a').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="edit-download-reasons"]/div[2]/label').click()
driver.find_element_by_xpath('//*[@id="edit-reasons-d"]/div[1]/label').click()
driver.find_element_by_xpath('//*[@id="edit-submit"]').click()
time.sleep(5)