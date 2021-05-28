import datetime
import time
from selenium import webdriver

# https://chromedriver.chromium.org/getting-started

options = webdriver.ChromeOptions()
prefs = {'download.default_directory': 'C:\\WeatherData'}
options.add_experimental_option('prefs', prefs)
# https://stackoverflow.com/questions/35331854/downloading-a-file-at-a-specified-location-through-python-and-selenium-using-chr
driver = webdriver.Chrome('C:\\[Git_Repos]\\Python_Playground\\chromeDriver-win32\\chromedriver.exe',
                          options=options)

startDate = datetime.datetime(2020, 1, 1)
# https://www.w3schools.com/python/python_datetime.asp

for i in range(365):
    # print(startDate)
    startDate += datetime.timedelta(days=1)
    # https://stackoverflow.com/questions/3240458/how-to-increment-a-datetime-by-one-day
    dateString = str(startDate.date())
    print('Current crawling:' + dateString)

    url = 'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466920&stname=%25E8%2587%25BA%25E5%258C%2597&datepicker=' + dateString
    driver.get(url)

    csvFile = driver.find_element_by_id('downloadCSV')
    csvFile.click()
    time.sleep(1)

driver.close()
