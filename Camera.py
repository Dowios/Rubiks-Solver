# Use your cursor to click on anywhere on the webcam veiwer, then at the cmd, it will show the color you click and the HSV.

import cv2
import numpy as np
WINDOW_NAME= ("image")
webcam = cv2.VideoCapture(1)
Shooting_images = None
color = ""
colornum = 0
done = False
colormap = []
colorrange = [0, 0, 0, 0, 0, 0]
cam_index = 1

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
            correction(colornum, px)
        elif colornum < 60:
            if px[1] < 80:
                color += "W"
            elif colorrange[1] > px[0] >= colorrange[0]:
                color += "Y"
            elif colorrange[2] > px[0] >= colorrange[1]:
                color += "G"
            elif colorrange[3] > px[0] >= colorrange[2]:
                color += "B"
            else:
                if 100 > px[2]:
                    color += "R"
                else:
                    if 210 > px[1]:
                        color += "R"
                    else:
                        color += "O"
            print px
            print "[%s, %s]" % (x, y)
            print color
        elif colornum >= 60:
            print "done"
            done = True
        colornum += 1
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
    while done != True:
        ret, Shooting_images = webcam.read()
        cv2.imshow('image',Shooting_images)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
        if k == 9:
            change_camera()
    cv2.destroyAllWindows()
    result = arrange(color)
    return result

def correction(color_n, px):
    global colormap
    if color_n == 0:
        colormap.append(px[2])
        print "red", colormap[0]
    elif color_n == 1:
        colormap.append(px[0])
        colormap.append(px[2])
        print "orange", colormap[2], colormap[1]
    elif color_n == 2:
        colormap.append(px[0])
        print "yellow", colormap[3]
    elif color_n == 3:
        colormap.append(px[0])
        print "green", colormap[4]
    elif color_n == 4:
        colormap.append(px[0])
        print "blue", colormap[5]
    elif color_n == 5:
        colormap.append(px[1])
        print "white", colormap[6]
        mapping()

def mapping():
    global colormap
    global colorrange
    if colormap[1] > 100:
        colorrange[0] = (colormap[1] + colormap[3] - 179) / 2
        colorrange[3] = colormap[5] / 2 + colormap[1] / 2
    else:
        colorrange[0] = colormap[1] / 2 + colormap[3] / 2
        colorrange[3] = colormap[1] / 2 + 90 + colormap[5] / 2
    colorrange[1] = (colormap[3] + colormap[4]) / 2
    colorrange[2] = (colormap[4] + colormap[5]) / 2
    colorrange[4] = colormap[0] / 2 + colormap[2] / 2
    colorrange[5] = colormap[6] + 30
    print colorrange


def arrange(c):
    res = c[:9] + c[9:12] + c[18:21] + c[27:30] + c[36:39] + c[12:15] + c[21:24] + c[30:33] + c[39:42] + c[15:18] + c[24:27] + c[33:36] + c[42:45] + c[45:]
    print res
    return res

def change_camera():
    global Shooting_images
    global webcam
    global cv2
    global cam_index
    cam_index = 1 - cam_index
    webcam.release()
    webcam = cv2.VideoCapture(cam_index)

# Create a black image, a window and bind the function to window
if __name__ == '__main__':
    c = open()