import datetime
import time
from selenium import webdriver
# https://chromedriver.chromium.org/getting-started

driver = webdriver.Chrome('C:\\[Git_Repos]\\Python_Playground\\chromeDriver-win32\\chromedriver.exe')

startDate = datetime.datetime(2020, 1, 1)
# https://www.w3schools.com/python/python_datetime.asp

for i in range(365):
    # print(startDate)
    startDate += datetime.timedelta(days=1)
    # https://stackoverflow.com/questions/3240458/how-to-increment-a-datetime-by-one-day

url = 'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466920&stname=%25E8%2587%25BA%25E5%258C%2597&datepicker=2021-05-20#'
driver.get(url)

csvFile = driver.find_element_by_id('downloadCSV')
csvFile.click()
time.sleep(1)

driver.close()
