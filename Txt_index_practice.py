

### 뭐부터 할까?
### 파이선 
## 마이마이 연습 
## 사쿠라모유
## 노래 찾아서 듣기
## 웹 개발 시작
## 사쿠라장 시청
## 양파가루 구입 요거톡 구입
##원순



import pyautogui
import time
import os
import datetime
from pygame import mixer
import sys, fileinput


def lineChange( Replace_What , New_Value ) :

    try:
        File = r"config.txt"        
        for Line in fileinput.input(File, inplace=True):  #:- Entire Line Replace
            if Replace_What in Line:
                Line = Line.replace(Line, Replace_What + '=' + str(New_Value) + '\n')
            sys.stdout.write(Line)

        print('config file changed.')    
    except :
        print('failed to read config file')



def lineReturn(Replace_What):
            
    try:   
        f = open("config.txt", 'r')
        lines = f.readlines()
        for line in lines:
        #     item = line.split("=")
            if line.find(Replace_What) == 0:  
        #     index = item[item.index(Replace_What)+1]
                result = line.lstrip(Replace_What)
                result = result.lstrip('=')
                result = result.rstrip('\n')
                result = int(result)
        
        
        f.close()
        return result
    except:
        print("config load error")   



   






da = "date"
New_Value = str(time.strftime('%d', time.localtime(time.time() )) )


i = lineReturn(da)
today =  int(time.strftime('%d', time.localtime(time.time() ))  )

print(today)

# 날짜가 바뀌었다면 날짜와 인덱스 초기화
if not(i == today):
    index = "index"
    
    lineChange( index , 0 )
    lineChange( da , today )

    print("init index..")


print(lineReturn("index"))

# 인덱스 순서대로 텍스트 처리 작업
# 농장 한줄에 방문 시 인덱스 추가   


