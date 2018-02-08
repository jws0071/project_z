# parser.py
import requests
from bs4 import BeautifulSoup
from PyQt4.QtGui import *
from PyQt4 import QtCore
import sys
import time
i = 0
sec = 1  #위젯 종료후 재기동 시간


def view(req):
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    my_titles = soup.select(
        '#topWrap > div.CT_ZONE_DETAILTOPINFO > ul.list_stockrate > li:nth-of-type(1) > em'
    )
    # print(my_titles)
    for title in my_titles:
        # Tag안의 텍스트
        result = title.text
    return result

def last_view(req):
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    my_titles = soup.select(
        '#stockContent > ul.list_price > li:nth-of-type(1) > dl.first > dd'
    )
    # print(my_titles)
    for title in my_titles:
        # Tag안의 텍스트
        result = title.text
    return result

def url():
    number = input(" 종목수 입력하세요(최대 4개)")
    code_list = []
    for i in range (0, int(number)) :
        code = input("종목 코드를 입력하세요 : ")
        test = "http://finance.daum.net/item/main.daum?code="+code
        code_list.insert(i, test)
    return code_list


class MyDialog(QDialog) :

    code_list = url()

    def __init__(self):
        QDialog.__init__(self)
        #print(test)
        res = []
        last_res = []
        sum_res = []

        for i in range(0, int(len(MyDialog.code_list))):
            req = requests.get(MyDialog.code_list[i])
            tmp_res = view(req)
            res.insert(i,tmp_res)
            tmp_last_res = last_view(req)
            last_res.insert(i, tmp_last_res)

        for h in range(0, int(len(res))):
            last_res_re = last_res[h].replace(",", "")
            res_re = res[h].replace(",", "")
            test = str(float(res_re) - float(last_res_re))
            sum_res.insert(h, test)

        last_res_str = ""
        res_str = ""
        sum_res_str = ""
        for j in range(0, int(len(last_res))):
            last_res_str += str(last_res[j]) + " // "
            res_str += str(res[j]) + " // "
            sum_res_str += str(sum_res[j]) + " // "


        # 레이블,Edit,버튼 컨트롤
        lblName_last = QLabel(last_res_str)
        lblName = QLabel(res_str)
        lblName_sum = QLabel(sum_res_str)
        btnOk = QPushButton("종료")

        # 레이아웃
        layout = QVBoxLayout()
        layout.addWidget(lblName_last)
        layout.addWidget(lblName)
        layout.addWidget(lblName_sum)
        layout.addWidget(btnOk)

        # 다이얼로그에 레이아웃 지정
        self.setLayout(layout)
        self.setGeometry(0, 900, 0, 0) # 화면 위치 설정
        #btnOk.clicked.connect(sys.exit(1))
        btnOk.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        sys.exit(1)

def main():
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    QtCore.QTimer.singleShot(4900, dialog.close) # 위젯이 떠 있는 시간 조정
    app.exec_()

while True:
    print(i)
    if __name__ == '__main__':
        main()
    time.sleep(sec)
    i += 1

'''
# req = requests.get('http://finance.daum.net/item/main.daum?code=251270') # 해당 종목 코드를 입력하세요
#req1 = requests.get('http://finance.daum.net/item/main.daum?code=035720')
#req2 = requests.get('http://finance.daum.net/item/main.daum?code=028050')
#req3 = requests.get('http://finance.daum.net/item/main.daum?code=046890')

res = view(req)
res1 = view(req1)
res2 = view(req2)
res3 = view(req3)

last_res = last_view(req)
last_res1 = last_view(req1)
last_res2 = last_view(req2)
last_res3 = last_view(req3)


last_res_re = last_res[0].replace(",", "")
last_res_re1 = last_res[1].replace(",", "")
last_res_re2 = last_res[2].replace(",", "")
last_res_re3 = last_res[3].replace(",", "")
res_re = res[0].replace(",", "")
res_re1 = res[1].replace(",", "")
res_re2 = res[2].replace(",", "")
res_re3 = res[3].replace(",", "")

lblName_sum = QLabel(str(float(res_re)-float(last_res_re))+" // " + str(float(res_re1)-float(last_res_re1) )  + " // " + str(float(res_re2)-float(last_res_re2) ) + " // "+ str(float(res_re3)- float(last_res_re3)))

'''