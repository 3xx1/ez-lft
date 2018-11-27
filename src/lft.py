import matplotlib.pyplot as plt
import numpy as np
import cv2
from matplotlib.widgets  import RectangleSelector
import matplotlib
matplotlib.use('Agg')

img_source = cv2.imread('images/LFT_example.png')
img_grayscale = cv2.cvtColor(img_source, cv2.COLOR_BGR2GRAY)
_, img_binary = cv2.threshold(img_grayscale, 250, 255, cv2.THRESH_BINARY)
spectrumContainers, _ = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(spectrumContainers))

# I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)

plt.imshow(cv2.cvtColor(img_source, cv2.COLOR_BGR2RGB))
plt.show()

# def line_select_callback(eclick, erelease):
#     x1, y1 = eclick.xdata, eclick.ydata
#     x2, y2 = erelease.xdata, erelease.ydata
#
# rs = RectangleSelector(I, line_select_callback,
#                        drawtype='box', useblit=False, button=[1],
#                        minspanx=5, minspany=5, spancoords='pixels',
#                        interactive=True)

# rs.mean()

# print(rs)
