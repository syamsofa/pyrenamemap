import glob
import cv2
import pandas as pd
import pathlib
import os

path ="D:\PENGOLAHAN PETA ST2023\py\petamentah"

os.chdir(path)
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")
 
# prints all files
# print(dir_list)
def read_qr_code(filename):
    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        return value
    except:
        return

for file in os.listdir():
    value = read_qr_code(file)
    print(value)
    old_name=file
    new_name=value+".jpg"
    os.rename(old_name,new_name)

