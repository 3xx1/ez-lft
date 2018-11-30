import matplotlib.pyplot as plt
import numpy as np
import cv2
from matplotlib.widgets  import RectangleSelector
import matplotlib

# Required information for each scanned image
Distance_control_test = 85
Distance_control_background = 105

I_raw = cv2.imread('images/LFT_example.png')
I = cv2.resize(I_raw, (638, 292))

# Select ROI_control
fromCenter = False
ROI_control = cv2.selectROI(I, fromCenter)

# Crop image
ROI_control_crop = I[int(ROI_control[1]):int(ROI_control[1]+ROI_control[3]), int(ROI_control[0]):int(ROI_control[0]+ROI_control[2])]
ROI_test_crop = I[int(ROI_control[1])+Distance_control_test:int(ROI_control[1]+ROI_control[3]+Distance_control_test), int(ROI_control[0]):int(ROI_control[0]+ROI_control[2])]
ROI_background_crop = I[int(ROI_control[1])+Distance_control_background:int(ROI_control[1]+ROI_control[3]+Distance_control_background), int(ROI_control[0]):int(ROI_control[0]+ROI_control[2])]

##ROI_control = I[203:223, 190:270]

##ROI_test = I[378:398, 190:270]

##ROI_background = I[418:438, 190:270]


b_ROI_control_crop = ROI_control_crop.copy()
# set green and red channels to 0
b_ROI_control_crop[:, :, 1] = 0
b_ROI_control_crop[:, :, 2] = 0

g_ROI_control_crop = ROI_control_crop.copy()
# set green and red channels to 0
g_ROI_control_crop[:, :, 0] = 0
g_ROI_control_crop[:, :, 2] = 0

r_ROI_control_crop = ROI_control_crop.copy()
# set green and red channels to 0
r_ROI_control_crop[:, :, 0] = 0
r_ROI_control_crop[:, :, 1] = 0



b_ROI_test_crop = ROI_test_crop.copy()
# set green and red channels to 0
b_ROI_test_crop[:, :, 1] = 0
b_ROI_test_crop[:, :, 2] = 0

g_ROI_test_crop = ROI_test_crop.copy()
# set blue and red channels to 0
g_ROI_test_crop[:, :, 0] = 0
g_ROI_test_crop[:, :, 2] = 0

r_ROI_test_crop = ROI_test_crop.copy()
# set blue and green channels to 0
r_ROI_test_crop[:, :, 0] = 0
r_ROI_test_crop[:, :, 1] = 0




b_ROI_background_crop = ROI_background_crop.copy()
# set green and red channels to 0
b_ROI_background_crop[:, :, 1] = 0
b_ROI_background_crop[:, :, 2] = 0

g_ROI_background_crop = ROI_background_crop.copy()
# set blue and red channels to 0
g_ROI_background_crop[:, :, 0] = 0
g_ROI_background_crop[:, :, 2] = 0

r_ROI_background_crop = ROI_background_crop.copy()
# set blue and green channels to 0
r_ROI_background_crop[:, :, 0] = 0
r_ROI_background_crop[:, :, 1] = 0

roi_control_avg_intensity = np.mean(g_ROI_control_crop)

roi_test_avg_intensity = np.mean(g_ROI_test_crop)

roi_background_avg_intensity = np.mean(g_ROI_background_crop)

roi_corrected_0to1 = (roi_test_avg_intensity - roi_background_avg_intensity)/(0 - roi_background_avg_intensity)

print roi_corrected_0to1
print roi_control_avg_intensity
print roi_test_avg_intensity
print roi_background_avg_intensity

# output to text file
lines = ['roi_corrected_0to1', str(roi_corrected_0to1), 'roi_control_avg_intensity', str(roi_control_avg_intensity), 'roi_test_avg_intensity', str(roi_test_avg_intensity), 'roi_background_avg_intensity', str(roi_background_avg_intensity)]
with open('output.txt', 'w') as file:
    file.write('\n'.join(lines))

file.close()

ROI_control_box = cv2.rectangle(I,(int(ROI_control[0]),int(ROI_control[1])),(int(ROI_control[0]+ROI_control[2]),int(ROI_control[1]+ROI_control[3])),(255,0,0),3)
ROI_test_box = cv2.rectangle(I,(int(ROI_control[0]),int(ROI_control[1])+Distance_control_test),(int(ROI_control[0]+ROI_control[2]),int(ROI_control[1]+ROI_control[3])+Distance_control_test),(0,0,255),3)
ROI_background_box = cv2.rectangle(I,(int(ROI_control[0]),int(ROI_control[1])+Distance_control_background),(int(ROI_control[0]+ROI_control[2]),int(ROI_control[1]+ROI_control[3])+Distance_control_background),(0,0,0),3)

plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.show()
