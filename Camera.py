# Use your cursor to click on anywhere on the webcam veiwer, then at the cmd, it will show the color you click and the HSV.

import cv2
import numpy as np
WINDOW_NAME= ("image")
webcam = cv2.VideoCapture(0)
Shooting_images = None

def draw_circle(event,x,y,flags,param):
	global Shooting_images
	if event == 1:
		hsv = cv2.cvtColor(Shooting_images,cv2.COLOR_BGR2HSV)
		px = hsv[y, x]
		if px[1] < 50 and px[2] > 150:
			print "white"
		elif 22.5 > px[0] > 7.5:
			print "orange"
		elif 45 > px[0] > 22.5:
			print "yellow"
		elif 85 >= px[0] >= 45:
			print "green"
		elif 135 > px[0] > 85:
			print "blue"
		elif 7.5 > px[0]:
			print "red"
		elif px[0] > 135:
			print "red"
		print px
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

# Create a black image, a window and bind the function to window

#Read Shooting images
while 1:
	ret, Shooting_images = webcam.read()
	cv2.imshow(WINDOW_NAME,Shooting_images)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
#press ESC leave
cv2.destroyAllWindows()