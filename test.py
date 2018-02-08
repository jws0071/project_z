# parser.py
import requests
from bs4 import BeautifulSoup

# HTTP GET Request
req = requests.get('http://finance.daum.net/item/main.daum?code=028050')
req1 = requests.get('http://finance.daum.net/item/main.daum?code=251270')
req2 = requests.get('http://finance.daum.net/item/main.daum?code=035720')
req3 = requests.get('http://finance.daum.net/item/main.daum?code=046890')
# HTML 소스 가져오기
#def view(req):
html = req.text
soup = BeautifulSoup(html, 'html.parser')
# stockContent > ul.list_price > li:nth-child(1) > dl.first > dd
my_titles = soup.select(
    '#stockContent > ul.list_price > li:nth-of-type(1) > dl.first > dd'
    #'#topWrap > div.CT_ZONE_DETAILTOPINFO > ul.list_stockrate > li:nth-of-type(1) > em'
    )
#print(my_titles)

for title in my_titles:
    # Tag안의 텍스트
    print(title.text)
    #result = title.text
    #return result
'''
res = view(req)
res1 = view(req1)
res2= view(req2)
res3 = view(req3)

print(res +  " // " + res1+  " // " + res2+  " // " + res3)
'''