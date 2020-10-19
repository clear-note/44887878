
import pyautogui
import time
import os
import datetime
from pygame import mixer
import keyboard

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


def discard(num) :
    
    
        replace()
    
   

        mouseLoc =  pyautogui.locateOnScreen('button/scroll.png',confidence= 0.9)
        pyautogui.moveTo(mouseLoc) 

        print('start monster kill ' + str(num)   ) 
        

        # 최근 소환된 몬스터로 스크롤 
        for i in range(25) :
          pyautogui.click()

        try:

            # 삭제 num번 반복 
            for i in range(num):
                kill2 = pyautogui.locateOnScreen('button/kill.png',confidence= 0.9)
                kill2 = list(kill2) 
                kill2 = kill2[:2]
                kill2 = tuple(kill2)

                # 방출 메뉴 소환
                pyautogui.rightClick(kill2)
                pyautogui.rightClick(kill2)
                pyautogui.rightClick(kill2)
                

                # 방출 메뉴 버튼
                discard = pyautogui.locateOnScreen('button/discard.png',confidence= 0.9)
                pyautogui.click(discard)
                
                # 방출 확인
                mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.9)
                pyautogui.click(mixButton2)

                # 확인 
                time.sleep(0.1)
                enter3 = pyautogui.locateOnScreen('button/enter3.png',confidence= 0.95)
                pyautogui.click(enter3)
                pyautogui.click(enter3)
                

                time.sleep(0.3)
                
                # 한칸 스크롤
                pull = pyautogui.locateOnScreen('button/pull.png',confidence= 0.95)
                pyautogui.click(pull)

                time.sleep(0.2)


            

        except :
            print('image found faild')
            replace()
        
  
  
        return 0



def scrollmouse(num):
    mouseLoc =  pyautogui.locateOnScreen('button/scroll.png',confidence= 0.9)
    pyautogui.moveTo(mouseLoc) 
    
    for i in range(num) :
      pyautogui.click()
    
    




def replace():

    #mouseLoc =  pyautogui.locateOnScreen('place/moveTo.png',confidence= 0.9)
    pyautogui.moveTo(1,1) 
    

## 현재 위치 파악
def nowPlace():
    myroom = pyautogui.locateOnScreen('place/myroom1.png',confidence= 0.9)
    otherroom = pyautogui.locateOnScreen('place/otherroom1.png',confidence= 0.9)
    shop= pyautogui.locateOnScreen('place/shop.png',confidence= 0.9)
    
    if myroom :
     print('now place is myroom')
     return 1

    if otherroom :
     print('now place is ohterroom')
     return 2

    if shop :
     pyautogui.click(shop)
     print('now place is shop')

     return 3

    
    return -1 
    


# 조합식 1
def mix(num, mixcount):
   # 타깃 몬스터 서치 
   mix1_2 =  pyautogui.locateOnScreen('Rec' + str(num)+ '/mix2.png',confidence= 0.995)
   # 타깃 몬스터가 없으면 함수 종료
   if mix1_2 is None:
       print ('target '+ str(num) +  ' is not exist..') 
       return 0
   else:
       print ('target '+ str(num) +  ' found, start mix') 

   time.sleep(0.5)

   # 타깃 몬스터  우 클릭
   pyautogui.rightClick(mix1_2)
   pyautogui.rightClick(mix1_2)
   pyautogui.rightClick(mix1_2)

   # 메뉴 버튼 서치
   mixButton = pyautogui.locateOnScreen('button/mixButton.png',confidence= 0.9)
   pyautogui.click(mixButton)
   
   # 조합 시 등급과 레벨이
   mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.9)
   pyautogui.click(mixButton2)

   # 내 몬스터 클릭

   mix1_1 =  pyautogui.locateOnScreen('Rec' + str(num)+ '/mix1.png',confidence= 0.9)
   pyautogui.click(mix1_1)


   # 조합하기 클릭 
   mixButton3 = pyautogui.locateOnScreen('button/button3.png',confidence= 0.95)
   pyautogui.click(mixButton3)
    
   # 특별 조합식 조합을 시작합니다
   mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.9)
   pyautogui.click(mixButton2)

   # 조합에 5000 와르가 소모됩니다
   mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.9)
   pyautogui.click(mixButton2)

   time.sleep(1)

   # 여유 공간이 없을경우 집으로 직행
   if pyautogui.locateOnScreen('button/notspace.png',confidence= 0.95) and pyautogui.locateOnScreen('place/otherroom1.png',confidence= 0.95) :

     mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.9)
     pyautogui.click(mixButton2)

     gohome = pyautogui.locateOnScreen('button/gohome.png',confidence= 0.9)
     pyautogui.click(gohome)
     
     

     return 2

    
   # 조합 대기시간
   time.sleep(2.4)
   
   #조합 로그 출력
   
   print('target ' + str(num) +' mix count: ' + str(mixcount))


   # 확인
   enter = pyautogui.locateOnScreen('button/enter.png',confidence= 0.95)
   
   # 스페셜이 나왔다면 정지
   if (pyautogui.locateOnScreen('button/enter2.png',confidence= 0.95)) :

       mixer.init()
       mixer.music.load('alarm.mp3')
       mixer.music.play()
       time.sleep(50000)
       mixer.music.stop()

    
       return -1
   
   pyautogui.click(enter)
   pyautogui.click(enter)

   
   time.sleep(0.2)

   # 확인
   enter2 = pyautogui.locateOnScreen('button/enter2.png',confidence= 0.95)
   pyautogui.click(enter2)
   pyautogui.click(enter2)

   time.sleep(0.2)

   # 조합된 몬스터는 당신의 농장으로
   mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.95)
   pyautogui.click(mixButton2)
   
   time.sleep(0.07)
   
   # 타깃 몬스터가 남아있다면?
   mix1_2 =  pyautogui.locateOnScreen('Rec' + str(num)+ '/mix2.png',confidence= 0.99)
   # 타깃 몬스터가 없으면 함수 종료
   if mix1_2 :
       print ('one more target '+ str(num) +  '  found')
       mix(num, mixcount +1 ) 
       return 0



   return 1


def visit():
   # 랜덤방문 버튼 클릭
   visit = pyautogui.locateOnScreen('button/visit.png',confidence= 0.9)
   pyautogui.click(visit)
   time.sleep(0.1)
   
   # 농장에 방문합니다
   mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.9)
   pyautogui.click(mixButton2)
   time.sleep(2)



def visitMyroomTo():
   

   # 상점에 방문합니다
   shop = pyautogui.locateOnScreen('button/shop.png',confidence= 0.9)
   pyautogui.click(shop)
   
   # 랜덤방문 버튼 클릭
   visit = pyautogui.locateOnScreen('button/door.png',confidence= 0.9)
   pyautogui.click(visit)
  
   
   # 농장에 방문합니다
   door2 = pyautogui.locateOnScreen('button/door2.png',confidence= 0.9)
   pyautogui.click(door2)
   

   #확인
   mixButton2 = pyautogui.locateOnScreen('button/button2.png',confidence= 0.9)
   pyautogui.click(mixButton2)
   
   
   
   time.sleep(2)

   # 현 위치가 아직도 샵이라면 재실행
   if nowPlace() is 3 :
       visitMyroomTo()

     

def OtherToHome():
     if pyautogui.locateOnScreen('button/fulled.png',confidence= 0.98) and   pyautogui.locateOnScreen('place/otherroom1.png',confidence= 0.95)   :
        gohome = pyautogui.locateOnScreen('button/gohome.png',confidence= 0.9)
        
        pyautogui.click(gohome)


        time.sleep(4)
        
        return 1

     else :
        return 0  

def exception():
    if pyautogui.locateOnScreen('button/nope1.png',confidence= 0.97) :
        nope2 = pyautogui.locateOnScreen('button/nope2.png',confidence= 0.97)
        

        pyautogui.click(nope2)



## 메인 프로그램 


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




# 프로그램 속도
speed = 1


try:
    config = open("config.txt", 'r+')
    lines = config.readlines()
    
    rec1 = str(lines[1].rstrip('\n'))
    mixcount1 = int(lines[2].rstrip('\n'))
    rec2 = str(lines[5].rstrip('\n'))
    mixcount2 = int(lines[6].rstrip('\n'))
    rec3 = str(lines[9].rstrip('\n'))
    mixcount3 = int(lines[10].rstrip('\n'))
    rec4 = str(lines[13].rstrip('\n'))
    mixcount4 = int(lines[14].rstrip('\n'))
    rec5 = str(lines[17].rstrip('\n'))
    mixcount5 = int(lines[18].rstrip('\n'))
    rec6 = str(lines[21].rstrip('\n'))
    mixcount6 = int(lines[22].rstrip('\n'))
    rec7 = str(lines[25].rstrip('\n'))
    mixcount7 = int(lines[26].rstrip('\n'))

    #버릴 몬스터 수
    dis = int(lines[33].rstrip('\n'))
except :
    print('config file error')
    time.sleep(40000)






while 1 :
     
    # 현재 위치 파악
    np = nowPlace()

    ## 현재 위치가 남의 농장일 경우
    if np is 2 :
        
        for i in range(4):


            GoHome = OtherToHome()                  
            if GoHome == 1 :
                    break
            

            # 키보드 이벤트 캐치    
            if keyboard.is_pressed('q'):
                print('Quit')
                time.sleep(10000)
                break


            if rec1 == "run" :         
                mix1 =  mix(1, mixcount1)

                
                # 로그 출력기능
                if mix1 is 1:
                  GoHome = OtherToHome()  
                  mixcount1 = mixcount1 + 1

                  if GoHome == 1 :
                   break
           
            #키보드 이벤트 캐치
            if keyboard.is_pressed('q'):
                print('Quit')
                time.sleep(10000)
                break

            if rec2 == "run" :         
                mix2 =  mix(2, mixcount2)

                # 로그 출력기능
                if mix2 is 1:
                  GoHome = OtherToHome()  
                  mixcount2 = mixcount2 + 1
                  
                  if GoHome == 1 :
                   break

            # 키보드 이벤트 캐치    
            if keyboard.is_pressed('q'):
                print('Quit')
                time.sleep(10000)
                break


            if rec3 == "run" :         
                mix3 =  mix(3, mixcount3)
                # 로그 출력기능
                if mix3 is 1:
                  GoHome = OtherToHome()  
                  mixcount3 = mixcount3 + 1
                  
                  if GoHome == 1 :
                   break

            # 키보드 이벤트 캐치    
            if keyboard.is_pressed('q'):
                print('Quit')
                time.sleep(10000)
                break


            if rec4 == "run" :         
                mix4 =  mix(4, mixcount4)
                # 로그 출력기능
                if mix4 is 1:
                  GoHome = OtherToHome()  
                  mixcount4 = mixcount4 + 1
                  
                  if GoHome == 1 :
                   break
           
            # 키보드 이벤트 캐치    
            if keyboard.is_pressed('q'):
                print('Quit')
                time.sleep(10000)
                break


            if rec5 == "run" :         
                mix5 =  mix(5, mixcount5)
                # 로그 출력기능
                if mix5 is 1:
                  GoHome = OtherToHome()  
                  mixcount5 = mixcount5 + 1
                  
                  if GoHome == 1 :
                   break 

            # 키보드 이벤트 캐치    
            if keyboard.is_pressed('q'):
                print('Quit')
                time.sleep(10000)
                break

            if rec6 == "run" :         
                mix6 =  mix(6, mixcount6)
                # 로그 출력기능
                if mix6 is 1:
                  GoHome = OtherToHome()  
                  mixcount6 = mixcount6 + 1
                  
                  if GoHome == 1 :
                   break
            
            if rec7 == "run" :         
                mix7 =  mix(7, mixcount7)
                # 로그 출력기능
                if mix7 is 1:
                  GoHome = OtherToHome()  
                  mixcount7 = mixcount7 + 1
                  
                  if GoHome == 1 :
                   break
            


            if i < 4:
             scrollmouse(7)
            

       
        #농장 꽉 차있다면 시간낭비 말고 내 농장 직행
                           
        # 그렇지 않다면 랜덤방문 시전
        
        else: 
            exception()
            visit()
        
    ## 현재 위치가 내 농장일 경우
    if np is 1 :
          
          exception()
           # 키보드 이벤트 캐치 
          if keyboard.is_pressed('q'):
                print('Quit')
                time.sleep(10000)
                break
          
          discard(dis)
      
          time.sleep(2)
            

        ## 랜덤방문 이용
          if keyboard.is_pressed('q'):
                print('Quit')
                time.sleep(10000)
                break
          visitMyroomTo()
