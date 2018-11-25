from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import requests


def main():
	pir = MotionSensor(4)
	camera = PiCamera()
	start = int(get_time(0))
	stop = int(get_time(1))

	while True:
		now = datetime.now()
	
		if stop >= now.hour >= start:
			camera.resolution = (1280,720)
			pir.wait_for_motion()
			filename = 'hummingbird_{0:%Y}{0:%m}{0:%d}{0:%H}{0:%M}{0:%S}.h264'.format(now)
			print('Camera Recording')
			camera.start_recording(filename)
			pir.wait_for_no_motion()
			camera.stop_recording()
			print('Camera stopped recording')

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
