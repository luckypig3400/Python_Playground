from logging import currentframe
from selenium import webdriver
import time

driver = webdriver.Chrome(
    'C:\\[Git_Repos]\\Python_Playground\\chromeDriver-win32\\chromedriver.exe')

url = 'https://e-service.cwb.gov.tw/HistoryDataQuery/index.jsp'

driver.get(url)
time.sleep(3)

citySelectBox = driver.find_element_by_id('stationCounty')
cityOptions = [x for x in citySelectBox.find_elements_by_tag_name("option")]
# https://stackoverflow.com/questions/18515692/listing-select-option-values-with-selenium-and-python/18516161

file = open("C:\\WeatherData\\station_info.csv", "a")
# https://www.w3schools.com/python/python_file_write.asp
file.write("縣市,站點名稱,經度,緯度,海拔高度,設站日期,地址,備註\n")
# write columns name for csv file

for element in cityOptions:
    cityName = element.get_attribute("value")

    if cityName == '臺北市' or cityName == '新北市':
        # https://stackoverflow.com/questions/50136361/find-element-by-value-selenium-python
        driver.find_element_by_xpath(
            "//select[@id='stationCounty']/option[@value='" + cityName + "']").click()
        # https://stackoverflow.com/questions/7867537/how-to-select-a-drop-down-menu-value-with-selenium-using-python

        time.sleep(0.6)  # wait for station options loading

        stationSelectBox = driver.find_element_by_id('station')
        stationOptions = [
            x for x in stationSelectBox.find_elements_by_tag_name("option")]
        # 上面兩行找出該縣市所有的測站選項

        for eachStation in stationOptions:
            currentStation = eachStation.get_attribute("value")

            driver.find_element_by_xpath(
                "//select[@id='station']/option[@value='" + currentStation + "']").click()

            time.sleep(0.3)  # wait for station info loading

            longitude = driver.find_element_by_id('Longitude')  # 經度
            latitude = driver.find_element_by_id('Latitude')  # 緯度
            altitude = driver.find_element_by_id('Altitde')  # 海拔高度
            stationBeginTime = driver.find_element_by_id(
                'StnBeginTime')  # 設站日期
            address = driver.find_element_by_id('Address')  # 地址
            note = driver.find_element_by_id('WebRemark')  # 備註

            rowData = (cityName + ',' + eachStation.text + "," + longitude.text + "," + latitude.text +
                       "," + altitude.text + "," + stationBeginTime.text + "," + address.text + "," + note.text)
            # https://stackoverflow.com/questions/48139676/how-to-get-the-value-of-an-element-in-python-selenium/48139708

            file.write(rowData + '\n')

    time.sleep(0.6)

print("已成功擷取指定範圍的站點資訊")
time.sleep(0.6)
driver.close()

file.close()
print("成功寫入檔案")

print("以下為檔案內容:")
file = open("C:\\WeatherData\\station_info.csv", "r")
print(file.read())
