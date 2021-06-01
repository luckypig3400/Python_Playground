import os

currentDirPath = os.path.abspath(os.curdir)
print(currentDirPath)

os.chdir("..")
# https://stackoverflow.com/questions/17885516/moving-up-one-directory-in-python/41652554
parentDirPath = os.path.abspath(os.curdir)
os.chdir(currentDirPath)

currentDirName = currentDirPath - parentDirPath
print(currentDirName)

# onlyfiles = [f for f in listdir()]