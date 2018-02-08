# parser.py
import requests
from bs4 import BeautifulSoup
Script_Raw = []
result = []
c = []
# HTTP GET Request
req = requests.get('http://finance.daum.net/quote/fall.daum?stype=P&page=1&col=pchgrate&order=asc')
# HTML 소스 가져오기
html = req.text
soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
    'table.gTable.clr.subPrice > tr > td.txt > a'
)
print(my_titles)


for title in my_titles:
    re_title = title['href'].replace("/item/main.daum?code=", "")
    re_title_text = title.text.replace(" ","")
    print(re_title)

