
from Adafruit_IO import Client
import time
import os
from PIL import Image
import pytesseract
import cv2
import numpy as np
from gtts import gTTS

#adafruit io key
aio = Client('9dacde0601a4***************')

#source path of input image(also we can modify for camera taking instant images)
src_path="/home/pi/Downloads/"



def get_string(img_path):

    #read image with opencv
    img=cv2.imread(img_path)

    # convert image to gray
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #apply dilation and erosion to remove some noise
    kernel=np.ones((1,1),np.uint8)
    img=cv2.dilate(img,kernel, iterations=1)
    img=cv2.erode(img,kernel, iterations=1)
    cv2.imwrite(src_path + "removed_noise.png", img)

    #apply threshold to obtain only black and white
    img=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    #thresh1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY)
    cv2.imwrite(src_path + "thresh.png",img)

    #ocr-ing
    result=pytesseract.image_to_string(Image.open(src_path + "thresh.png"))
    return result


while True:

   # receiving feed ocr in "data"
   data = aio.receive('ocr')

   #removing extra data from feed and coverting "value" to int
   temp=int(data.value)
   if temp:

      print temp

      #calling get_string function for test2.png
      text1 = get_string(src_path + "test2.png")
      print text1

      #text to speech
      tts=gTTS(text=text1, lang='en')
      tts.save('hello.mp3')
      os.system('mpg321 hello.mp3')

      time.sleep(30)
