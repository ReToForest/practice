import random
import time

def random_number():
     random.seed(int(time.time()))
     return random.randint(1, 100)

answer =int(input ("答案："))
guess = random_number()
cnt = 0

while True:
    print(f"我猜是：{guess}")
    cnt += 1
    if guess<answer:
         print("小了")
         guess=(guess+answer)//2+1
    elif guess>answer:
         print("大了")
         guess=(guess+answer)//2
    else:     
         print("bingo")
         print(f"最终一共猜了{cnt}次")  
         print("game over") 
         break
