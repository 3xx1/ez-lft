import matplotlib.pyplot as plt
import numpy as np
#from scipy import ndimage
import cv2
from matplotlib.widgets  import RectangleSelector
import matplotlib

from imutils import contours
import imutils


# Required information for each scanned image
Distance_control_test = 85
Distance_control_background = 105

# Upload and resize the scanned image
I_raw = cv2.imread('images/LFT_example.png')
I_resize = cv2.resize(I_raw, (638, 292))

#blur to extract edge
I = cv2.blur(I_resize, (5, 10))

# HSV to extract edge
hsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)

# thresholds to detect test lines as edge extraction by Canny
lower_red = np.array([0,27,100])
upper_red = np.array([5,100,180])

mask = cv2.inRange(hsv, lower_red, upper_red)
#res = cv2.bitwise_and(I,I, mask= mask)

# edges by the threshold
edges = cv2.Canny(mask,100,200)
copy = edges.copy()

# Find contours for detected portion of the image
###im2, cnts, hierarchy = cv2.findContours(copy, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
###cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:25] # get largest 25 contour areas
rects = []
cnts = cv2.findContours(copy, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# sort number for each rectangle from left to right
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
cnts = contours.sort_contours(cnts)[0]

for (i, c) in enumerate(cnts):
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    x, y, w, h = cv2.boundingRect(approx)
    if w >= 41 and h >= 7:
        # if width and height are enough
        # create rectangle for bounding
        rect = (x, y, w, h)
        rects.append(rect)
        cv2.rectangle(I, (x, y), (x+w, y+h), (255, 0, 0), 1)
        # add number for each rectangle
        cv2.putText(I, "#{}".format(i + 1), (x, y - 15),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1);




cv2.imshow('Edges',edges)
#cv2.imshow('res',res)
#cv2.imshow('mask',mask)


plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.show()





# Select ROI_control
#fromCenter = False
#ROI_control = cv2.selectROI(I, fromCenter)

# Crop image
#ROI_control_crop = I[int(ROI_control[1]):int(ROI_control[1]+ROI_control[3]), int(ROI_control[0]):int(ROI_control[0]+ROI_control[2])]
#ROI_test_crop = I[int(ROI_control[1])+Distance_control_test:int(ROI_control[1]+ROI_control[3]+Distance_control_test), int(ROI_control[0]):int(ROI_control[0]+ROI_control[2])]
#ROI_background_crop = I[int(ROI_control[1])+Distance_control_background:int(ROI_control[1]+ROI_control[3]+Distance_control_background), int(ROI_control[0]):int(ROI_control[0]+ROI_control[2])]


#b_ROI_control_crop = ROI_control_crop.copy()
## set green and red channels to 0
#b_ROI_control_crop[:, :, 1] = 0
#b_ROI_control_crop[:, :, 2] = 0

#g_ROI_control_crop = ROI_control_crop.copy()
## set green and red channels to 0
#g_ROI_control_crop[:, :, 0] = 0
#g_ROI_control_crop[:, :, 2] = 0

#r_ROI_control_crop = ROI_control_crop.copy()
## set green and red channels to 0
#r_ROI_control_crop[:, :, 0] = 0
#r_ROI_control_crop[:, :, 1] = 0



#b_ROI_test_crop = ROI_test_crop.copy()
## set green and red channels to 0
#b_ROI_test_crop[:, :, 1] = 0
#b_ROI_test_crop[:, :, 2] = 0

#g_ROI_test_crop = ROI_test_crop.copy()
## set blue and red channels to 0
#g_ROI_test_crop[:, :, 0] = 0
#g_ROI_test_crop[:, :, 2] = 0

#r_ROI_test_crop = ROI_test_crop.copy()
## set blue and green channels to 0
#r_ROI_test_crop[:, :, 0] = 0
#r_ROI_test_crop[:, :, 1] = 0




#b_ROI_background_crop = ROI_background_crop.copy()
## set green and red channels to 0
#b_ROI_background_crop[:, :, 1] = 0
#b_ROI_background_crop[:, :, 2] = 0

#g_ROI_background_crop = ROI_background_crop.copy()
## set blue and red channels to 0
#g_ROI_background_crop[:, :, 0] = 0
#g_ROI_background_crop[:, :, 2] = 0

#r_ROI_background_crop = ROI_background_crop.copy()
## set blue and green channels to 0
#r_ROI_background_crop[:, :, 0] = 0
#r_ROI_background_crop[:, :, 1] = 0

#roi_control_avg_intensity = np.mean(g_ROI_control_crop)

#roi_test_avg_intensity = np.mean(g_ROI_test_crop)

#roi_background_avg_intensity = np.mean(g_ROI_background_crop)

#roi_corrected_0to1 = (roi_test_avg_intensity - roi_background_avg_intensity)/(0 - roi_background_avg_intensity)

#print roi_corrected_0to1
#print roi_control_avg_intensity
#print roi_test_avg_intensity
#print roi_background_avg_intensity

## output to text file
#lines = ['roi_corrected_0to1', str(roi_corrected_0to1), 'roi_control_avg_intensity', str(roi_control_avg_intensity), 'roi_test_avg_intensity', str(roi_test_avg_intensity), 'roi_background_avg_intensity', str(roi_background_avg_intensity)]
#with open('output.txt', 'w') as file:
    #file.write('\n'.join(lines))

#file.close()

#ROI_control_box = cv2.rectangle(I,(int(ROI_control[0]),int(ROI_control[1])),(int(ROI_control[0]+ROI_control[2]),int(ROI_control[1]+ROI_control[3])),(255,0,0),3)
#ROI_test_box = cv2.rectangle(I,(int(ROI_control[0]),int(ROI_control[1])+Distance_control_test),(int(ROI_control[0]+ROI_control[2]),int(ROI_control[1]+ROI_control[3])+Distance_control_test),(0,0,255),3)
#ROI_background_box = cv2.rectangle(I,(int(ROI_control[0]),int(ROI_control[1])+Distance_control_background),(int(ROI_control[0]+ROI_control[2]),int(ROI_control[1]+ROI_control[3])+Distance_control_background),(0,0,0),3)

#plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
#plt.show()
