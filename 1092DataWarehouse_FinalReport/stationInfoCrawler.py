from selenium import webdriver
import time

driver= webdriver.Chrome('C:\\[Git_Repos]\\Python_Playground\\chromeDriver-win32\\chromedriver.exe')

url = 'https://e-service.cwb.gov.tw/HistoryDataQuery/index.jsp'

driver.get(url)
time.sleep(3)

citySelectBox = driver.find_element_by_id('stationCounty')
stationSelectBox = driver.find_element_by_id('station')

time.sleep(3)
driver.close()