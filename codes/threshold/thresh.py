# learn more
# https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html

import os
import cv2

# Define the path to the input image
img_path = os.path.join(".", "photos", "sample_one.jpg")

# Read the image using OpenCV
img = cv2.imread(img_path)

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply global thresholding to create a binary image
# Threshold the grayscale image using a fixed threshold value of 80
# Pixels with intensity values greater than 80 become white (255), and others become black (0)
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

# Apply adaptive thresholding using a Gaussian-based method
# cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
# - src: Source image (grayscale)
# - maxValue: Maximum pixel value (255 for binary images)
# - adaptiveMethod: Adaptive thresholding method (cv2.ADAPTIVE_THRESH_GAUSSIAN_C in this case)
# - thresholdType: Type of thresholding applied after adaptive thresholding (cv2.THRESH_BINARY)
# - blockSize: Size of the neighborhood for adaptive thresholding (21 in this example)
# - C: Constant subtracted from the mean for adaptive thresholding (30 in this example)
img_adaptive_thresh = cv2.adaptiveThreshold(
    img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30
)

# Display the original image, grayscale image, and thresholded images
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", img_gray)
cv2.imshow("Global Thresholding", thresh)
cv2.imshow("Adaptive Thresholding", img_adaptive_thresh)

# Wait for a key press to close the image windows
cv2.waitKey(0)