import cv2
import copy
import time

THRESHHOLD = 16;

def comparepx(px1, px2):
    return abs(int(px1[0]) - int(px2[0])) < THRESHHOLD and \
           abs(int(px1[0]) - int(px2[0])) < THRESHHOLD and \
           abs(int(px1[0]) - int(px2[0])) < THRESHHOLD

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

height, width = frame.shape[:2]

screen = copy.deepcopy(frame);

bg = cv2.imread('bg.png')

while rval:
    for x in range(width):
        for y in range(height):
            if (comparepx(frame[y,x], screen[y,x])):
                frame[y, x] = bg[y, x]

    cv2.imshow("preview", frame)
    rval, frame = vc.read()

    #time.sleep(1)
    key = cv2.waitKey(20)
    if key == 1048603: # exit on ESC
        break
    if key == 1048608:
        screen = copy.deepcopy(frame)


cv2.destroyWindow("preview")
