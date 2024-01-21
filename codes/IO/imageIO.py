import os
import cv2

# Define the path to the input image
image_path = os.path.join(".", "photos", "sample_one.jpg")

# Read the image from the specified pathṇ
# cv2.imread() returns a NumPy array representing the image
img = cv2.imread(image_path)
print(img.shape)

# Check if the image is successfully loaded
# img is None if there was an issue loading the image
if img is not None:
    # Define the path for the output image
    output_path = os.path.join(".", "photos", "sample_two.jpg")

    # Write the image to the specified output path
    # cv2.imwrite() writes the image to the specified file
    cv2.imwrite(output_path, img)
    print(f"Image successfully written to {output_path}")

    # Visualize the image using OpenCV's imshow function
    # cv2.imshow() displays the image in a window with the specified name
    cv2.imshow("random image", img)

    # Wait for a key press to close the image window
    # cv2.waitKey() waits indefinitely until a key is pressed (0 means indefinitely)
    cv2.waitKey(0)

    # Close all OpenCV windows to avoid any issues
    cv2.destroyAllWindows()
else:
    print(f"Error: Unable to read the image at {image_path}")
