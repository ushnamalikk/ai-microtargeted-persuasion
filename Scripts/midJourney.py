from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
from selenium.webdriver.support import expected_conditions as EC
import json
import re



text_dict = {}
with open('responseDict.json', 'r') as f:
    text_dict = json.load(f)


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
waitTime = 70               #seconds



prompt1 = "You are well experienced in curating a prompt for Midjourney."
prompt2 = "I will give you a template and some other instructions."
prompt3 = "For any text I provide, you have to decide multiple scenes that best describe the text and give me the prompt for them."
prompt4 = "Template: [subject],[camera angle],[detail],[mood],[lighting],[color grading],[camera lens]"
prompt5 = "Instructions: for angles you can use wide angle, high angle, low angle, from behind, from front, bird's eye view, or any combination of these."
prompt6 = "For lighting, you can use morning, noon, sunset, night, golden hour, sunny, overcast, foggy, smoggy, natural lighting, or silhouette."
prompt7 = "For color grading, either muted colors or desaturated colors."
prompt8 = "For style, I prefer you to use 35 mm disposable camera style or Polaroid."

prompt9 = "I am providing you with some example prompts that I have previously used. Make sure you understand them so when I provide you with text, you can create a perfectly curated prompt tuned for my taste."
prompt10 = "make sure that you create the prompt that is based in a pakistani setting and is culturally relevant. when using characters make them pakistani"
prompt11 = "A top angle shot captures a group of university students gathered around an outdoor study space on campus engaged in conversation. They sit with Urdu literature and history books spread out, with one student reading aloud while others listen intently. Behind them, a building with traditional architectural elements adds to the patriotic atmosphere, blending academic ambition with cultural heritage. Shot at morning time with sunny atmosphere using 35 mm disposable camera."
prompt12 = "A bird's eye view of a breathtaking view of Badshahi Mosque at night, with modern skyscrapers lit up against the dark sky. The streets are bustling with activity, and lights from homes and businesses create a vibrant, lively atmosphere. Natural lighting with muted tones and camera specs 35mm."
prompt13 = "I will provide you with a text, and for each paragraph, you will return multiple prompts. Make sure your response is like the above paragraphs without any heading, plain simple text, and line-separated."



#XPATHs
Tabvar = 1
TextBox = "//textarea[contains(@id,'input')]"
QueueCount = "//div[contains(@class,'space-between flex items-start flex-grow-0')]"

# chat gpt
ChatTextBox = "//div[contains(@id,'prompt-textarea')]"
SendPrompt = "//button[contains(@aria-label,'Send promp')]"
WaitCheck = "//button[contains(@data-testid,'stop-button')]"    #updated
NewChat = "//div[contains(@class,'flex h-14 items-center')]//span[contains(@class,'flex')][2]//button[contains(@class,'bg-token-sidebar-surface-secondary')]"
NewChat2 = "//div[@class='flex items-center']//span[contains(@class,'flex')][2]//button[contains(@class,'bg-token')]"   #when side bar is closed use this instead
PrompCount = 1

# switches between 0 or 1 tab
def switchTab():
    global Tabvar
    if Tabvar == 0:
        Tabvar = 1
    else:
        Tabvar = 0
    driver.switch_to.window(driver.window_handles[Tabvar])


driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, waitTime)
print("Driver started")

#open website 
driver.get('https://www.midjourney.com/imagine')

#open google on new tab 
driver.switch_to.new_window('tab')
driver.get('https://chatgpt.com/')
sleep(2)

chattext_box = wait.until(EC.presence_of_element_located((By.XPATH, ChatTextBox)))
chattext_box.clear()

prompts = [prompt1, prompt2, prompt3, prompt4, prompt5, prompt6, prompt7, prompt8]
for prompt in prompts:
    chattext_box.send_keys(prompt)
    chattext_box.send_keys(Keys.SHIFT, Keys.ENTER)
    
chattext_box.send_keys(Keys.ENTER)
sleep(0.5)

PrompCount += 1

#wait for the response
wait.until(EC.invisibility_of_element_located((By.XPATH, WaitCheck)))
sleep(0.5)

chattext_box = wait.until(EC.presence_of_element_located((By.XPATH, ChatTextBox)))
chattext_box.clear()

prompts = [prompt9, prompt10, prompt11, prompt12, prompt13]
for prompt in prompts:
    chattext_box.send_keys(prompt)
    chattext_box.send_keys(Keys.SHIFT, Keys.ENTER)

chattext_box.send_keys(Keys.ENTER)
sleep(0.5)

PrompCount += 1

#wait for the response
wait.until(EC.invisibility_of_element_located((By.XPATH, WaitCheck)))
sleep(0.5)



Skipuntil = False


# for each text in the second of dict strip each para and enter in text box
for key in text_dict:
    
    if key == "1a":
        break

    if key == "3b010":
        Skipuntil = True

    if Skipuntil == False:
        print("Skipping: ", key)
        continue
    
    print("Processing: ", key)
    text = text_dict[key]
    prompts = text['second']
    prompts = prompts.split("\n\n")
    
    chattext_box = wait.until(EC.presence_of_element_located((By.XPATH, ChatTextBox)))
    chattext_box.clear()
    
    for prompt in prompts:
        chattext_box.send_keys(prompt)
        chattext_box.send_keys(Keys.SHIFT, Keys.ENTER)
        chattext_box.send_keys(Keys.SHIFT, Keys.ENTER)
        # print("Prompt: ", prompt)

    #press enter
    chattext_box.send_keys(Keys.ENTER)
    sleep(0.5)

    #wait for the response
    wait.until(EC.invisibility_of_element_located((By.XPATH, WaitCheck)))
    sleep(0.5)

    #get the response
    ResultParaN = "(//div[contains(@class,'markdown prose')])[" + str(PrompCount) + "]/p"
    paragraphs = wait.until(EC.presence_of_all_elements_located((By.XPATH, ResultParaN)))
    textparagraph = []
    for para in paragraphs:
        textparagraph.append(para.text)
        print(para.text)

    sleep(0.5)
    # switch to midjourney tab
    switchTab()

    for para in textparagraph:
        while True:
            try:
                element = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, QueueCount)))
                match = re.search(r"(\d+)", element.text)
                ActualCount = int(match.group(1)) if match else None
                print("Queue count:", ActualCount)

                if ActualCount < 9:
                    MJtextbox = wait.until(EC.presence_of_element_located((By.XPATH, TextBox)))
                    MJtextbox.send_keys(para)
                    MJtextbox.send_keys(Keys.RETURN)
                    break  # Exit the loop if count is less than 10
                else:
                    print("Queue count is more than 10, waiting to retry...")
                    sleep(15)  # Wait for 5 seconds before retrying
                    driver.refresh()

            except:
                # If the element is not found, proceed with sending the text
                MJtextbox = wait.until(EC.presence_of_element_located((By.XPATH, TextBox)))
                MJtextbox.send_keys(para)
                MJtextbox.send_keys(Keys.RETURN)
                print("Queue count not found, proceeding.")
                break  # Exit the loop if queue count element is not found

        sleep(1)
    
    switchTab()
    PrompCount += 1




        
print("All Images are processed")
driver.quit()
