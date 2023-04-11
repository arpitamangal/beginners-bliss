# starts a browser of your choice, navigates to google.com, and searches for "askew" as well as "google in 1998" (separate searches!)


from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}



def launch_URL():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.set_script_timeout(120)
    driver.set_page_load_timeout(10)
    driver.get(url)
    return driver


def search_google(driver,text):
    inp = driver.find_element(By.CSS_SELECTOR,"input[type=text]")
    inp.send_keys(text)

try:
    url = "https://google.com"
    text = "askew\n"
    driver = launch_URL()
    search_google(driver,text)
    time.sleep(10)
    driver.quit()
except:
  print("Problem with the connection...")


try:
    url = "https://google.com"
    text = "google in 1998\n"
    driver = launch_URL()
    search_google(driver,text)
    time.sleep(10)
    driver.quit()
except:
  print("Problem with the connection...")

