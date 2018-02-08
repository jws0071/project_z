# parser.py
import requests
from bs4 import BeautifulSoup
Script_Raw = []
result = []
c = []
# HTTP GET Request

def last_view(req,intnum):
    # HTML 소스 가져오기
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        'table.gTable.clr > tr > td.txt > a'
    )

    f = open("C:/test/item_code_list"+intnum+".txt", 'a')
    for title in my_titles:
        # title.split()
        re_title = title['href'].replace("/item/main.daum?code=", "")
        re_title_text = title.text.replace(" ","")
        file_str = re_title + " " + re_title_text + "\n"
        f.write(file_str)
        print(re_title + "  " + title.text)
    f.close()

req = requests.get('http://finance.daum.net/quote/all.daum?type=S&stype=P') #코스피
req1 = requests.get('http://finance.daum.net/quote/all.daum?type=S&stype=Q') #코스닥
intnum1="1"
intnum2="2"
last_view(req, intnum1)
last_view(req1,intnum2)






