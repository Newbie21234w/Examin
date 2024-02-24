import requests
import lxml
from bs4 import BeautifulSoup
url = "https://kups.club/"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
session = requests.session()
response = session.get(url, headers=header)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="lxml")
    allproduct = soup.find("div",  class_="col-lg-4 col-md-sm-6")
    products = allproduct.find_all("div", class_="card-text")



