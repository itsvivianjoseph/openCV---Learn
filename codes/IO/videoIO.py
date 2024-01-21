import cv2

# Provide the absolute path to the video file
vdo_path = "videos\sample_video.mp4"

# Open the video file
# cv2.VideoCapture() initializes a video capture object for reading video frames
video = cv2.VideoCapture(vdo_path)

# Check if the video is successfully opened
# video.isOpened() returns True if the video capture object is successfully opened
if not video.isOpened():
    print(f"Error: Could not open video file at {vdo_path}")
    exit()

ret = True

# Loop through video frames
while ret:
    # Read the next frame from the video
    # video.read() returns a tuple (ret, frame), where ret is a boolean indicating success and frame is the frame data
    ret, frame = video.read()

    # Display the current frame
    # cv2.imshow() displays an image in a window with the specified name
    cv2.imshow("frame", frame)

    # Wait for a specified amount of time (in milliseconds) before showing the next frame
    # cv2.waitKey() waits for a key event. The argument is the delay in milliseconds. Here, 100 milliseconds delay.
    cv2.waitKey(100)

# Release the video capture object to free resources
video.release() # releases the video capture object

# Close all OpenCV windows
cv2.destroyAllWindows() # closes all OpenCV windows