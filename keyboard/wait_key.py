
import cv2

print("Wait indefinitely for a key press.")
# The function cv2.waitKey(0) waits indefinitely until a key is pressed.
cv2.waitKey(0)

print("Wait for 5000 milliseconds (5 seconds) for a key press.")
cv2.waitKey(5000)
# If no key is pressed within this time, the function returns -1.
# Note: cv2.waitKey() is often used in conjunction with OpenCV image display functions like cv2.imshow().

print("Press ESC to exit")
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ASCII value of esc key is 27
        break