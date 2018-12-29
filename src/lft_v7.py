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
Distance_control_background = 60
Distance_control_background2 = 120

ROI_test_box_width = 36
ROI_test_box_height = 40

ROI_background_box_width = 36
ROI_background_box_height = 20

ROI_background2_box_width = 36
ROI_background2_box_height = 20


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

    if w >= 42 and h >= 10:
        # if width and height are enough
        # create rectangle for bounding
        rect = (x, y, w, h)
        rects.append(rect)

        # compute the center of the rectangles
        centerCoord = (rect[0]+(rect[2]/2), rect[1]+(rect[3]/2))
        # write circles from the center of the rectangles
        #cv2.circle(I, (rect[0]+(rect[2]/2), rect[1]+(rect[3]/2)), 5, (255, 255, 255), 2)

        # write ellipses from the center of the rectangles
        ellipse_control = cv2.ellipse(I, ((rect[0]+(rect[2]/2), rect[1]+(rect[3]/2)), (5, 5), -1), (255, 0, 0), 3)
        #list = zip(ellipse_control)
        #for i in enumerate(list):
            #cv2.putText(I, "#{}".format(i + 1), (rect[0]+(rect[2]/2), rect[1]+(rect[3]/2) - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1)


        # write ROI at test line, based on the center of the control line
        #ROI_test = cv2.ellipse(I, ((rect[0]+(rect[2]/2), rect[1]+(rect[3]/2) + Distance_control_test), (35, 9), 0), (255, 255, 0), 2)
        #ROI_test_box = cv2.rectangle(I,(int(rect[0]+(rect[2]/2) - 14),int(rect[1]+(rect[3]/2) + Distance_control_test - 2.5)),(int(rect[0]+(rect[2]/2) + 14),int(rect[1]+(rect[3]/2) + Distance_control_test + 2.5)),(255,255,0),1)
        #ROI_test_crop = I[int(rect[1]+(rect[3]/2) + Distance_control_test - (ROI_test_box_height/2)):int(rect[1]+(rect[3]/2) + Distance_control_test + (ROI_test_box_height/2)), int(rect[0]+(rect[2]/2) - (ROI_test_box_width/2)):int(rect[0]+(rect[2]/2) + (ROI_test_box_width/2))]

        # write ROI at background, based on the center of the control line
        #ROI_background_box = cv2.rectangle(I,(int(rect[0]+(rect[2]/2) - 14),int(rect[1]+(rect[3]/2) + Distance_control_background - 2.5)),(int(rect[0]+(rect[2]/2) + 14),int(rect[1]+(rect[3]/2) + Distance_control_background + 2.5)),(0,0,0),1)
        #ROI_background_crop = I[int(rect[1]+(rect[3]/2) + Distance_control_background - (ROI_test_box_height/2)):int(rect[1]+(rect[3]/2) + Distance_control_background + (ROI_test_box_height/2)), int(rect[0]+(rect[2]/2) - (ROI_test_box_width/2)):int(rect[0]+(rect[2]/2) + (ROI_test_box_width/2))]


        # write rectangles for bounding of contours
        #cv2.rectangle(I, (x, y), (x+w, y+h), (255, 0, 0), 1)

        # add number for each rectangle
        #cv2.putText(I, "#{}".format(i + 1), (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1)

        #b_ROI_test_crop = ROI_test_crop.copy()
        # set green and red channels to 0
        #b_ROI_test_crop[:, :, 1] = 0
        #b_ROI_test_crop[:, :, 2] = 0

        #g_ROI_test_crop = ROI_test_crop.copy()
        # set blue and red channels to 0
        #g_ROI_test_crop[:, :, 0] = 0
        #g_ROI_test_crop[:, :, 2] = 0

        #r_ROI_test_crop = ROI_test_crop.copy()
        # set blue and green channels to 0
        #r_ROI_test_crop[:, :, 0] = 0
        #r_ROI_test_crop[:, :, 1] = 0


        #b_ROI_background_crop = ROI_background_crop.copy()
        # set green and red channels to 0
        #b_ROI_background_crop[:, :, 1] = 0
        #b_ROI_background_crop[:, :, 2] = 0

        #g_ROI_background_crop = ROI_background_crop.copy()
        # set blue and red channels to 0
        #g_ROI_background_crop[:, :, 0] = 0
        #g_ROI_background_crop[:, :, 2] = 0

        #r_ROI_background_crop = ROI_background_crop.copy()
        # set blue and green channels to 0
        #r_ROI_background_crop[:, :, 0] = 0
        #r_ROI_background_crop[:, :, 1] = 0


        #calculate signal intensities
        #roi_control_avg_intensity = np.mean(g_ROI_control_crop)
        #roi_test_avg_intensity = np.mean(g_ROI_test_crop)
        #roi_background_avg_intensity = np.mean(g_ROI_background_crop)
        #roi_corrected_0to1 = (roi_test_avg_intensity - roi_background_avg_intensity)/(0 - roi_background_avg_intensity)

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

        #plt.plot([1-x for x in myAvg])
        #plt.plot([1-x for x in myAvg] - (np.mean([1-x for x in myAvg2]) + np.mean([1-x for x in myAvg3]))/2)

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




        #plt.plot([1-x for x in myAvg2])

        #plt.plot([1-x for x in myAvg3])

        #print np.mean([1-x for x in myAvg2])
        #print np.std([1-x for x in myAvg2])
        #print np.mean([1-x for x in myAvg3])
        #print np.std([1-x for x in myAvg3])
        #print (np.mean([1-x for x in myAvg2]) + np.mean([1-x for x in myAvg3]))/2
        #print (np.std([1-x for x in myAvg2]) + np.std([1-x for x in myAvg3]))/2

        #3x standard devication of (background + background2)
        #print (np.std([1-x for x in myAvg2]) + np.std([1-x for x in myAvg3]))/2*3


        # make models for individual components
        #mod_expon = ExponentialModel(prefix='exp_')
        #mod_gauss = GaussianModel(prefix='g1_')
        # sum components to make a composite model (add more if needed)
        #model  = mod_expon + mod_gauss
        # create fitting parameters by name, give initial values
        #params = model.make_params(g1_amplitude=5, g1_center=55, g1_sigma=5, exp_amplitude=5, exp_decay=10)
        # do fit
        #result = model.fit(myAvg, params, x=[1-x for x in myAvg])
        #print(result.fit_report())
        #plt.plot(x, result.best_fit, 'r-')


        #print min(1-x for x in myAvg)
        #print np.mean([1-x for x in myAvg])

        #fig = plt.figure()

        #for i in range(5):
            #plt.subplot(5,1,i+1)
            #m = Basemap()
            #m.imshow([1-x for x in myAvg][i])
            #plt.plot([1-x for x in myAvg])

        #plt.show()

        #axes = []
        #fig = plt.figure()
        #for i in range (1, 2):
            #axes.append(fig.add_subplot(1, 1, i))
            #axes[i-1].plot([1-x for x in myAvg])

        #ax1.set_title('Sharing both axes')
        #ax2.scatter(x, y)
        #ax3.scatter(x, 2 * y ** 2 - 1, color='r')

        #plot([1-x for x in myAvg])
        #plt.autoscale()
        #canvas.draw()



        #print roi_corrected_0to1
        #print roi_control_avg_intensity
        #print roi_test_avg_intensity
        #print roi_background_avg_intensity

        # write ROI at test line and background, based on the center of the control line
        ROI_test_box = cv2.rectangle(I,(int(rect[0]+(rect[2]/2) - (ROI_test_box_width/2)),int(rect[1]+(rect[3]/2) + Distance_control_test - (ROI_test_box_height/2))),(int(rect[0]+(rect[2]/2) + (ROI_test_box_width/2)),int(rect[1]+(rect[3]/2) + Distance_control_test + (ROI_test_box_height/2))),(255,255,51),2)
        ROI_background_box = cv2.rectangle(I,(int(rect[0]+(rect[2]/2) - (ROI_background_box_width/2)),int(rect[1]+(rect[3]/2) + Distance_control_background - (ROI_background_box_height/2))),(int(rect[0]+(rect[2]/2) + (ROI_background_box_width/2)),int(rect[1]+(rect[3]/2) + Distance_control_background + (ROI_background_box_height/2))),(0,0,0),1)
        ROI_background2_box = cv2.rectangle(I,(int(rect[0]+(rect[2]/2) - (ROI_background2_box_width/2)),int(rect[1]+(rect[3]/2) + Distance_control_background2 - (ROI_background2_box_height/2))),(int(rect[0]+(rect[2]/2) + (ROI_background2_box_width/2)),int(rect[1]+(rect[3]/2) + Distance_control_background2 + (ROI_background_box_height/2))),(0,0,0),1)



        # add number for each rectangle
        cv2.putText(I, "#{}".format(i + 1), (rect[0]+(rect[2]/2) - 20, rect[1]+(rect[3]/2) - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # output to text file
        #lines = ['roi_corrected_0to1', str(roi_corrected_0to1), 'roi_test_avg_intensity', str(roi_test_avg_intensity), 'roi_background_avg_intensity', str(roi_background_avg_intensity)]
        #with open('output.txt', 'w') as file:
        #    file.write('\n'.join(lines))

        #file.close()

        plt.subplot(224)
        plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
        plt.title("ROI on image")
        plt.xlabel("Pixels")
        plt.ylabel("Pixels")



#cv2.imshow('Edges',edges)
#cv2.imshow('res',res)
#cv2.imshow('mask',mask)

#fig = plt.figure()

#plt.subplot()

#fig = plt.figure()

#plt.subplot(133)
#plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))

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
