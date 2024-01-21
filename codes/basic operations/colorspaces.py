import os
import cv2

# Define the path to the input image
image_path = os.path.join(".", "photos", "sample_one.jpg")

# Read the image from the specified path
# cv2.imread() returns a NumPy array representing the image
original_img = cv2.imread(image_path)

# Display the original image
cv2.imshow("Original Image", original_img)
cv2.waitKey(0)

# Convert the image to black and white (grayscale)
# cv2.cvtColor() is used to convert the color space of the image
# cv2.COLOR_BGR2GRAY converts BGR (color) image to grayscale
black_and_white_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

# Convert the image to inverse (negative) color
# cv2.cvtColor() is used to convert the color space of the image
# cv2.COLOR_BGR2RGB converts BGR (color) image to RGB
inverse_color_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)

# Apply a constant border to the image
# cv2.copyMakeBorder() is used to add a constant border
# cv2.BORDER_CONSTANT is the border type, and value=[0, 255, 0] is the constant border color (green)
img_with_border = cv2.copyMakeBorder(original_img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[0, 255, 0])

# Convert the original image to HSV color space
# cv2.COLOR_BGR2HSV converts BGR (color) image to HSV
hsv_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)

# Display the black and white, inverse color, bordered, and HSV images
cv2.imshow("Black and White Image", black_and_white_img)
cv2.imshow("Inverse Color Image", inverse_color_img)
cv2.imshow("Image with Border", img_with_border)
cv2.imshow("HSV Image", hsv_img)

# Wait for a key press to close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()