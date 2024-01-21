import os
import cv2

# Define the path to the input image
img_path = os.path.join(".", "photos", "sample_one.jpg")

# Read the image from the specified path using cv2.imread()
# cv2.imread() reads an image from a file and returns it as a NumPy array
img = cv2.imread(img_path)

# Print the shape of the original image array
# img.shape returns the dimensions of the image array, e.g., (height, width, channels)
print("Original Image Shape:", img.shape)

# Crop a region of interest (ROI) from the image
# This creates a new image (cropped_img) containing the specified region
cropped_img = img[131:224, 8:165]

# Print the shape of the cropped image array
print("Cropped Image Shape:", cropped_img.shape)

# Display the original and cropped images using cv2.imshow()
# cv2.imshow() displays the image in a window with the specified name
cv2.imshow("Original Image", img)
cv2.imshow("Cropped Image", cropped_img)

# Wait for a key press to close the image windows
# cv2.waitKey() waits indefinitely until a key is pressed (0 means indefinitely)
cv2.waitKey(0)

# Close all OpenCV windows to avoid any issues
cv2.destroyAllWindows()