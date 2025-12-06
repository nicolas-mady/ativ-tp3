import os
from skimage.metrics import mean_squared_error
import cv2

DIR = 'images'
imgs = sorted(os.listdir(DIR))

ref = ''

for img in imgs:
    name, _ = os.path.splitext(img)

    if len(name) == 2:
        ref = img
        continue

    img1 = cv2.imread(f"{DIR}/{ref}")
    img2 = cv2.imread(f"{DIR}/{img}")

    mse = mean_squared_error(img1, img2)
    print(f"{name}: {mse}")