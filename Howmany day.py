import math
from datetime import date
from datetime import datetime
while (1) :
    n = int(input("ENTER : "))
    mybirth = date(2006, 10, 29) #ใส่วันเกิดตัวเอง
    mydaeth = date(2086, 10, 29) #ใส่วันที่จะมีชีวิตอยู่วันสุดท้าย
    total = mydaeth - mybirth
    if n == 1 : #function ใส่ 1 คิดของวันนี้
        now = date.today() #เวลา ณ ปัจจุบันหรือที่เราเซ็ทค่าไว้ date(year,month,day)
    elif n == 2 :
        d = int(input("input day : "))
        m = int(input("input month : "))
        y = int(input("input year : "))
        now = date(y,m,d)
    elif n == 3 :
        break
    timetonow = now - mybirth

    percent = (timetonow / total)*100

    minall = (percent / 100) * 24 * 60

    hour = minall / 60
    hr = int(hour)
    minute = minall % 60
    min = round(minute)

    if min == 60 :
        min = 0
        hr = hr + 1

    if min < 10 : 
        min = (f'{min:02}')

    print(hr,':',min,"น.")
    print(minall)
    #print(percent)