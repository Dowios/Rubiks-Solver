import cv2
import numpy as np
from collections import Counter
WINDOW_NAME= ("image")
WINDOW_NAME2= ("intro")
webcam = cv2.VideoCapture(0)
Shooting_images = None
color_one = []
color_two = []
color = ""
# xy_one = [[None] * 2 for i in range(27)]
# xy_two = [[None] * 2 for i in range(27)]
xy_one = [[177, 128], [235, 102], [260, 74], [242, 154], [316, 123], [357, 87], [322, 171], [379, 137], [425, 106], [157, 186], [222, 213], [299, 238], [361, 227], [413, 190], [457, 159], [173, 256], [233, 289], [298, 315], [369, 303], [413, 267], [454, 225], [160, 299], [245, 359], [306, 382], [366, 374], [409, 332], [434, 314]]
xy_two = [[153, 183], [179, 169], [215, 136], [270, 127], [331, 154], [398, 207], [135, 273], [168, 220], [206, 199], [270, 196], [341, 227], [401, 253], [127, 330], [156, 305], [197, 270], [259, 271], [330, 293], [403, 321], [301, 407], [210, 391], [159, 378], [324, 391], [270, 378], [187, 351], [377, 370], [310, 351], [223, 319]]
xy_one_index = 0
xy_two_index = 0
colorrange = [0, 0, 0, 0, 0, 0]
cam_index = 0
function = ["getXY", "getHSV", "getColor", "createArray", "applyArray", "generateColor"]
func = "getXY"
def open():
	global Shooting_images
	global webcam
	global cv2
	global func
	global color
	img = np.zeros((512,512,3), np.uint8)
	cv2.namedWindow('image')
	cv2.setMouseCallback('image', mouse_down)
	intro = cv2.imread('1.png',0)
	cv2.imshow('intro',intro)
	cv2.resizeWindow('intro', 200, 200)
	#Read Shooting images
	while True:
		ret, Shooting_images = webcam.read()
		cv2.imshow('image',Shooting_images)
		k = cv2.waitKey(5) & 0xFF
		if k == 27:
			break
		if k == 9:
			change_camera()
		if k == 49:
			func = function[0]
			print "getXY"
		if k == 50:
			func = function[1]
			print "getHSV"
		if k == 51:
			func = function[2]
			print "getColor"
		if k == 97:
			func = function[3]
			print "createArray"
		if k == 13:
			print "applyArray"
			print apply_xy_array()
		if k == 99:
			print "generateColor"
			color = generate_color()
			print color
		if k == 100:
			break

	cv2.destroyAllWindows()
	return color

def change_camera():
	global Shooting_images
	global webcam
	global cv2
	global cam_index
	cam_index = 2 - cam_index
	webcam.release()
	webcam = cv2.VideoCapture(cam_index)

def mouse_down(event,x,y,flags,param):
	global Shooting_images
	global color
	global colorrange
	global webcam
	if event == 1:
		if func == "getXY":
			print x, y
		if func == "getHSV":
			print color_get(x, y)
		if func == "getColor":
			print color_differentiate(x, y)
		if func == "createArray":
			print create_xy_array(x, y)
def color_get(x, y):
	hsv = cv2.cvtColor(Shooting_images,cv2.COLOR_BGR2HSV)
	px = hsv[y, x]
	return px
def create_xy_array(x, y):
	global xy_one_index
	global xy_two_index
	if cam_index == 0:
		xy_one[xy_one_index] = [x, y]
		if xy_one_index > 25:
			xy_one_index = 0
		else:	
			xy_one_index += 1
		return xy_one
	else:
		xy_two[xy_two_index] = [x, y]
		if xy_two_index > 25:
			xy_two_index = 0
		else:	
			xy_two_index += 1
		return xy_two

def apply_xy_array():
	if cam_index == 0:
		for xy in xy_one:
			color_one.append(aver(xy[0], xy[1]))
		return color_one
	else:
		for xy in xy_two:
			color_two.append(aver(xy[0], xy[1]))
		return color_two

# def color_detect():

def aver(x, y):
	mat = []
	mat.append(color_differentiate(x, y))
	mat.append(color_differentiate(x + 1, y))
	mat.append(color_differentiate(x - 1, y))
	mat.append(color_differentiate(x, y))
	mat.append(color_differentiate(x + 1, y))
	mat.append(color_differentiate(x - 1, y))
	mat.append(color_differentiate(x, y - 1))
	mat.append(color_differentiate(x + 1, y - 1))
	mat.append(color_differentiate(x - 1, y - 1))
	return Counter(mat).most_common(1)[0]

def color_differentiate(x, y):
	px = color_get(x, y)
	dis = int(px[2]) - int(px[1])
	print px
	if px[1] < 110 and dis > 20:
		return "W"
	elif 58 > px[0] >= 20:
		return "Y"
	elif 90 > px[0] >= 58:
		return "G"
	elif 160 > px[0] >= 90:
		return "B"
	else:
		if 5 < px[0] <= 160:
			return "O"
		elif px[0] > 160 or px[0] < 3 :
			return "R"
		else:
			if 100 > px[2]:
				return "R"
			else:
				return "O"

def generate_color():
	color_one[4] = "Y"
	color_one[16] = "B"
	color_one[19] = "R"
	color_two[7] = "G"
	color_two[10] = "O"
	color_two[22] = "W"
	one = ''.join(color_one)
	two = ''.join(color_two)
	c = one[:15] + two[:6] + one[15:21] + two[6:12] + one[21:] + two[12:]
	return c


# Create a black image, a window and bind the function to window
if __name__ == '__main__':
	c = open()