from selenium import webdriver
import time

driver= webdriver.Chrome('C:\\[Git_Repos]\\Python_Playground\\chromeDriver-win32\\chromedriver.exe')

url = 'https://e-service.cwb.gov.tw/HistoryDataQuery/index.jsp'

driver.get(url)
time.sleep(3)

citySelectBox = driver.find_element_by_id('stationCounty')
cityOptions = [x for x in citySelectBox.find_elements_by_tag_name("option")]
# https://stackoverflow.com/questions/18515692/listing-select-option-values-with-selenium-and-python/18516161

for element in cityOptions:
    cityName = element.get_attribute("value")
    
    # https://stackoverflow.com/questions/50136361/find-element-by-value-selenium-python
    driver.find_element_by_xpath("//select[@id='stationCounty']/option[@value='" + cityName + "']").click()
    # https://stackoverflow.com/questions/7867537/how-to-select-a-drop-down-menu-value-with-selenium-using-python

    time.sleep(0.3)

stationSelectBox = driver.find_element_by_id('station')


time.sleep(3)
driver.close()