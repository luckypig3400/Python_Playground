from os import cpu_count, listdir, path
from os.path import isfile, join
import pathlib

currentDirName = pathlib.Path()
currentDirPath = pathlib.Path.absolute()
# https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory/3430395

print(currentDirName)

# onlyfiles = [f for f in listdir()]