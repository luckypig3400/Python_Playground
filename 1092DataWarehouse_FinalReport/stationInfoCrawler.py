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
            print(currentStation + eachStation.text)

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

            print("經度:" + longitude.text)
            # https://stackoverflow.com/questions/48139676/how-to-get-the-value-of-an-element-in-python-selenium/48139708
            print("緯度:" + latitude.text)
            print("海拔高度:" + altitude.text)
            print("設站日期" + stationBeginTime.text)
            print("地址:" + address.text)
            print("備註:" + note.text)

    time.sleep(0.6)

print("已成功擷取指定範圍的站點資訊")
time.sleep(0.6)
driver.close()
