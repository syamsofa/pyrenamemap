import glob
import cv2
import pandas as pd
import pathlib
import os

from PIL import Image
from pyzbar.pyzbar import decode
data = decode(Image.open('img2.jpg'))
print(data[0].data.decode('UTF-8'))

# for file in os.listdir():
#     value = read_qr_code(file)
#     print(value)
#     old_name=file
#     new_name=value+".jpg"
#     os.rename(old_name,new_name)

