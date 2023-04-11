
from bs4 import BeautifulSoup
import requests
import time
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

#save console in text file
# import sys 
# file_path = "screen.txt'
# sys.stdout = open(file_path, "w")


# #### 1. Access https://www.planespotters.net/user/login using a standard GET request. 
#Read and store the cookies received in the response.  
#In addition, parse the response and read (and store to a string variable) the value of the hidden input field that will (most likely) be required in the login process.


try: 
    # Call requests module's session() method to return a requests.sessions.Session object.
    session = requests.Session()
    # Show all headers and cookies in this session.
    session.headers
    # Use this session object to get a web page by url.
    response = session.get("https://www.planespotters.net/user/login", headers=header)
    # When above browse web page process complete, this session has cookies.
    soup = BeautifulSoup(response.text, 'lxml')
    cookies_pre = session.cookies.get_dict()
    print("Cookies get login page:",cookies_pre)
    csrf = soup.find('input', {'id': 'csrf'}).get('value')
    print("csrf:",csrf)
    rid = soup.find('input', {'id': 'rid'}).get('value')
    print("rid:",rid)
    
except:
  print("Problem with the connection...")


# #### 2. Make a post request using the cookies from (1) as well as all required name-value-pairs (including your username and passwords).

# #### 3. Get the cookies from the response of the post request and add them to your cookies from (1).


try: 
    # Call requests module's session() method to return a requests.sessions.Session object.
    # Show all headers and cookies in this session.
    # Use this session object to get a web page by url.
    username = "username"
    password = "password"
    response = session.post("https://www.planespotters.net/user/login", headers = header,
                            data={"username": username,
                                  "password": password,
                                  "csrf": csrf,
                                  "rid:": rid},
                            cookies=cookies_pre)
    # When above browse web page process complete, this session has cookies.
    cookies_post = session.cookies.get_dict()
    print("Cookies post login page:", cookies_post)    
except:
  print("Problem with the connection...")



# #### 4. Verify that you are logged in by accessing the profile page https://www.planespotters.net/member/profile Links to an external site.with the saved cookies.


try: 
    url= "https://www.planespotters.net/member/profile"
    page = session.get(url, headers = header, cookies=cookies_post)
    # Create a beautifulsoup object 
    soup = BeautifulSoup(page.text, 'lxml')
except:
  print("Problem with the connection...")




# #### 5. A boolean value to show your username is contained in the document "soup".

print(bool(soup.findAll(text = username)))

