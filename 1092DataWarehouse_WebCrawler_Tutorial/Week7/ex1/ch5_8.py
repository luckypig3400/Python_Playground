# ch5_8.py
import bs4
import requests

htmlFile = requests.get('https://ithelp.ithome.com.tw/articles/10186119')
# print(htmlFile.text)
objSoup = bs4.BeautifulSoup(htmlFile.text, 'lxml')
objTag = objSoup.select('#fb-root') # element id
print("資料型態     = ", type(objTag))          # 列印資料型態
print("串列長度     = ", len(objTag))           # 列印串列長度
print("元素資料型態 = ", type(objTag[0]))       # 列印元素資料型態
print("元素內容     = ", objTag[0].getText())   # 列印元素內容
