import cv2

# Open the default camera (camera index 0)
# cv2.VideoCapture() initializes a video capture object for reading video frames
webcam = cv2.VideoCapture(0)

# Infinite loop to continuously capture and display frames from the webcam
while True:
    # Read a frame from the webcam
    # webcam.read() returns a tuple (ret, frame), where ret is a boolean indicating success and frame is the frame data
    ret, frame = webcam.read()

    # Display the current frame in a window named "frame"
    # cv2.imshow() displays an image in a window with the specified name
    cv2.imshow("frame", frame)

    # Check for the 'q' key press to exit the loop
    # cv2.waitKey() waits for a key event. The argument is the delay in milliseconds (40 milliseconds here).
    # The condition (cv2.waitKey(40) & 0xFF == ord('q')) checks if the 'q' key is pressed.
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

# Release the webcam capture object to free resources
# webcam.release() releases the video capture object
webcam.release()

# Close all OpenCV windows
# cv2.destroyAllWindows() closes all OpenCV windows
cv2.destroyAllWindows()