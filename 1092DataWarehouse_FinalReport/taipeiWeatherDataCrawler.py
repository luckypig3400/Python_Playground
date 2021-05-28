import datetime
import time
from selenium import webdriver

# https://chromedriver.chromium.org/getting-started

taipeiStations = [
    ['466910_鞍部', 'viewMain&station=466910&stname=%25E9%259E%258D%25E9%2583%25A8']
    , ['466920_臺北', 'viewMain&station=466920&stname=%25E8%2587%25BA%25E5%258C%2597']
    , ['466930_竹子湖', 'viewMain&station=466930&stname=%25E7%25AB%25B9%25E5%25AD%2590%25E6%25B9%2596']
    , ['C0A980_社子', 'viewMain&station=C0A980&stname=%25E7%25A4%25BE%25E5%25AD%2590']
    , ['C0A9E0_士林', 'viewMain&station=C0A9E0&stname=%25E5%25A3%25AB%25E6%259E%2597']
    , ['C0A9F0_內湖', 'viewMain&station=C0A9F0&stname=%25E5%2585%25A7%25E6%25B9%2596']
    , ['C0AC40_大屯山', 'viewMain&station=C0AC40&stname=%25E5%25A4%25A7%25E5%25B1%25AF%25E5%25B1%25B1']
    , ['C0AC70_信義', 'viewMain&station=C0AC70&stname=%25E4%25BF%25A1%25E7%25BE%25A9']
    , ['C0AC80_文山', 'viewMain&station=C0AC80&stname=%25E6%2596%2587%25E5%25B1%25B1']
    , ['C0AH40_平等', 'viewMain&station=C0AH40&stname=%25E5%25B9%25B3%25E7%25AD%2589']
    , ['C0AH70_松山', 'viewMain&station=C0AH70&stname=%25E6%259D%25BE%25E5%25B1%25B1']
    , ['C0AI40_石牌', 'viewMain&station=C0AI40&stname=%25E7%259F%25B3%25E7%2589%258C']
    , ['C0A9C0_天母', 'viewMain&station=C0A9C0&stname=%25E5%25A4%25A9%25E6%25AF%258D']
    , ['C1AC50_關渡', 'viewMain&station=C1AC50&stname=%25E9%2597%259C%25E6%25B8%25A1']
]

for i in range(len(taipeiStations)):
    stationName = taipeiStations[i][0]
    queryParameters = taipeiStations[i][1]

    print(stationName + '的資料抓取參數為:' + queryParameters)

    downloadSavePath = 'C:\\WeatherData\\Taipei\\' + stationName  # 針對不同站點儲存在不同資料夾
    options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': downloadSavePath}
    options.add_experimental_option('prefs', prefs)
    # https://stackoverflow.com/questions/35331854/downloading-a-file-at-a-specified-location-through-python-and-selenium-using-chr
    driver = webdriver.Chrome('C:\\[Git_Repos]\\Python_Playground\\chromeDriver-win32\\chromedriver.exe',
                              options=options)

    startDate = datetime.datetime(2020, 1, 1)  # 設定要抓取資料的日期起點
    # https://www.w3schools.com/python/python_datetime.asp
    totalDaysYouWannaFetch = 365  # 設定要抓取的份數

    # 以下開始抓取該站點1年份的資料,可更改365為其他天數(抓取自訂的天數)
    for fetchCount in range(totalDaysYouWannaFetch):
        dateString = str(startDate.date())
        # print('Current crawling:' + dateString)

        url = 'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=' + queryParameters + '&datepicker=' + dateString
        driver.get(url)

        csvFile = driver.find_element_by_id('downloadCSV')
        csvFile.click()
        time.sleep(0.3)

        startDate += datetime.timedelta(days=1)
        # https://stackoverflow.com/questions/3240458/how-to-increment-a-datetime-by-one-day

    driver.close()
    print("已成功抓取站點:" + stationName + "指定份數的每日資料")

print("成功抓取全部台北市氣象測站自設定的日期以來往後"+totalDaysYouWannaFetch+"份的資料")
