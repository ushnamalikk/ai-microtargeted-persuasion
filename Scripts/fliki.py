from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
from selenium.webdriver.support import expected_conditions as EC
import time

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
wait = WebDriverWait(driver, 10)

print("Driver started")

# #actrion variables
# nameVideo = "Reallocation For"
# langVideo = 0

# #response file is in the previoius folder
# with open("response.txt", "r") as file:
#     responses = file.read().split("\n")
#     # print(responses)

# ImageNames = []
# baseImageName = "unique_"
# for i in range(len(responses)):
#     ImageNames.append(baseImageName + str(i+1) + ".jpeg")


#XPATHs
NewFile = "//button[contains(@class,'module_primary__FOp7N')]"
EmptyWorkflow = "(//h4[contains(text(),' Empty')])[1]"
FileName = "//input[contains(@placeholder,'Enter file name')]"
AspectRatio = "//button[contains(text(),'16:9')]"
UrduLanguage = "//option[contains(@value,'61b8b3024268666c126bac27')]" 
# EngLanguage = "//option[contains(@value,'61b8b2f54268666c126babc9')]" 
PakistanDialect = "//option[contains(@value,'61b8b3144268666c126bacaf')]"
# ScriptType = "//option[contains(@value,'script')]"
Submit = "//button[contains(@type,'submit')]"

# now we in the main workspace
ScriptText = "//textarea[contains(@placeholder,'Paste')]"
StockImages = "//input[contains(@value,'image')]"

BGAudio = "//button[contains(@class,'style-module_outline__Yyq-Q')]"
FavoritesAudio = "//button[contains(@id,'trigger-favorite')]"
FirstAudio = "//div[contains(@class,'_row_1igxt_33 _audioList_1igxt_38')]/div[contains(@class,'_item_1v22e_1')]"        #cant test without the payment

Scene1 = "(//div[contains(@class,'_compact')])[1]"
DeleteVoice = "(//div[contains(@class, 'style_layer__cJEm0')])[3]/div/div[2]/span/button"
ConfirmButton = "//button//span[contains(text(),'Confirm')]"

selectScene = "//div[contains(@class,'style_section__sYDzF')][2]/div"
AddLayer = "(//button[contains(., 'Add layer')])[2]"
AddAudio = "//div[contains(@role, 'menuitem') and contains(., 'Audio')]"
AddText = "//div[contains(@role, 'menuitem') and contains(., 'Text')]"      #khudi ko kar buland itna 

VoiceoverText = "//div[contains(@class,'_layer_ool4d_1')]"
RotationText = "//input[contains(@placeholder,'Rotation')]"
VoiceArtist = "//*[contains(text(),'Mia')]"
Stephen = "//span[contains(text(),'Stephen')]"
SelectVoice = "//span[contains(text(),'Select')]"
ImageButton = "//button[contains(@class,'_preview_1knpk_8')]"
SearchImage = "//input[contains(@placeholder,'Search for your uploaded files')]"
FirstImageSearch = "//div[contains(@class,'_item_4k1jf_1')]"
# AddScene ="//div[contains(@class,'_section_bqfam_1')][3]/div[contains(@class,'_add_bqfam_222')]/button[1]"
# SceneN = "//div[contains(@class,'_section_bqfam_1')][4]/div[contains(@class,'_scene_bqfam_4')]"
# SceneScriptInput = "//*[contains(@data-placeholder,'Start writing or paste script here')]"

# sleep(3000)

#open website 
driver.get('https://app.fliki.ai/files')

#create new file
newfile = wait.until(EC.presence_of_element_located((By.XPATH, NewFile)))
newfile.click()

#select empty workflow
emptyworkflow = wait.until(EC.presence_of_element_located((By.XPATH, EmptyWorkflow)))
emptyworkflow.click()

# #find buttons & fill in the details
filename = wait.until(EC.presence_of_element_located((By.XPATH, FileName)))
aspectratio = wait.until(EC.presence_of_element_located((By.XPATH, AspectRatio)))
urdu = wait.until(EC.presence_of_element_located((By.XPATH, UrduLanguage)))
# eng = wait.until(EC.presence_of_element_located((By.XPATH, EngLanguage)))
# Adtype = wait.until(EC.presence_of_element_located((By.XPATH, ScriptType)))
submit = wait.until(EC.presence_of_element_located((By.XPATH, Submit)))

filename.send_keys("test")
aspectratio.click()
urdu.click()
dialect = driver.find_element(By.XPATH, PakistanDialect)
dialect.click()


# Adtype.click()
submit.click()

# sleep(300)

# #find buttons & fill in the script
# scriptText = wait.until(EC.presence_of_element_located((By.XPATH, ScriptText)))
# stockImages = wait.until(EC.presence_of_element_located((By.XPATH, StockImages)))
# submit = wait.until(EC.presence_of_element_located((By.XPATH, Submit)))

# scriptText.send_keys(responses[0])   #gen initially with just one para
# stockImages.click()
# submit.click()

#wait for processing of video
sleep(3)
# bgAudio = wait.until(EC.element_to_be_clickable((By.XPATH, BGAudio)))
# bgAudio.click()
# favoritesAudio = wait.until(EC.element_to_be_clickable((By.XPATH, FavoritesAudio)))
# favoritesAudio.click()
# firstAudio = wait.until(EC.element_to_be_clickable((By.XPATH, FirstAudio)))
# firstAudio.click()

#now we have one para video we make settings in this then we duplicate scns so we dont have to set settings again
#correcting the rotation tilt
scene1 = wait.until(EC.element_to_be_clickable((By.XPATH, Scene1)))
scene1.click()

#first hover over the delete voice then click on it
deleteVoice = wait.until(EC.element_to_be_clickable((By.XPATH, DeleteVoice)))
deleteVoice.click()


confirmButton = wait.until(EC.element_to_be_clickable((By.XPATH, ConfirmButton)))
confirmButton.click()

#addding text and audio
addLayer = wait.until(EC.element_to_be_clickable((By.XPATH, AddLayer)))
addLayer.click()
addText = wait.until(EC.element_to_be_clickable((By.XPATH, AddText)))
addText.click()

sleep(2)
addLayer = wait.until(EC.element_to_be_clickable((By.XPATH, AddLayer)))
addLayer.click()
addAudio = wait.until(EC.element_to_be_clickable((By.XPATH, AddAudio)))
addAudio.click()





# all tested and running most XPaths till yet are doing pattern matching so they are not likely to change


sleep(200)

voiceoverText = wait.until(EC.element_to_be_clickable((By.XPATH, VoiceoverText)))
voiceoverText.click()
rotationText = wait.until(EC.element_to_be_clickable((By.XPATH, RotationText)))
rotationText.clear()
rotationText.send_keys("0")

#correcting the voice artist    ElevenLabs changes this part of the code
try:
    voiceArtist = wait.until(EC.element_to_be_clickable((By.XPATH, VoiceArtist)))
    voiceArtist.click()
    stephen = wait.until(EC.element_to_be_clickable((By.XPATH, Stephen)))
    stephen.click()
    selectVoice = wait.until(EC.element_to_be_clickable((By.XPATH, SelectVoice)))
    selectVoice.click()
except:
    print("Voice artist already selected")

#correcting the media
imagebutton = wait.until(EC.element_to_be_clickable((By.XPATH, ImageButton)))
imagebutton.click()
searchImage = wait.until(EC.element_to_be_clickable((By.XPATH, SearchImage)))
searchImage.send_keys(ImageNames[0])
searchImage.send_keys(Keys.RETURN)
firstImageSearch = wait.until(EC.element_to_be_clickable((By.XPATH, FirstImageSearch)))
firstImageSearch.click()


#duplicate the scene
for i, response in enumerate(responses[1:]):
    #adding new scene
    AddScene ="//div[contains(@class,'_section_bqfam_1')]["+str(i+2)+"]/div[contains(@class,'_add_bqfam_222')]/button[1]"
    addScene = wait.until(EC.element_to_be_clickable((By.XPATH, AddScene)))
    addScene.click()
    #selecting new scene
    sceneN = "//div[contains(@class,'_section_bqfam_1')]["+str(i+3)+"]/div[contains(@class,'_scene_bqfam_4')]"
    sceneN = wait.until(EC.element_to_be_clickable((By.XPATH, sceneN)))
    sceneN.click() 
    #adding the text
    SceneScriptInput = "//*[contains(@data-placeholder,'Start writing or paste script here')]"
    sceneScriptInput = wait.until(EC.element_to_be_clickable((By.XPATH, SceneScriptInput)))
    sceneScriptInput.send_keys(response)
    #adding the media
    imagebutton = wait.until(EC.element_to_be_clickable((By.XPATH, ImageButton)))
    imagebutton.click()
    searchImage = wait.until(EC.element_to_be_clickable((By.XPATH, SearchImage)))
    searchImage.send_keys(ImageNames[i+1])
    searchImage.send_keys(Keys.RETURN)
    firstImageSearch = wait.until(EC.element_to_be_clickable((By.XPATH, FirstImageSearch)))
    firstImageSearch.click()
    
    sleep(2)


print("Done")
sleep(3000)
