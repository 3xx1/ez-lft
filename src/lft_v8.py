import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.figure import Figure
import matplotlib.colors as colors
from matplotlib.cm import ScalarMappable

#from mpl_toolkits.basemap import Basemap
import pandas as pd
import matplotlib as mpl

from numpy import exp, loadtxt, pi, sqrt

from lmfit import Model
from lmfit.models import PowerLawModel, ExponentialModel, GaussianModel

import numpy as np
from numpy import arange, sin, pi
from kivy.app import App

from scipy import signal
#from scipy import ndimage
import cv2
from matplotlib.widgets  import RectangleSelector
import matplotlib

from imutils import contours
import imutils



# Required information for each scanned image
Distance_control_test = 90
Distance_control_background = 54
Distance_control_background2 = 126

ROI_test_box_width = 26
ROI_test_box_height = 48

ROI_background_box_width = 26
ROI_background_box_height = 24

ROI_background2_box_width = 26
ROI_background2_box_height = 24


# Upload and resize the scanned image
I_raw = cv2.imread('images/LFT_example.png')
I_resize = cv2.resize(I_raw, (638, 292))

#blur to extract edge
I = cv2.blur(I_resize, (5, 10))

# HSV to extract edge
hsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)

# thresholds to detect test lines as edge extraction by Canny
lower_red = np.array([0,34,50])
upper_red = np.array([6,255,255])

mask = cv2.inRange(hsv, lower_red, upper_red)
#res = cv2.bitwise_and(I,I, mask= mask)

# edges by the threshold
edges = cv2.Canny(mask,100,200)
copy = edges.copy()

# Find contours for detected portion of the image
rects = []
cnts = cv2.findContours(copy, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# sort number for each rectangle from left to right
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
cnts = contours.sort_contours(cnts)[0]

for (i, c) in enumerate(cnts):
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    x, y, w, h = cv2.boundingRect(approx)

    if w >= 42 and h >= 10:
        # if width and height are enough
        # create rectangle for bounding
        rect = (x, y, w, h)
        #rects.append(rect)

        # compute the center of the rectangles
        centerCoord = (rect[0]+(rect[2]/2), rect[1]+(rect[3]/2))

        # write ellipses from the center of the rectangles
        ellipse_control = cv2.ellipse(I, ((rect[0]+(rect[2]/2), rect[1]+(rect[3]/2)), (5, 5), -1), (255, 0, 0), 3)
        #list = zip(ellipse_control)
        #for i in enumerate(list):
            #cv2.putText(I, "#{}".format(i + 1), (rect[0]+(rect[2]/2), rect[1]+(rect[3]/2) - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1)

        #Box at test line
        x1, y1 = int(rect[0]+(rect[2]/2) - (ROI_test_box_width/2)), int(rect[1]+(rect[3]/2) + Distance_control_test - (ROI_test_box_height/2))
        x2, y2 = int(rect[0]+(rect[2]/2) + (ROI_test_box_width/2)), int(rect[1]+(rect[3]/2) + Distance_control_test + (ROI_test_box_height/2))

        #Box at background
        x3, y3 = int(rect[0]+(rect[2]/2) - (ROI_background_box_width/2)), int(rect[1]+(rect[3]/2) + Distance_control_background - (ROI_background_box_height/2))
        x4, y4 = int(rect[0]+(rect[2]/2) + (ROI_background_box_width/2)), int(rect[1]+(rect[3]/2) + Distance_control_background + (ROI_background_box_height/2))

        #Box at background
        x5, y5 = int(rect[0]+(rect[2]/2) - (ROI_background2_box_width/2)), int(rect[1]+(rect[3]/2) + Distance_control_background2 - (ROI_background2_box_height/2))
        x6, y6 = int(rect[0]+(rect[2]/2) + (ROI_background2_box_width/2)), int(rect[1]+(rect[3]/2) + Distance_control_background2 + (ROI_background2_box_height/2))

        green = I[:,:,1]

        myAvg = []
        for y in range(int(round(y1)), int(round(y2))):
            myAvg.append(np.mean(green[y,int(round(x1)):int(round(x2))]))

        myAvg2 = []
        for y in range(int(round(y3)), int(round(y4))):
            myAvg2.append(np.mean(green[y,int(round(x3)):int(round(x4))]))

        myAvg3 = []
        for y in range(int(round(y5)), int(round(y6))):
            myAvg3.append(np.mean(green[y,int(round(x5)):int(round(x6))]))

        #plot signal at test line more than 3STD of background
        plt.subplot(221)
        plt.plot([1-x for x in myAvg] - (np.mean([1-x for x in myAvg2]) + np.mean([1-x for x in myAvg3]))/2 - (np.std([1-x for x in myAvg2]) + np.std([1-x for x in myAvg3]))/2*3, label = i+1)
        plt.legend()
        plt.title("Profile at test line")
        plt.xlabel("Pixels")
        plt.ylabel("Pixel intensity")

        #integrate and plot results
        results = np.trapz([1-x for x in myAvg] - (np.mean([1-x for x in myAvg2]) + np.mean([1-x for x in myAvg3]))/2 - (np.std([1-x for x in myAvg2]) + np.std([1-x for x in myAvg3]))/2*3)
        print results
        plt.subplot(222)
        plt.scatter([i + 1], results)
        plt.title("Integrated signal intensity")
        plt.xlabel("Sample#")
        plt.ylabel("Integrated signal intensity")

        # write ROI at test line and background, based on the center of the control line
        ROI_test_box = cv2.rectangle(I,(int(rect[0]+(rect[2]/2) - (ROI_test_box_width/2)),int(rect[1]+(rect[3]/2) + Distance_control_test - (ROI_test_box_height/2))),(int(rect[0]+(rect[2]/2) + (ROI_test_box_width/2)),int(rect[1]+(rect[3]/2) + Distance_control_test + (ROI_test_box_height/2))),(255,255,51),2)
        ROI_background_box = cv2.rectangle(I,(int(rect[0]+(rect[2]/2) - (ROI_background_box_width/2)),int(rect[1]+(rect[3]/2) + Distance_control_background - (ROI_background_box_height/2))),(int(rect[0]+(rect[2]/2) + (ROI_background_box_width/2)),int(rect[1]+(rect[3]/2) + Distance_control_background + (ROI_background_box_height/2))),(0,0,0),1)
        ROI_background2_box = cv2.rectangle(I,(int(rect[0]+(rect[2]/2) - (ROI_background2_box_width/2)),int(rect[1]+(rect[3]/2) + Distance_control_background2 - (ROI_background2_box_height/2))),(int(rect[0]+(rect[2]/2) + (ROI_background2_box_width/2)),int(rect[1]+(rect[3]/2) + Distance_control_background2 + (ROI_background_box_height/2))),(0,0,0),1)

        # add number for each rectangle
        cv2.putText(I, "#{}".format(i + 1), (rect[0]+(rect[2]/2) - 20, rect[1]+(rect[3]/2) - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        #[(count) for count in enumerate(centerCoord)]
        #[[i,j] for i,j in enumerate(ellipse_control)]
        #cv2.putText(I, "#{}".format(i), (rect[0]+(rect[2]/2) - 20, rect[1]+(rect[3]/2) - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)




        # output to text file
        #lines = ['roi_corrected_0to1', str(roi_corrected_0to1), 'roi_test_avg_intensity', str(roi_test_avg_intensity), 'roi_background_avg_intensity', str(roi_background_avg_intensity)]
        #with open('output.txt', 'w') as file:
        #    file.write('\n'.join(lines))

        #file.close()

        plt.subplot(223)
        plt.imshow(cv2.cvtColor(I_resize, cv2.COLOR_BGR2RGB))
        plt.title("Raw image")
        plt.xlabel("Pixels")
        plt.ylabel("Pixels")

        plt.subplot(224)
        plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
        plt.title("ROI on image")
        plt.xlabel("Pixels")
        plt.ylabel("Pixels")


plt.show()
