import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_separator():
    print("\n" + "="*50 + "\n")

clear_terminal()

print_separator()
browser_choice = input("Choose your browser (1 for Chrome, 2 for Firefox): ")

if browser_choice == '1':
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    driver_path = "chromedriver"
    driver = webdriver.Chrome(service=Service(driver_path), options=options)

elif browser_choice == '2':
    options = FirefoxOptions()
    options.add_argument("--start-maximized")
    driver_path = "geckodriver"
    driver = webdriver.Firefox(service=FirefoxService(driver_path), options=options)

else:
    print("Invalid choice. The program will now exit.")
    exit()

print_separator()
driver.get("https://discord.com/login")
input("Log into Discord, then press Enter here when you're done...")

print_separator()
driver.get("https://disboard.org/servers")
keyword = input("What keyword would you like to search for a server?: ")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(keyword)
search_box.send_keys(Keys.RETURN)

time.sleep(5)

join_buttons = driver.find_elements(By.CLASS_NAME, "btn-join")
print(f"{len(join_buttons)} servers found. Joining the first 3...\n")

for button in join_buttons[:3]:
    try:
        button.click()
        time.sleep(3)
    except Exception as e:
        pass

print_separator()
msg = input("What message would you like to spam?: ")
count = int(input("How many times?: "))
delay = float(input("Delay between each message (in seconds): "))

print_separator()
print("Starting the message sending process...\n")

for i in range(count):
    try:
        textarea = driver.find_element(By.TAG_NAME, "textarea")
        textarea.send_keys(msg)
        textarea.send_keys(Keys.RETURN)
        print(f"[{i+1}/{count}] Message sent.")
        time.sleep(delay)
    except Exception as e:
        print(f"Error sending the message: {e}")
        break

print_separator()
print("Process completed. Thank you for using the script.")
