import csv

csvList = []

with open('text.csv', 'r') as reader:
    per = 0
    comp = 0
    foir = 0
    cnt = 0
    for line in reader:
        fields = line.split(',')
        cnt = cnt + 1
        if cnt < 30:
            print(fields)
            a = fields[0]
            b = fields[1]
            c = fields[2]
            d = fields[3]
            e = fields[4]
            per = per + int(c)
            comp = comp + int(d)
            foir = foir + int(e)
        else :
            break
    print(per)
    print(comp)
    print(foir)
        #print(len(fields))
        #for a in fields:
            #print(a)
         #   print(len(a))
