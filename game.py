# -*- coding: utf-8 -*-
import random
import os
print ('來猜猜數字')
ST = []
t=0
while t<4: #先設定題目四個數字，且不能重複
	num = str(random.randrange(0,10))
	if not (num in ST):
		ST.append(num)
		t+=1
time=1
while True:
	inp = input('輸入四個數字\t')
	A=0
	B=0
	if "STOP" in inp:  #輸入"STOP"則放棄，公布答案
		print('停止遊戲，答案是：')
		print ("".join(str(n) for n in ST))
		break
	else:
		try:
			int(inp)  #確保輸入數字
			if "".join(str(n) for n in ST) == inp:  #當和答案輸入相同時，就對了！
				print ('太棒了 答對囉！')
				print ('總共花了',time,'次')
				break
			elif len(inp) != 4:	#確保輸入的是「四個」數字
				print ('確實打四個數字！')
			else:
				for num in range(4):  #顯示幾Ａ幾Ｂ
					if ST[num] == inp[num]:	 #數字對，位置也對
						A+=1
					if inp[num] in ST: #輸入的數字有在答案裡面
						B+=1
				print (A,'A',B-A,'b')  #數字對，位置錯的部分是(B-A)
			time+=1
		except:
			print('別亂打')
