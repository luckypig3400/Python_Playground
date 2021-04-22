from selenium import webdriver

browser = webdriver.Chrome("C:\\[Git_Repos]\\Python_Playground\\1092DataWarehouse_WebCrawler_Tutorial\\Week8\\chromedriver.exe")
browser.get('https://aaa.24ht.com.tw')                # 網頁下載至瀏覽器
print('瀏覽器名稱 = ', browser.name)             # 列印瀏覽器名稱
print('網頁url    = ', browser.current_url)      # 列印網頁url
print('網頁連線id = ', browser.session_id)       # 網頁連線id
print('瀏覽器功能 = \n',browser.capabilities)    # 瀏覽器功能設定訊息

