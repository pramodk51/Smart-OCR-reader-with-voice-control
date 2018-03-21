# smart-OCR-reader-with-voice-control
The following project is a smart OCR reader based on Raspberry Pi.It extracts the texts from images and 
converts them into speech.OpenCV has been used to make the images more favorable for OCR by some image processing.

For OCR, pytesseract has been used as a wrapper for tesseract-OCR.

For text to speech conversion, gTTS library has been used for python environment.

Google Assistant and adafruit IO has been used with a link through IFTTT to provide voice control over starting and
stoping the reading process. 

To make use of the code in other project, make following changes:
1.create an account on IFTTT and on adafruit IO.

2.make a feed in adafruit IO ("ocr" in this code)

3.make recipe on IFTTT to link google assistant and adafruit IO.
(you may assume any if statement like "start ocr" or "start reading" to set the feed to 1.)
(create another recipe with google assistant and adafruit IO with IFTTT to change the feed from 1 to 0 . (" stop reading") )

4.Change the API key with your own API key from adafruit IO.
aio = Client('9dacde0***************')

5.Change the path of the input image in the code as per your requirement.
(src_path="/home/pi/Downloads/")

That should work fine.
