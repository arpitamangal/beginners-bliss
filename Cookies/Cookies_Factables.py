
# #### Go to fctables.com and create an account. Let’s place a virtual bet and we will verify the login by accessing the bet here.


#Loading Packages
from bs4 import BeautifulSoup
import requests
import time
header = {'User-Agent':'Mozilla/5.0'}



# #### Code that automatically logs into the website fctables.com


# creating a sessionn request use the login usename and password for the account created
session = requests.Session()
session.headers
response = session.post("https://www.fctables.com/user/login/", data={"referer": "https://www.fctables.com/",
                                                               "login_action": "1",
                                                               "login_username": "username",
                                                               "login_password": "password",
                                                               "user_remeber": "1",
                                                               "submit": "1"})
# saving cookies from session
cookies = session.cookies.get_dict()
cookies
time.sleep(10)


# #### Verify that you have successfully logged in:  use the cookies you received during log in and write code to access https://www.fctables.com/tipster/my_bets/ .  Check whether the bet appears on the page. 


URL = "https://www.fctables.com/tipster/my_bets/"
page = session.get(URL,  cookies=cookies)
soup = BeautifulSoup(page.content, 'html.parser')
div = soup.select("div.game")
for i in div:
    print (i.text)


