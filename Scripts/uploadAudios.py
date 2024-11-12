from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import requests
import sys



print("Starting the driver")

#driver variables
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument(f"--user-data-dir=user_data")
waitTime = 160               #seconds



# XPATHs
UploadButton = "//input[contains(@accept,'.mp')]"
root = '/home/rafay/LUMS/Projects/PMT/Scripts/images'



driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, waitTime)
print("Driver started")

#open website 
driver.get('https://app.fliki.ai/editor/67109af142ead2d7f67f60cc')
sleep(10)



def upload_audio(audio_path):
    try:
        #upload audio
        upload = wait.until(EC.element_to_be_clickable((By.XPATH, UploadButton)))
        upload.send_keys(audio_path)

        print("Audio uploaded")

    except Exception as e:
        print(f"Error in uploading audio: {e}")

    return  
    

for foldername, subfolders, filenames in os.walk(root):
    print(f"Looking in {foldername}")
    for filename in filenames:
        if filename.endswith(".png"):  # Assuming you only want to upload .mp3 files
            file_path = os.path.join(foldername, filename)

            upload_audio(file_path)


print("All audios uploaded")