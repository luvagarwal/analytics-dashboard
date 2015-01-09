from datetime import datetime
from datetime import timedelta

	
def getxtime(time,num,unit):
	item = time
	lis=[]
	lis.append(item)
	for i in xrange(num-1):
		if unit=='hour':
			item = item - timedelta(0,3600)
		if unit=='day':
			item = item - timedelta(1)
		if unit=='month':
			if item.month!=1:
				item = datetime(item.year,item.month-1,item.day,item.hour,item.second)
			else:
				item = datetime(item.year,12,item.day,item.hour,item.second)
		if unit=='year':
			item=datetime(item.year-1,item.month,item.day,item.hour,item.second)  	
		lis.append(item)
	print lis
	

