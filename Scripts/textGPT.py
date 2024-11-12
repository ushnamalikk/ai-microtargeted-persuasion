from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
from selenium.webdriver.support import expected_conditions as EC
import json


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
waitTime = 80               #seconds



print("Driver started")

#actrion variables

#loading prompt 1
promptDict = {}
with open('promptDict.json', 'r') as fp:
    promptDict = json.load(fp)

#other prompts
prompt2 = "Now translate this script to Urdu" 
prompt3 = "Can you convert it into a script that is written the way it should be pronounced in English?"


#XPATHs
TextBox = "//textarea[contains(@id,'prompt-textarea')]"
SendPrompt = "//button[contains(@aria-label,'Send promp')]"
# WaitCheck = "//div[contains(@class,'mt-1 flex gap-3 empty:hidden juice:-ml-3')]"
WaitCheck = "//button[contains(@data-testid,'stop-button')]"    #updated
# ResultParaN = "//div[contains(@class,'markdown prose')]/p[]"
NewChat = "//div[contains(@class,'flex h-14 items-center')]//span[contains(@class,'flex')][2]//button[contains(@class,'bg-token-sidebar-surface-secondary')]"
NewChat2 = "//div[@class='flex items-center']//span[contains(@class,'flex')][2]//button[contains(@class,'bg-token')]"   #when side bar is closed use this instead



driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, waitTime)

#open website 
driver.get('https://chatgpt.com/')

# storing result in dict
responseDict = {}

# load dict from json (if present)
try:
    with open('responseDict.json', 'r') as fp:
        responseDict = json.load(fp)
except:
    print("No previous responses found\nrunning code for the first time")


for key in promptDict:

    if key in responseDict:                                                         #checkpointing <3
        print("Response already present for key", key)
        continue

    prompt = promptDict[key]

    sleep(1)
    # entering the prompt in text field
    textbox = wait.until(EC.element_to_be_clickable((By.XPATH, TextBox)))
    textbox.send_keys(prompt)
    sleep(2)
    textbox.send_keys(Keys.RETURN)
    sleep(0.5)

    #proceed when waitcheck is unclickable 
    wait.until(EC.invisibility_of_element_located((By.XPATH, WaitCheck)))
    sleep(0.5)

    # entering the prompt2 in text field
    textbox = wait.until(EC.element_to_be_clickable((By.XPATH, TextBox)))
    textbox.send_keys(prompt2)
    textbox.send_keys(Keys.RETURN)
    sleep(0.5)

    #proceed when waitcheck is unclickable
    wait.until(EC.invisibility_of_element_located((By.XPATH, WaitCheck)))
    sleep(0.5)
    
    # entering the prompt3 in text field
    textbox = wait.until(EC.element_to_be_clickable((By.XPATH, TextBox)))
    textbox.send_keys(prompt3)
    textbox.send_keys(Keys.RETURN)
    sleep(0.5)
    
    #proceed when waitcheck is unclickable
    wait.until(EC.invisibility_of_element_located((By.XPATH, WaitCheck)))
    sleep(1)


    #geetting the final response from gpt
    ResultParaN = "//div[contains(@class,'markdown prose')]/p"
    paragraphs = wait.until(EC.presence_of_all_elements_located((By.XPATH, ResultParaN)))

    result = ""
    for paragraph in paragraphs:
        result += paragraph.text + "\n"

    responseDict[key] = result

    #saving the response dict
    with open('responseDict.json', 'w', encoding='utf-8') as fp:
        json.dump(responseDict, fp, ensure_ascii=False)

    print("Response saved for key", key)

    #clicking new chat
    newchat = wait.until(EC.element_to_be_clickable((By.XPATH, NewChat2)))
    newchat.click()

    sleep(5)



print("All prompts are processed")
driver.quit()
