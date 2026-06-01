import numpy as np
import cv2
# import matplotlib.pyplot as plt

# img = np.array([
#     [200,180,100,100,120],
#     [190,150,255,255,120],
#     [210,150,255, 80,180]
# ], dtype=np.uint8)

# plt.imshow(img, cmap='gray')
# plt.axis("off")
# plt.show()
# plt.imsave("pixel.png", img, cmap='gray')


m=cv2.imread("pixel.png")
# print(m)

for i in m:
    print(i)