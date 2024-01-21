# learn more 
# https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html
# https://www.geeksforgeeks.org/python-bilateral-filtering/

import os
import cv2

# Define the path to the input image
image_path = os.path.join(".", "photos", "sample_one.jpg")

# Read the image from the specified path
# cv2.imread() returns a NumPy array representing the image
original_img = cv2.imread(image_path)

# Display the original image
cv2.imshow("Original Image", original_img)

# Define the kernel size for blur operations
k_size = 7  # Bigger the kernel size, stronger the blur

# Apply a simple box blur to the image
blur_img = cv2.blur(original_img, (k_size, k_size))
cv2.imshow("Box Blur Image", blur_img)

# Apply Gaussian blur to the image
blur_gauss = cv2.GaussianBlur(original_img, (k_size, k_size), 0)
cv2.imshow("Gaussian Blur Image", blur_gauss)

# Apply median blur to the image
blur_median = cv2.medianBlur(original_img, k_size)
cv2.imshow("Median Blur Image", blur_median)

# Apply bilateral blur to the image
# The parameters are (source image, d, sigmaColor, sigmaSpace)
# d: Diameter of each pixel neighborhood.
# sigmaColor: Value of \sigma  in the color space. The greater the value, the colors farther to each other will start to get mixed.
# sigmaSpace: Value of \sigma  in the coordinate space. The greater its value, the more further pixels will mix together, given that their colors lie within the sigmaColor range.
blur_bilateral = cv2.bilateralFilter(original_img, d=9, sigmaColor=75, sigmaSpace=75)
cv2.imshow("Bilateral Blur Image", blur_bilateral)

# Wait for a key press to close the image windows
cv2.waitKey(0)