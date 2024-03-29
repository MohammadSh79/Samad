from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
import platform
import os
import sys
import time

load_dotenv()

username = os.getenv('STUDENT_ID')
password = os.getenv('PASSWORD')
food = os.getenv('FOOD_NAME')
selfName = os.getenv('SELF_NAME')
nextWeek = True if os.getenv('NEXT_WEEK').lower() == 'true' else False # Should I click on the next week arrow before searching for food?

refreshCount = 0
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

driver.get("https://food.guilan.ac.ir/")
print('[INFO] Site loaded')

# Login
username_input = driver.find_element(By.NAME, 'username').send_keys(username)
password_input = driver.find_element(By.NAME, 'password').send_keys(password)
driver.find_element(By.NAME, "login").click()

if 'نام کاربری یا رمز عبور اشتباه است' in str(driver.page_source):
    print('[ERROR] Wrong Username or Password')
    driver.close()
    sys.exit(0)

print('[INFO] Logged in successfully')

# Select 'Reserve Food'
driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/span").click()

time.sleep(1)

# Select Self
menu = Select(driver.find_element(By.XPATH, '//*[@id="selectself_selfListId"]'))
menu.select_by_visible_text(selfName)

driver.find_element(By.XPATH, "//div[@id='generalAjaxDialogBodyDiv']/table/tbody/tr[3]/td/input").click()
print('[INFO] Self Selected')

if nextWeek:
    driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div/div/div[2]/form[1]/table/tbody/tr/td/table/tbody/tr[1]/td[5]/input").click()

driver.get_screenshot_as_file("Screenshot.png")
print("[INFO] Screenshot saved")

# Select food
while True:
    try:
        foodName = driver.find_element(By.XPATH, "//*[contains(text(), '" + str(food) +  "')]")
        foodBox = foodName.find_element(By.XPATH, "../../../../../..")
        images = foodBox.find_elements(By.TAG_NAME, 'img')
        exitt = False
        for image in images:
            if 'buy' in image.get_attribute('src'):
                image.click()
                exitt = True
                break
        if exitt:
            break
        refreshCount += 1
        sys.stdout.write("\rRefresh Count: {0}\n".format(refreshCount))
        sys.stdout.flush()
        driver.refresh()
        
    except:
        refreshCount += 1
        sys.stdout.write("\rRefresh Count: {0}\n".format(refreshCount))
        sys.stdout.flush()
        driver.refresh()
        pass

driver.switch_to.alert.accept()
driver.find_element(By.XPATH, "//*[@id='doReservBtn']").click()
driver.close()
print("[INFO] Done MotherFucker B-)")
sys.exit(0)