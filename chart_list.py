# parser.py
import requests
from bs4 import BeautifulSoup
Script_Raw = []
result = []
c = []
line_out_1=[]

f = open("C:/test/item_code_list1.txt", 'r')
cnt_line = 0
line_str = ""
while True:
    line = f.readline()
    if not line: break
    line_new = line.replace('\n', ' ')
    line_str += line_new
    cnt_line += 1
line_new_arr = line_str.split()
line_out = [[0 for col in range(2)] for row in range(cnt_line)]
cnt_line_2 = cnt_line * 2
x1 = 0
for i in range(0, int(cnt_line)) :
    #print(i)
    for j in range(0, 2):
        #print(j)
        line_out[i][j] = line_new_arr[x1]
        if x1 == cnt_line_2 :
            break
        else:
            x1 = x1 + 1
f.close()

# HTTP GET Request




def view(req, insert_code, insert_str):

    # HTML 소스 가져오기
    html = req.text
    # BeautifulSoup으로 html소스를 python객체로 변환하기
    # 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
    # 이 글에서는 Python 내장 html.parser를 이용했다.
    soup = BeautifulSoup(html, 'html.parser')



    my_titles = soup.select(
        '#contentWrap > table > tbody'
    )

    for title in my_titles:
        a = title.text.replace('\n', ' ')
        #print(a)

    b = a.split()

    if len(b) > 0:
        #print(len(b))
        j = 0


        Script_Output = [[0 for col in range(int(8))] for row in range(int(len(b)/8))]
        len_cnt = int(len(b))
        #print(len_cnt/8)
        x = 0
        #print(len_cnt)

        for i in range(0, int(len(b)/8)) :
            #print(i)
            for j in range(0, int(8)):
                #print(j)
                Script_Output[i][j] = b[x]
                if x == len_cnt-1 :
                    break
                else:
                    x = x + 1



        x = Script_Output[0][3]
        x = x.replace(",","")


        for_sum = 0
        gigan_sum = 0
        for i in range(0, int(len(b)/8)) :
            #print(Script_Output[i][3]])
            x = Script_Output[i][3]
            x = x.replace(",", "")
            for_sum = float(for_sum) +  float(x)
            #print(Script_Output[i][4])
            y = Script_Output[i][4]
            y = y.replace(",", "")
            gigan_sum = float(gigan_sum) + float(y)



        cnt = 0
        check = 0
        cnt_b = 0
        check_b = 0

        for j in range(0, int(len(b)/8)) :
            a = Script_Output[j][3]
            if '+' in  a :
                cnt += 1
            else :
                cnt = 0
            b = Script_Output[j][4]
            if cnt >= 5:
                check = 1

            if '+' in b :
                cnt_b +=1
            else :
                cnt_b = 0

            if cnt_b >= 5:
                check_b = 1




        if float(for_sum) > 0 :
            print("su1")
            if float(gigan_sum) > 0:
                print("su2")
                if check == 1 and check_b == 1:
                    f = open("C:/test/item_code_check.txt", 'a')
                    print("su3")
                    file_str = str(insert_code)+","+ str(insert_str)+ ",for," + str(for_sum) + ",gigan," + str(gigan_sum) + "\n"
                    f.write(file_str)
                    f.close()

for i in range(0, int(cnt_line)) :
    insert_code = line_out[i][0]
    insert_str = line_out[i][1]
    test = "http://finance.daum.net/item/foreign_yyyymmdd.daum?code="+insert_code
    #test = "http://finance.daum.net/item/foreign_yyyymmdd.daum?code=148020"
    req = requests.get(test)
    print(insert_code)
    view(req, insert_code, insert_str)

'''
test = "http://finance.daum.net/item/foreign_yyyymmdd.daum?code=71901A5"
req = requests.get(test)
view(req)
'''