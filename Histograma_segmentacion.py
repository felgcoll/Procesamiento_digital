import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.util import img_as_ubyte, img_as_float
import cv2

# You need to change this to a valid image file on your computer
input_image = '4.png'

img = cv2.imread(input_image)
blur = cv2.blur(img, (3, 3))

cv2.imwrite('108_.png', blur)

blur = '108_.png'

gray_image = io.imread(blur, as_gray=True)
gray_image = img_as_ubyte(gray_image)
io.imshow(gray_image)
io.show()

print(f"Image shape: {gray_image.shape} and size: {gray_image.size}")
print(f"Un'ravel'ed shape: {gray_image.ravel().shape} and size: {gray_image.ravel().size}")

ax = plt.hist(gray_image.ravel(), bins=256)
plt.show()

approx_median = np.percentile(gray_image, 50)

ax = plt.hist(gray_image.ravel(), bins=256)
plt.axvline(approx_median, color='orange')
plt.show()

quartiles = [25, 50, 85]
ax = plt.hist(gray_image.ravel(), bins=256)
for q in np.percentile(gray_image, quartiles):
    plt.axvline(q, color='orange')
    print(q)
plt.show()