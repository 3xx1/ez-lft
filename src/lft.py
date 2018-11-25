import matplotlib.pyplot as plt
import numpy as np
import cv2
from matplotlib.widgets  import RectangleSelector

I = cv2.imread('images/LFT_example.png')

plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.show()

def line_select_callback(eclick, erelease):
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata

rs = RectangleSelector(I, line_select_callback,
                       drawtype='box', useblit=False, button=[1],
                       minspanx=5, minspany=5, spancoords='pixels',
                       interactive=True)

rs.mean()
