import cv2
import numpy as np
WINDOW_NAME= ("image")
WINDOW_NAME2= ("intro")
webcam = cv2.VideoCapture(0)
Shooting_images = None
color_one = []
color_two = []
color = ""
# xy_one = [[None] * 2 for i in range(27)]
# xy_two = [[None] * 2 for i in range(27)]
xy_one = [[236, 85], [288, 56], [305, 29], [304, 112], [348, 72], [412, 37], [382, 141], [432, 88], [484, 60], [214, 145], [280, 174], [364, 204], [425, 190], [475, 137], [521, 113], [228, 215], [289, 239], [356, 273], [425, 262], [469, 221], [508, 179], [216, 260], [290, 312], [356, 338], [420, 333], [465, 285], [495, 265]]
xy_two = [[184, 118], [207, 104], [243, 60], [298, 55], [366, 86], [438, 138], [165, 212], [200, 158], [237, 128], [296, 124], [380, 159], [428, 184], [158, 269], [189, 236], [228, 200], [279, 193], [364, 228], [428, 244], [332, 348], [244, 328], [196, 317], [360, 323], [295, 313], [223, 281], [412, 297], [334, 281], [265, 248]]
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
			color_one.append(color_differentiate(xy[0], xy[1]))
		return color_one
	else:
		for xy in xy_two:
			color_two.append(color_differentiate(xy[0], xy[1]))
		return color_two

# def color_detect():

def color_differentiate(x, y):
	px = color_get(x, y)
	print px
	if px[1] < 100:
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