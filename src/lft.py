import matplotlib.pyplot as plt
import cv2

I = cv2.imread('images/LFT_example.png')

plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.show()
