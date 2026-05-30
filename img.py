import numpy as np
img = np.array([
    [50,100],
    [150,200]
], dtype=np.uint8)

bright = img + 50

print(bright)