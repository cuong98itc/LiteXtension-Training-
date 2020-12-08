import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

url = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'
payload ={
    'log': 'admin',
    'pwd': '123456aA'
}
try:
    response = requests.post(url, data=payload)
except NameError as err:
    print('status: ', response)
    print(err)
    exit()
soup = BeautifulSoup(response.text, 'html.parser')
UserName = soup.find('span', class_='display-name')
print(UserName.text.strip())