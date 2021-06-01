import os

currentDirPath = os.path.abspath(os.curdir)
print(currentDirPath)

os.chdir("..")
# https://stackoverflow.com/questions/17885516/moving-up-one-directory-in-python/41652554
parentDirPath = os.path.abspath(os.curdir)
os.chdir(currentDirPath)

currentDirName = currentDirPath.replace(parentDirPath + "\\", "")
# https://www.w3schools.com/python/ref_string_replace.asp
print(currentDirName)

# onlyfiles = [f for f in listdir()]
