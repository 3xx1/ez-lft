import matplotlib.pyplot as plt
import numpy as np
import cv2
from matplotlib.widgets  import RectangleSelector
import matplotlib


I = cv2.imread('images/LFT_example.png')

ROI_control = I[203:223, 190:270]

ROI_test = I[378:398, 190:270]

ROI_background = I[418:438, 190:270]

b_ROI_control = ROI_control.copy()
# set green and red channels to 0
b_ROI_control[:, :, 1] = 0
b_ROI_control[:, :, 2] = 0

g_ROI_control = ROI_control.copy()
# set blue and red channels to 0
g_ROI_control[:, :, 0] = 0
g_ROI_control[:, :, 2] = 0

r_ROI_control = ROI_control.copy()
# set blue and green channels to 0
r_ROI_control[:, :, 0] = 0
r_ROI_control[:, :, 1] = 0

b_ROI_test = ROI_test.copy()
# set green and red channels to 0
b_ROI_test[:, :, 1] = 0
b_ROI_test[:, :, 2] = 0

g_ROI_test = ROI_test.copy()
# set blue and red channels to 0
g_ROI_test[:, :, 0] = 0
g_ROI_test[:, :, 2] = 0

r_ROI_test = ROI_test.copy()
# set blue and green channels to 0
r_ROI_test[:, :, 0] = 0
r_ROI_test[:, :, 1] = 0

b_ROI_background = ROI_background.copy()
# set green and red channels to 0
b_ROI_background[:, :, 1] = 0
b_ROI_background[:, :, 2] = 0

g_ROI_background = ROI_background.copy()
# set blue and red channels to 0
g_ROI_background[:, :, 0] = 0
g_ROI_background[:, :, 2] = 0

r_ROI_background = ROI_background.copy()
# set blue and green channels to 0
r_ROI_background[:, :, 0] = 0
r_ROI_background[:, :, 1] = 0

roi_control_avg_intensity = np.mean(g_ROI_control)

roi_test_avg_intensity = np.mean(g_ROI_test)

roi_background_avg_intensity = np.mean(g_ROI_background)

roi_corrected = (roi_test_avg_intensity - roi_background_avg_intensity)/(0 - roi_background_avg_intensity)

print roi_corrected
print roi_control_avg_intensity
print roi_test_avg_intensity
print roi_background_avg_intensity

ROI_control_box = cv2.rectangle(I,(190,203),(270,223),(255,0,0),3)
ROI_test_box = cv2.rectangle(I,(190,378),(270,398),(0,0,255),3)
ROI_background_box = cv2.rectangle(I,(190,418),(270,438),(0,0,0),3)

plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.show()
