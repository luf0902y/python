# -*- coding: utf-8 -*-
year = raw_input('Enter year:\n')
year = int(year)
if year%400 == 0:
	print '閏年'
else :
	if year%100 ==0:
		print '平年'
	elif year%4==0:
		print '閏年'
	else:
		print '平年'
