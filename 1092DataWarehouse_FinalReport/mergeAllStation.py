import os
from os import listdir
from os.path import isfile, join
import codecs

currentDirPath = os.path.abspath(os.curdir)
print(currentDirPath)

os.chdir("..")
# https://stackoverflow.com/questions/17885516/moving-up-one-directory-in-python/41652554
parentDirPath = os.path.abspath(os.curdir)
os.chdir(currentDirPath)

currentDirName = currentDirPath.replace(parentDirPath + "\\", "")
# https://www.w3schools.com/python/ref_string_replace.asp
print(currentDirName)

onlyfiles = [f for f in listdir(currentDirPath)
             if isfile(join(currentDirPath, f))]
# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory


mergedFileName = currentDirPath + "\\" + currentDirName + "Merged.csv"
mergedFile = codecs.open(mergedFileName, "a+", "utf-8")
# https://stackoverflow.com/questions/934160/write-to-utf-8-file-in-python

mergedFile.write(u"\"測站名稱\",\"觀測日期\",\"觀測時間(hour)\",\"測站氣壓(hPa)\",\"海平面氣壓(hPa)\",\"氣溫(℃)\",\"露點溫度(℃)\",\"相對溼度(%)\",\"風速(m/s)\",\"風向(360degree)\",\"最大陣風(m/s)\",\"最大陣風風向(360degree)\",\"降水量(mm)\",\"降水時數(hr)\",\"日照時數(hr)\",\"全天空日射量(MJ/㎡)\",\"能見度(km)\",\"紫外線指數\",\"總雲量(0~10)\"\n")
mergedFile.write(u"\"StnName\",\"ObsDate\",\"ObsTime\",\"StnPres\",\"SeaPres\",\"Temperature\",\"Td dew point\",\"RH\",\"WS\",\"WD\",\"WSGust\",\"WDGust\",\"Precp\",\"PrecpHour\",\"SunShine\",\"GloblRad\",\"Visb\",\"UVI\",\"Cloud Amount\"")

for fileName in onlyfiles:
    print(fileName)

    if fileName == (currentDirName + "Merged.csv") or fileName == "mergeCSV.py":
        print("Not Weather Data")
    else:
        unmergeFile = codecs.open(fileName, "r", "utf-8")

        dateList = fileName.split("-")
        date = fileName.replace(".csv", "")
        date = date.replace((dateList[0] + "-"), "")

        unmergeFile.readline()
        unmergeFile.readline()
        # 前兩列為標題 直接儀器不使用

        mergedFile.write("\n")  # 在寫入每個檔案前換行
        line = unmergeFile.readline()
        while len(line) != 0:  # https://www.coder4.com/archives/3101
            mergedFile.write("\"" + currentDirName + "\",\"")
            mergedFile.write(date + "\",")
            mergedFile.write(line)
            line = unmergeFile.readline()

        unmergeFile.close()

mergedFile.close()
