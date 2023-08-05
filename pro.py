import glob
import cv2
import pandas as pd
import pathlib
import os

from PIL import Image
from pyzbar.pyzbar import decode

path ="D:\PENGOLAHAN PETA ST2023\py\petamentah"

os.chdir(path)
dir_list = os.listdir(path)

for file in os.listdir():
    try:        
        data = decode(Image.open(file))
        new_name=data[0].data.decode('UTF-8')+".jpg"
        old_name=file
        os.rename(old_name,new_name)
    except:
        pass
