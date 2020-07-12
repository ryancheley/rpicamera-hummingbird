import os
import time
import requests 
from datetime import datetime 

TIMEBETWEEN = 60

def main(): 
	start = int(get_time(0)) 
	stop = int(get_time(1)) 
	while True:
		now = datetime.now()
		print('Starting Pictures')
		if stop >= now.hour >= start: 
			filename = 'wildlife_{0:%Y}{0:%m}{0:%d}{0:%H}{0:%M}{0:%S}'.format(now)
			print(filename)
			os.system("raspistill -o %s.jpg"%(filename))
			time.sleep(TIMEBETWEEN - 6)
 
def get_time(i): 
	filepath = '/home/pi/Documents/python_projects/data.txt' 
	with open(filepath) as fp: 
		line = fp.readline() 
		cnt = 1 
		data = [] 
		while line: 
			data.append(line.strip()) 
			line = fp.readline() 
			cnt += 1 
		return data[i] 

if __name__ == '__main__': 
	main()
