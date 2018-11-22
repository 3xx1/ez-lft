import cv2

a = [["sho", "koji", "kaz"],[0, 1, 2]]
print a[0][1]

img = cv2.imread('images/lenna.png') # lenna.png is 220x220
xPos = 40
yPos = 10
print 'rgb at (' + str(xPos) + ', ' + str(yPos) + ') - ' + str(img[xPos][yPos][0]) + ', ' + str(img[xPos][yPos][1]) + ', ' + str(img[xPos][yPos][2])
