# Use your cursor to click on anywhere on the webcam veiwer, then at the cmd, it will show the color you click and the HSV.

import cv2
import numpy as np
WINDOW_NAME= ("image")
webcam = cv2.VideoCapture(2)
Shooting_images = None
color = ""
colornum = 0
done = False
fir_done = False
colormap = []
colorrange = [0, 0, 0, 0, 0, 0]

def color_detect(event,x,y,flags,param):
	global Shooting_images
	global color
	global colornum
	global done
	global colormap
	global colorrange
	global webcam
	global fir_done
	if event == 1:
		hsv = cv2.cvtColor(Shooting_images,cv2.COLOR_BGR2HSV)
		px = hsv[y, x]
		if colornum < 6:
			if colornum == 0:
				colormap.append(px[0])
				print "red", colormap[0]
			elif colornum == 1:
				colormap.append(px[0])
				print "orange", colormap[1]
			elif colornum == 2:
				colormap.append(px[0])
				print "yellow", colormap[2]
			elif colornum == 3:
				colormap.append(px[0])
				print "green", colormap[3]
			elif colornum == 4:
				colormap.append(px[0])
				print "blue", colormap[4]
			elif colornum == 5:
				colormap.append(px[1])
				print "white", colormap[5]
				if colormap[0] > 100:
					colorrange[0] = (colormap[0] + colormap[1] - 179) / 2
					if colormap[0] < 0:
						colormap[0] += 180
					colorrange[4] = colormap[4] / 2 + colormap[0] / 2
				else:
					colorrange[0] = colormap[0] / 2 + colormap[1] / 2
					if (colormap[0] + colormap[4] + 179) / 2 > 179:
						colorrange[4] = (colormap[0] + colormap[4] + 179) / 2 - 179
					else:
						colorrange[4] = (colormap[0] + colormap[4] + 179) / 2
				colorrange[1] = (colormap[1] + colormap[2]) / 2
				colorrange[2] = (colormap[2] + colormap[3]) / 2
				colorrange[3] = (colormap[3] + colormap[4]) / 2
				colorrange[5] = colormap[5] + 30
				print colorrange
			colornum += 1
		elif colornum < 60:
			if colornum == 32:
				fir_done = True
			if px[1] < colorrange[5] and px[2] > 100:
				color += "W"
			elif colorrange[1] > px[0] >= colorrange[0]:
				color += "O"
			elif colorrange[2] > px[0] >= colorrange[1]:
				color += "Y"
			elif colorrange[3] > px[0] >= colorrange[2]:
				color += "G"
			elif colorrange[4] > px[0] >= colorrange[3]:
				color += "B"
			else:
				color += "R"
			print px
			print color
			colornum += 1
		elif colornum >= 60:
			print "done"
			done = True
		print len(color)
def open():
	global Shooting_images
	global webcam
	global cv2
	img = np.zeros((512,512,3), np.uint8)
	cv2.namedWindow('image')
	cv2.setMouseCallback('image',color_detect)
	print "Correction (Red, Orange, Yellow, Green, White):"
	#Read Shooting images
	while fir_done != True:
		ret, Shooting_images = webcam.read()
		cv2.imshow('image',Shooting_images)
		k = cv2.waitKey(5) & 0xFF
		if k == 27:
			break

	# cv2.destroyAllWindows()
	# img = np.zeros((512,512,3), np.uint8)
	# cv2.namedWindow('image2')
	# cv2.setMouseCallback('image2',color_detect)
	webcam.release()
	webcam = cv2.VideoCapture(1)
	while done != True:
		ret, Shooting_images = webcam.read()
		cv2.imshow('image',Shooting_images)
		k = cv2.waitKey(5) & 0xFF
		if k == 27:
			break
	#press ESC leave
	cv2.destroyAllWindows()
	result = arrange(color)
	return result

def arrange(c):
	res = c[:9] + c[9:12] + c[18:21] + c[27:30] + c[36:39] + c[12:15] + c[21:24] + c[30:33] + c[39:42] + c[15:18] + c[24:27] + c[33:36] + c[42:45] + c[45:]
	print res
	return res

# Create a black image, a window and bind the function to window
if __name__ == '__main__':
	c = open()