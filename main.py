import cv2
import numpy
import aircv as ac
import os
import sys
import time
from ctypes import *
import win32com
import win32api
import win32com.client
import json
from PIL import ImageGrab
import random
import pyttsx3
import pyautogui

#大图中找小图，并返回各种坐标和相似度
def matchImg(imgsrc,imgobj,num,confidencevalue=0.5):
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
    return ac.find_all_template(imsrc, imobj, threshold = num)

#截屏并保存
def screenshot(bmpname):
    im = ImageGrab.grab()
    im.save('./Screenshot/' + bmpname + '.bmp','bmp')

#输入大图和小图找出小图在大图中的位置和相似度，如果没找到就返回None
def ReturnCoordinates(imgsrc, imgobj, Similarity):
    try:
        return matchImg(imgsrc, imgobj, Similarity)
    except:
        print("没找到")
        return None


screenshot("desktop")
coordinates = ReturnCoordinates("./Screenshot/desktop.bmp", "./Screenshot/qq.bmp", 0.9)
coordinate = coordinates[0]['result']
pyautogui.moveTo(coordinate[0], coordinate[1], 0.6, pyautogui.easeInQuad)
