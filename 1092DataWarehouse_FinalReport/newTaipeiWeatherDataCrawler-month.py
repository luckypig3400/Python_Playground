import datetime
import time
from selenium import webdriver

# https://chromedriver.chromium.org/getting-started

newTaipeiStations = [
    ['466880_板橋', 'viewMain&station=466880&stname=%25E6%259D%25BF%25E6%25A9%258B'],
    ['466900_淡水', 'viewMain&station=466900&stname=%25E6%25B7%25A1%25E6%25B0%25B4'],
    ['C0A520_山佳', 'viewMain&station=C0A520&stname=%25E5%25B1%25B1%25E4%25BD%25B3'],
    ['C0A530_坪林', 'viewMain&station=C0A530&stname=%25E5%259D%25AA%25E6%259E%2597'],
    ['C0A540_四堵', 'viewMain&station=C0A540&stname=%25E5%259B%259B%25E5%25A0%25B5'],
    ['C0A550_泰平', 'viewMain&station=C0A550&stname=%25E6%25B3%25B0%25E5%25B9%25B3'],
    ['C0A560_福山', 'viewMain&station=C0A560&stname=%25E7%25A6%258F%25E5%25B1%25B1'],
    ['C0A570_桶後', 'viewMain&station=C0A570&stname=%25E6%25A1%25B6%25E5%25BE%258C'],
    ['C0A640_石碇', 'viewMain&station=C0A640&stname=%25E7%259F%25B3%25E7%25A2%2587'],
    ['C0A650_火燒寮', 'viewMain&station=C0A650&stname=%25E7%2581%25AB%25E7%2587%2592%25E5%25AF%25AE'],
    ['C0A660_瑞芳', 'viewMain&station=C0A660&stname=%25E7%2591%259E%25E8%258A%25B3'],
    ['C0A860_大坪', 'viewMain&station=C0A860&stname=%25E5%25A4%25A7%25E5%259D%25AA'],
    ['C0A870_五指山', 'viewMain&station=C0A870&stname=%25E4%25BA%2594%25E6%258C%2587%25E5%25B1%25B1'],
    ['C0A880_福隆', 'viewMain&station=C0A880&stname=%25E7%25A6%258F%25E9%259A%2586'],
    ['C0A890_雙溪', 'viewMain&station=C0A890&stname=%25E9%259B%2599%25E6%25BA%25AA'],
    ['C0A920_富貴角', 'viewMain&station=C0A920&stname=%25E5%25AF%258C%25E8%25B2%25B4%25E8%25A7%2592'],
    ['C0A931_三和', 'viewMain&station=C0A931&stname=%25E4%25B8%2589%25E5%2592%258C'],
    ['C0A940_金山', 'viewMain&station=C0A940&stname=%25E9%2587%2591%25E5%25B1%25B1'],
    ['C0A950_鼻頭角', 'viewMain&station=C0A950&stname=%25E9%25BC%25BB%25E9%25A0%25AD%25E8%25A7%2592'],
    ['C0A970_三貂角', 'viewMain&station=C0A970&stname=%25E4%25B8%2589%25E8%25B2%2582%25E8%25A7%2592'],
    ['C0AC60_三峽', 'viewMain&station=C0AC60&stname=%25E4%25B8%2589%25E5%25B3%25BD'],
    ['C0AD30_蘆洲', 'viewMain&station=C0AD30&stname=%25E8%2598%2586%25E6%25B4%25B2'],
    ['C0AD40_土城', 'viewMain&station=C0AD40&stname=%25E5%259C%259F%25E5%259F%258E'],
    ['C0AD50_鶯歌', 'viewMain&station=C0AD50&stname=%25E9%25B6%25AF%25E6%25AD%258C'],
    ['C0AG90_中和', 'viewMain&station=C0AG90&stname=%25E4%25B8%25AD%25E5%2592%258C'],
    ['C0AH00_汐止', 'viewMain&station=C0AH00&stname=%25E6%25B1%2590%25E6%25AD%25A2'],
    ['C0AH10_永和', 'viewMain&station=C0AH10&stname=%25E6%25B0%25B8%25E5%2592%258C'],
    ['C0AH30_五分山', 'viewMain&station=C0AH30&stname=%25E4%25BA%2594%25E5%2588%2586%25E5%25B1%25B1'],
    ['C0AH50_林口', 'viewMain&station=C0AH50&stname=%25E6%259E%2597%25E5%258F%25A3'],
    ['C0AH80_深坑', 'viewMain&station=C0AH80&stname=%25E6%25B7%25B1%25E5%259D%2591'],
    ['C0AH90_福山植物園', 'viewMain&station=C0AH90&stname=%25E7%25A6%258F%25E5%25B1%25B1%25E6%25A4%258D%25E7%2589%25A9%25E5%259C%2592'],
    ['C0AI00_五股', 'viewMain&station=C0AI00&stname=%25E4%25BA%2594%25E8%2582%25A1'],
    ['C0AI10_屈尺', 'viewMain&station=C0AI10&stname=%25E5%25B1%2588%25E5%25B0%25BA'],
    ['C0AI20_白沙灣', 'viewMain&station=C0AI20&stname=%25E7%2599%25BD%25E6%25B2%2599%25E7%2581%25A3'],
    ['C0AI30_三重', 'viewMain&station=C0AI30&stname=%25E4%25B8%2589%25E9%2587%258D'],
    ['C0ACA0_新莊', 'viewMain&station=C0ACA0&stname=%25E6%2596%25B0%25E8%258E%258A'],
    ['C0AD00_三芝', 'viewMain&station=C0AD00&stname=%25E4%25B8%2589%25E8%258A%259D'],
    ['C0AD10_八里', 'viewMain&station=C0AD10&stname=%25E5%2585%25AB%25E9%2587%258C'],
    ['C1A630_下盆', 'viewMain&station=C1A630&stname=%25E4%25B8%258B%25E7%259B%2586'],
    ['C1A9N0_四十份', 'viewMain&station=C1A9N0&stname=%25E5%259B%259B%25E5%258D%2581%25E4%25BB%25BD']
]

for i in range(len(newTaipeiStations)):
    stationName = newTaipeiStations[i][0]
    queryParameters = newTaipeiStations[i][1]

    print(stationName + '的資料抓取參數為:' + queryParameters)

    downloadSavePath = 'C:\\WeatherData\\newTaipei-Month\\' + stationName  # 針對不同站點儲存在不同資料夾
    options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': downloadSavePath}
    options.add_experimental_option('prefs', prefs)
    # https://stackoverflow.com/questions/35331854/downloading-a-file-at-a-specified-location-through-python-and-selenium-using-chr
    driver = webdriver.Chrome('C:\\[Git_Repos]\\Python_Playground\\chromeDriver-win32\\chromedriver.exe',
                              options=options)

    startDate = datetime.datetime(2020, 1, 1)  # 設定要抓取資料的日期起點(月)
    # https://www.w3schools.com/python/python_datetime.asp
    totalDaysYouWannaFetch = 12  # 設定要抓取的份數(月)

    # 以下開始抓取該站點1年份的資料,可更改365為其他天數(抓取自訂的天數)
    for fetchCount in range(totalDaysYouWannaFetch):
        dateString = str(startDate.date())
        dateString = dateString[:-3] # 移除後面三個字元(把日期移掉)
        # https://stackoverflow.com/questions/15478127/remove-final-character-from-string
        print('Current crawling:' + dateString)

        url = 'https://e-service.cwb.gov.tw/HistoryDataQuery/MonthDataController.do?command=' + queryParameters + '&datepicker=' + dateString
        driver.get(url)

        csvFile = driver.find_element_by_id('downloadCSV')
        csvFile.click()
        time.sleep(0.3)

        startDate += datetime.timedelta(days=31) # 一次增加一個月(雖然都用31天不太準確但是很方便)
        # https://stackoverflow.com/questions/3240458/how-to-increment-a-datetime-by-one-day

    driver.close()
    print("已成功抓取站點:" + stationName + "指定份數的每日資料")

print("成功抓取全部新北市氣象測站自設定的日期以來往後" + str(totalDaysYouWannaFetch) + "份的資料")
