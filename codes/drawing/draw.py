import os
import cv2

# Read the image from the specified path
img = cv2.imread(os.path.join(".", "photos", "sample_three.jpg"))

# Display the shape of the image (height, width, number of channels)
print("Original Image Shape:", img.shape)

# Resize the image to a specified width and height
resize_img = cv2.resize(img, (1000, 640))

# Display the shape of the resized image
print("Resized Image Shape:", resize_img.shape)

# Draw a line on the resized image
# cv2.line(img, pt1, pt2, color, thickness)
cv2.line(resize_img, (100, 150), (300, 450), (0, 255, 0), 3)

# Draw a rectangle on the resized image
# cv2.rectangle(img, pt1, pt2, color, thickness)
# Use -1 for thickness to fill the rectangle
cv2.rectangle(resize_img, (200, 350), (50, 600), (0, 0, 255), 5)

# Draw a circle on the resized image
# cv2.circle(img, center, radius, color, thickness)
cv2.circle(resize_img, (500, 550), 50, (255, 0, 0), 10)

# Add text to the resized image
# cv2.putText(img, text, org, font, fontScale, color, thickness, lineType)
cv2.putText(resize_img, "hey!!!", (800, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

# Display the original and resized images
# cv2.imshow("Original Image", img)
cv2.imshow("Resized Image with Annotations", resize_img)

# Wait for a key press to close the image window
cv2.waitKey(0)



# notes :

# cv2.resize() Method:

# cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
# src: Input image.
# dsize: Output image size specified as a tuple (width, height).
# fx, fy: Scale factors along the x and y axes, respectively.
# interpolation: Interpolation method, e.g., cv2.INTER_LINEAR (default), cv2.INTER_NEAREST, etc.

# cv2.line() Method:

# cv2.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
# img: Input image.
# pt1, pt2: Endpoints of the line specified as tuples (x1, y1) and (x2, y2).
# color: Line color as a tuple (B, G, R).
# thickness: Line thickness (default is 1).
# lineType: Type of line, e.g., cv2.LINE_8 (default), cv2.LINE_AA.
# shift: Number of fractional bits in the point coordinates.

# cv2.rectangle() Method:

# cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
# img: Input image.
# pt1, pt2: Opposite corners of the rectangle specified as tuples (x1, y1) and (x2, y2).
# color: Rectangle color as a tuple (B, G, R).
# thickness: Thickness of the rectangle outline. Use -1 to fill the rectangle.
# lineType, shift: Same as in cv2.line().

# cv2.circle() Method:

# cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])
# img: Input image.
# center: Center coordinates of the circle specified as a tuple (x, y).
# radius: Radius of the circle.
# color: Circle color as a tuple (B, G, R).
# thickness, lineType, shift: Same as in cv2.line().

# cv2.putText() Method:

# cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
# img: Input image.
# text: Text to be drawn on the image.
# org: Bottom-left corner of the text string specified as a tuple (x, y).
# fontFace: Font type, e.g., cv2.FONT_HERSHEY_SIMPLEX.
# fontScale: Font scale factor.
# color: Text color as a tuple (B, G, R).
# thickness, lineType, bottomLeftOrigin: Same as in cv2.line().