temp=input("不妨猜一下我现在心里想的是哪个数字:")
guess=int(temp)
if guess==8:
    print("yes")
    print("but there has no price")
    print("game over")
else:
    if guess < 8:
        print("小了")
    else:    
        print("大了")

print("game over")
        