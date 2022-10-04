from imp import source_from_cache
import profile
import requests
from bs4 import BeautifulSoup as bs

github_user = input('Enter your GIthub user name:')
url = "https://github.com/"+github_user
r = requests.get(url)

soup = bs(r.content,"html.parser")
profile_infomation =  soup.find("img",{"alt": "Avatar"} )['src']
print(profile_infomation)