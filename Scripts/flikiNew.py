from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json
import os

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

driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 15)
actions = ActionChains(driver)

# helper functions
def getLenghth(givenXpath):
    return len(wait.until(EC.presence_of_all_elements_located((By.XPATH, givenXpath))))



print("Driver started")


# XPATHs
DuplicateFile = "//div[contains(@class,'page_itemWrapper__lQT4J ') and .//*[text() = 'Template']]//button"
DuplicateFile2 = "//div[@role = 'menuitem' and contains(text(), 'uplicate')]"
Scene1 = "(//div[contains(@class,'_compact')])[1]"
RenameFile = "//input[contains(@placeholder, 'Enter name')]"
SelectAudio = "//span[contains(text(),'.mp3')]"
SelectImage = "//button/img"
MyFileButton = "//button[contains(@aria-controls,'content-my')]"
SearchButton = "//input[contains(@placeholder,'Search for your')]"
UploadButton = "//input[contains(@accept,'.mp')]"
SelectAudioTile = "//div[contains(@class,'style_row__REzTM')]//div[contains(@class,'style_item__XWkV2') and contains(@data-state,'')]"
SelectImageTile = "//div[contains(@class,'style_row__REzTM')]//div[contains(@class,'style_item__pgGMm') and contains(@data-state,'')]"
DeleteUpload = "(//button[contains(@class,' style-module_small__wzzMp')])"
DuplicateScene = "//button[.//*/@d[contains(., 'M360-240q-33')]]"
ConfirmButton = "(//div[contains(@class,'AlertDialogActions')]//button[contains(@class,'style-module_button__-niPX')])[1]"


ToDo_List = ['1a110', '1a111' ]
ImgDict = {}

# load dict froom json
with open('mapping.json') as f:
    ImgDict = json.load(f)


for key in ToDo_List:

    driver.get('https://app.fliki.ai/files')

    # variables for this key
    Images_path = "/home/rafay/LUMS/Projects/PMT/Scripts/images/stance_1/"
    Image_List = os.listdir(Images_path)
    Audio_path = "/home/rafay/LUMS/Projects/PMT/Scripts/Audios/"+key+"/"
    Audio_List = os.listdir(Audio_path)
    paraCount = len(Audio_List)

    # dupliacte file
    duplicateFile = wait.until(EC.element_to_be_clickable((By.XPATH, DuplicateFile)))
    duplicateFile.click()
    duplicateFile2 = wait.until(EC.element_to_be_clickable((By.XPATH, DuplicateFile2)))
    duplicateFile2.click()
    
    sleep(5)

    # rename file
    renameFile = wait.until(EC.element_to_be_clickable((By.XPATH, RenameFile)))
    renameFile.clear()
    renameFile.send_keys(key)
    renameFile.send_keys(Keys.RETURN)
    

    # correct the first scene with preset applied
    scene1 = wait.until(EC.element_to_be_clickable((By.XPATH, Scene1)))
    scene1.click()

    print("Working on video: ", key)

    for i in range(paraCount):

        # variables for this paragraph
        audio_path = Audio_path+key+"_"+str(i)+".mp3"
        image_path = Images_path+ImgDict[key+"_"+str(i)]+".png"

        print("Working on para: ", i, "of video: ", key, "with audio: ", audio_path, "and image: ", image_path)
        
        try:
            # replacing the audio
            selectAudio = wait.until(EC.element_to_be_clickable((By.XPATH, SelectAudio)))
            selectAudio.click()

            myFileButton = wait.until(EC.element_to_be_clickable((By.XPATH, MyFileButton)))
            myFileButton.click()

            # search and check if the audio is already uploaded
            sleep(2.5)
            searchButton = wait.until(EC.element_to_be_clickable((By.XPATH, SearchButton)))
            searchButton.clear()
            searchButton.send_keys(key+"_"+str(i))
            searchButton.send_keys(Keys.RETURN)
            sleep(2.5)
            try:
                length = len(WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, SelectAudioTile))))
                if length:

                    selectTile = wait.until(EC.element_to_be_clickable((By.XPATH, SelectAudioTile+"//div[.//*[contains(text(), '"+key+"_"+str(i)+"')]]")))
                    selectTile.click()
            except:
                # print("Uploading audio" + key+"_"+str(i))
                uploadButton = wait.until(EC.element_to_be_clickable((By.XPATH, UploadButton)))
                uploadButton.send_keys(audio_path)

                waitCheck = wait.until(EC.element_to_be_clickable((By.XPATH, UploadButton)))
                length = getLenghth(SelectAudioTile)                     #to select the latest tile
                selectTile = wait.until(EC.element_to_be_clickable((By.XPATH, SelectAudioTile+"//div[.//*[contains(text(), '"+key+"_"+str(i)+"')]]")))
                selectTile.click()


            # DELETING LOGIC
            # selectAudio = wait.until(EC.element_to_be_clickable((By.XPATH, SelectAudio)))
            # selectAudio.click()

            # length = getLenghth(SelectAudioTile)                     #to take cursor to the latest tile
            # selectTile = wait.until(EC.element_to_be_clickable((By.XPATH, "("+SelectAudioTile+")["+str(length)+"]")))
            # actions.move_to_element(selectTile).perform()

            # deleteUpload = wait.until(EC.element_to_be_clickable((By.XPATH, DeleteUpload+"[2]")))
            # deleteUpload.click()

            # alert = driver.switch_to.alert
            # alert.accept()
            
            # main = driver.find_element(By.TAG_NAME, 'body')
            # main.send_keys(Keys.ESCAPE)

            # replacing the image
            sleep(2.5)
            selectImage = wait.until(EC.element_to_be_clickable((By.XPATH, SelectImage)))
            selectImage.click()

            myFileButton = wait.until(EC.element_to_be_clickable((By.XPATH, MyFileButton)))
            myFileButton.click()

            # search and check if the image is already uploaded
            sleep(2.5)
            searchButton = wait.until(EC.element_to_be_clickable((By.XPATH, SearchButton)))
            searchButton.clear()
            searchButton.send_keys(ImgDict[key+"_"+str(i)])
            searchButton.send_keys(Keys.RETURN)
            sleep(2.5)
            try: 
                length = len(WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, SelectImageTile))))

                if length:
                    selectTile = wait.until(EC.element_to_be_clickable((By.XPATH, "("+SelectImageTile+"//div[.//*[text() = '"+ImgDict[key+"_"+str(i)]+".png']]/..)[1]")))
                    actions.double_click(selectTile).perform()

            except:
                # print("Uploading image"+ ImgDict[key+"_"+str(i)])


                uploadButton = wait.until(EC.element_to_be_clickable((By.XPATH, UploadButton)))
                uploadButton.send_keys(image_path)

                waitCheck = wait.until(EC.element_to_be_clickable((By.XPATH, UploadButton)))
                length = getLenghth(SelectImageTile)                     #to select the latest tile
                selectTile = wait.until(EC.element_to_be_clickable((By.XPATH, "("+SelectImageTile+"//div[.//*[text() = '"+ImgDict[key+"_"+str(i)]+".png']]/..)[1]")))
                actions.double_click(selectTile).perform()

                

            # DELETING LOGIC
            # selectImage = wait.until(EC.element_to_be_clickable((By.XPATH, SelectImage)))
            # selectImage.click()

            # length = getLenghth(SelectImageTile)                     #to take cursor to the latest tile
            # selectTile = wait.until(EC.element_to_be_clickable((By.XPATH, "("+SelectImageTile+")["+str(length)+"]")))
            # actions.move_to_element(selectTile).perform()

            # deleteUpload = wait.until(EC.element_to_be_clickable((By.XPATH, DeleteUpload+"[4]")))
            # deleteUpload.click()

            # alert = driver.switch_to.alert
            # alert.accept()

            # main = driver.find_element(By.TAG_NAME, 'body')
            # main.send_keys(Keys.ESCAPE)
            
            if i != paraCount-1:
                # duplicating the scene
                length = getLenghth(DuplicateScene)
                duplicateScene = wait.until(EC.element_to_be_clickable((By.XPATH, "("+DuplicateScene+")["+str(length)+"]")))
                duplicateScene.click()

                confirmButton = wait.until(EC.presence_of_element_located((By.XPATH, ConfirmButton)))
                confirmButton.send_keys(Keys.RETURN)
                sleep(2)

            else:
                print("Done with video: ", key)

        except Exception as e:
            print("Error in para: ", i,"of video: ", key)
            renameFile = wait.until(EC.element_to_be_clickable((By.XPATH, RenameFile)))
            renameFile.send_keys("  "+key)
            renameFile.send_keys(Keys.RETURN)
            print(e)
            break

    

print("Done")