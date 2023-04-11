


# #### write a script that goes to bestbuy.com, clicks on Deal of the Day, reads how much time is left for the Deal of the Day and prints the remaining time to screen (console), clicks on the Deal of the Day (the actual product), clicks on its reviews, and saves the resulting HTML to your local hard drive as "bestbuy_deal_of_the_day.htm"


from bs4 import BeautifulSoup
import requests
import time
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


#save console in text file
# import sys 
# file_path = "screen.txt'
# sys.stdout = open(file_path, "w")

def launch_URL():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.set_script_timeout(120)
    driver.set_page_load_timeout(10)
    driver.get(url);
    return driver



url = "https://bestbuy.com"
driver = launch_URL()


#clicks on Deal of the Day,
dealOfTheDay = driver.find_element(By.XPATH,"//a[text()='Deal of the Day']")
dealOfTheDay.click()
time.sleep(2)



#reads how much time is left for the Deal of the Day and prints the remaining time to screen (console),
remainingTime = driver.find_element(By.CLASS_NAME, "sr-only.sale-timer")
print(remainingTime.text)



#clicks on the Deal of the Day (the actual product)
offerProduct = driver.find_element(By.CLASS_NAME, "wf-offer-description.productV2")
offerProduct.click()
time.sleep(2)

#clicks on its reviews
productReview = driver.find_element(By.XPATH, "//span[text()='Reviews']")
productReview.click()
time.sleep(2)


#obtain page source
page = driver.page_source


#saves the resulting HTML to your local hard drive as "bestbuy_deal_of_the_day.htm"
filename = "bestbuy_deal_of_the_day.htm"
with open(filename, "w", encoding = 'utf-8') as file:
    file.write(page)
print("Saved File:", filename)

driver.quit()

