import random
t=0
ans=[]
time=1
while t<4:
	n = random.randrange(0,10)
	n = str(n)
	if n not in ans:
		ans.append(n)
		t+=1
	else:
		continue
ANS = "".join(ans)
print(ANS)
while True :
	inp = input('猜一猜')
	if inp == "STOP":
		print ('遊戲結束！\n答案是：',ANS)
		break
	else:
		try:
			int(inp)
			if len(inp) > 4 :
				print('請輸入四個數字！')
				continue
			else:
				if inp == ANS:
					print ('真厲害！答對了！')
					print ('共用了',time,'次')
					break
				else:
					A=0
					B=0
					for p in range(0,4):
						if inp[p] == ANS[p]:
							A+=1
						if inp[p] in ANS:
							B+=1
				print (A,'A',B-A,'B')
		except:
			print('請輸入四個數字！')
	time+=1
