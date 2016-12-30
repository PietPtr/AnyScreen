import cv2
import copy
import time

THRESHHOLD = 16;

# Compares two pixels. If for all color values the difference
# between color values is less than the THRESHHOLD, the pixels are
# deemed similar.
def comparepx(px1, px2):
    return abs(int(px1[0]) - int(px2[0])) < THRESHHOLD and \
           abs(int(px1[0]) - int(px2[0])) < THRESHHOLD and \
           abs(int(px1[0]) - int(px2[0])) < THRESHHOLD

# Create a new window to show images in and start the VideoCapture.
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

# Store the height and width of the webcam input
height, width = frame.shape[:2]

# This variable stores the "greenscreen"
screen = copy.deepcopy(frame);

# This stores what the greenscreen should be replaced with
bg = cv2.imread('bg.png')

# Keep updating while there is data from the camera
while rval:
    # for all pixels in the image that comes in from the camera ...
    for x in range(width):
        for y in range(height):
            # check if they are similar to greenscreen value ...
            if (comparepx(frame[y,x], screen[y,x])):
                # and if they are, set them to the new background image
                frame[y, x] = bg[y, x]

    # Show the image on screen
    cv2.imshow("preview", frame)

    # Read the next image from the camera
    rval, frame = vc.read()

    # Wait for user input
    key = cv2.waitKey(20)
    # exit on pressing escape
    if key == 1048603:
        break
    # press space to use a new "greenscreen" image
    if key == 1048608:
        screen = copy.deepcopy(frame)


cv2.destroyWindow("preview")
