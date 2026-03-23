from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def start_driver():
    chrome_options = Options()

    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")

    # 🔥 IMPORTANT FIX — disable Selenium Manager
    os.environ["SE_MANAGER_PATH"] = ""

    service = Service(executable_path="/opt/homebrew/bin/chromedriver")

    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver