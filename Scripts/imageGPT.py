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

try:
    super_key = sys.argv[1]
except:
    super_key = None

if super_key:
    print(f"Generating images for key: {super_key}")
else:
    print("Generating images for all keys")



text_dict = {}
with open('responseDict.json', 'r') as f:
    text_dict = json.load(f)

promptLine1 = "You are an image generator based in Pakistan and are tasked with creating a single comic book art image for the following paragraph:"
promptLine2 = "Some guidlines for generation are to make sure that the image is relevant in the context of Pakistan and also in the context of the paragraph. Do not add any country flag except pakistans in the image. DO NOT add any text, characters or words in generated image. Use matte, earthy and pastel color tones. Please generate a 16 by 9 aspect ratio image keeping the provided guidelines in mind."

# main fodler
OUTPUT_DIR = "images"
os.makedirs(OUTPUT_DIR, exist_ok=True)


#faceless undetected chrome
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
op.add_experimental_option("excludeSwitches", ["enable-logging"])
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




#XPATHs
TextBox = "//div[contains(@id,'prompt-textarea')]"
SendPrompt = "//button[contains(@aria-label,'Send promp')]"
WaitCheck = "//button[contains(@data-testid,'stop-button')]"    #updated
NewChat = "//div[contains(@class,'flex h-14 items-center')]//span[contains(@class,'flex')][2]//button[contains(@class,'bg-token-sidebar-surface-secondary')]"
NewChat2 = "//div[@class='flex items-center']//span[contains(@class,'flex')][2]//button[contains(@class,'bg-token')]"   #when side bar is closed use this instead
# ImageElement = "//img[contains(@src,'oaiusercontent')]"
ImageElement = "//article[contains(@data-testid, 'conversation-turn')]/descendant::img[contains(@src, 'oaiusercontent')][1]"

MenuButton = "(//button[contains(@aria-haspopup,'menu')])[1]"
OpenSidebar = "//button[contains(@aria-label,'Open sidebar')]"
CloseSidebar = "//button[contains(@aria-label,'Close sidebar')]"
RenameButton = "(//div[contains(@role,'menuitem')])[2]"
InputBox = "//input[contains(@type,'text')]"


driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, waitTime)
print("Driver started")

#open website 
driver.get('https://chatgpt.com/')
sleep(5)

imageDict = {}
try:
    with open('imageDict.json', 'r') as fp:
        imageDict = json.load(fp)
except:
    print("No previous responses found\nrunning code for the first time")



def save_image_from_url(image_url, save_path):
    response = requests.get(image_url)
    with open(save_path, 'wb') as f:
        f.write(response.content)


def image_generator(key):
    smartExitBool = False

    folder_path = os.path.join(OUTPUT_DIR, key)
    os.makedirs(folder_path, exist_ok=True)

    paragraphs = text_dict[key]['first'].split('\n\n')
    imageIndex = 0

    renameBool = False

    for index, paragraph in enumerate(paragraphs):
        if str(key)+"_"+str(index) in imageDict:
            print(f"Image already present for key: {key} and index: {index}")
            continue
        imageIndex += 1

        textbox = wait.until(EC.element_to_be_clickable((By.XPATH, TextBox)))
        textbox.clear()

        textbox.send_keys(promptLine1)
        textbox.send_keys(Keys.SHIFT, Keys.RETURN)

        for line in paragraph.split('\n'):
            textbox.send_keys(line.strip())
            textbox.send_keys(Keys.SHIFT, Keys.RETURN)

        textbox.send_keys(promptLine2)
        textbox.send_keys(Keys.RETURN)
        sleep(0.5)


        genBool = False

        for i in range(5):
            try:
                wait.until(EC.invisibility_of_element_located((By.XPATH, WaitCheck)))
                sleep(1)
                genBool = True
                break
            except:
                print("Retrying wait")

        if not genBool:
            print("Failed to generate image for key:"+key+" and para: "+str(index))
            sys.exit(0)


        try:
            updateImageElement = "("+ImageElement+")["+str(imageIndex)+"]"
            imageElement = wait.until(EC.presence_of_element_located((By.XPATH, updateImageElement)))

            image_url = imageElement.get_attribute('src')
            image_name = f"para_{index}.webp"
            save_path = os.path.join(folder_path, image_name)

            save_image_from_url(image_url, save_path)
            imageDict[str(key)+"_"+str(index)] = image_url
            smartExitBool = False

        except:
            # if smartExitBool:
            #     print("Smart exit activated")
            #     driver.quit()
            #     sys.exit(0)

            smartExitBool = True
            imageDict[str(key)+"_"+str(index)] = "Failed to generate image"
            imageIndex -= 1
            continue



        with open('imageDict.json', 'w', encoding='utf-8') as fp:
            json.dump(imageDict, fp, ensure_ascii=False, indent=4)
            

        print("Image saved for key:"+key+" and para: "+str(index))
        renameBool = True

        sleep(90)        

    #renaiming logic
    if renameBool:
        openSidebar = wait.until(EC.element_to_be_clickable((By.XPATH, OpenSidebar)))
        openSidebar.click()

        menuButton = wait.until(EC.element_to_be_clickable((By.XPATH, MenuButton)))
        menuButton.click()

        renameButton = wait.until(EC.element_to_be_clickable((By.XPATH, RenameButton)))
        renameButton.click()

        inputBox = wait.until(EC.element_to_be_clickable((By.XPATH, InputBox)))
        inputBox.send_keys(Keys.CONTROL + "a")
        inputBox.send_keys(Keys.DELETE)
        inputBox.send_keys("Image for "+key)
        inputBox.send_keys(Keys.RETURN)

        closeSidebar = wait.until(EC.element_to_be_clickable((By.XPATH, CloseSidebar)))
        closeSidebar.click()



# main code
if super_key:
    image_generator(super_key)

else:

    for key in text_dict:

        image_generator(key)

        newchat = wait.until(EC.element_to_be_clickable((By.XPATH, NewChat2)))
        newchat.click()

        print("")

        
print("All Images are processed")
driver.quit()
