import os
import cv2

# Define the path to the input image
img_path = os.path.join(".", "photos", "sample_one.jpg")

# Read the image from the specified path using cv2.imread()
img = cv2.imread(img_path)

# Get the height, width, and number of channels of the original image
height, width, channels = img.shape
# Print the original image information
print("Original image:")
print("Height:", height)
print("Width:", width)
print("Channels:", channels)

# Resize the image to a new width and height using cv2.resize()
# Note: The order of dimensions in the shape parameter is (width, height)
resize_img = cv2.resize(img, (640, 480))

# Get the height, width, and number of channels of the resized image
height, width, channels = resize_img.shape
# Print the resized image information
print("\nResized image:")
print("Height:", height)
print("Width:", width)
print("Channels:", channels)

# Display the original and resized images using cv2.imshow()
cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resize_img)

# Wait for a key press to close the image windows
cv2.waitKey(0)