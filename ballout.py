# -*- coding: utf-8 -*-
"""
因為考慮到中文編碼的問題，所以用for loop寫
也可以把名字存到list裡面，然後隨機取一個位置
"""
import random
filename ='namelist.txt'
fh = open(filename)
num = random.randrange(0,3)  #three people
t=0
for line in fh:
	if t<num:
		t+=1
		continue 
	else:
		print '被抽中的人是：',line.rstrip('\n')
		t+=1
		break
