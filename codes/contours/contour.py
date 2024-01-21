# learn more
# https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html

import os
import cv2

# Read the input image
img = cv2.imread(os.path.join('.', 'photos', 'birds.jpg'))

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image with inverted colors
# cv2.threshold(src, thresh, maxval, type[, dst]) returns a tuple (ret, dst)
# ret: the threshold used, thresh: the binary threshold image
# THRESH_BINARY_INV: Binary threshold with inverted colors (black and white inverted)
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours in the binary image
# cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]]) returns contours and hierarchy
# image: input image, mode: contour retrieval mode, method: contour approximation method
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through each contour found
for cnt in contours:
    # Check if the contour area is greater than a threshold value
    if cv2.contourArea(cnt) > 200:
        # cv2.drawContours(img, cnt, -1, (0, 255, 0), 1)

        # Get the bounding rectangle for the contour
        x1, y1, w, h = cv2.boundingRect(cnt)

        # Draw a rectangle around the detected object in the original image
        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)

# Display the original image with bounding rectangles
cv2.imshow('img', img)

# Display the thresholded image
cv2.imshow('thresh', thresh)

# Wait for a key press to close the image windows
cv2.waitKey(0)



# cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]]) returns contours and hierarchy
# image: Input image (binary, usually obtained through thresholding)
# mode: Contour retrieval mode (cv2.RETR_TREE retrieves all contours and reconstructs a full hierarchy)
# method: Contour approximation method (cv2.CHAIN_APPROX_SIMPLE compresses horizontal, diagonal, and vertical segments)
# contours: Output parameter representing the contours found in the image
# hierarchy: Output parameter representing the contour hierarchy (parent-child relationships)
# offset: Optional parameter representing an offset applied to all points of contours