# learn more 
# https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html

import os
import cv2
import numpy as np

# Define the path to the input image
img_path = os.path.join(".", "photos", "sample_two.jpg")

# Read the image
img = cv2.imread(img_path)

# Resize the image to a specified width and height
resize_img = cv2.resize(img, (600, 800))  # width, height

# Apply the Canny edge detection algorithm to the resized image
# Parameters: (image, threshold1, threshold2)
# - image: Input image
# - threshold1: First threshold for the hysteresis procedure
# - threshold2: Second threshold for the hysteresis procedure
img_edge = cv2.Canny(resize_img, 100, 200)

# Dilate the edges in the image to make them thicker and more visible
# Parameters: (image, kernel)
# - image: Input image
# - kernel: Structuring element for dilation
img_edge_dilate = cv2.dilate(img_edge, np.ones((5, 5), dtype=np.int8))

# Erode the dilated edges to refine and reduce thickness
# Parameters: (image, kernel)
# - image: Input image
# - kernel: Structuring element for erosion
img_edge_erode = cv2.erode(img_edge_dilate, np.ones((5, 5), dtype=np.int8))

# Display the original, resized, edged, dilated, and eroded images
# cv2.imshow("Image", img)
cv2.imshow("Resized Image", resize_img)
cv2.imshow("Edge Image", img_edge)
cv2.imshow("Edge Dilated Image", img_edge_dilate)
cv2.imshow("Edge Eroded Image", img_edge_erode)

# Wait for a key press to close the image windows
cv2.waitKey(0)