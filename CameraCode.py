# import libraries for camera initilization and detection
import cv2 as cv
import dlib
import time

# Initialize the camera using VideoCapture
frameWidth = 640
frameHeight = 480
vs = cv.VideoCapture(0)
vs.set(cv.CAP_PROP_FRAME_WIDTH, frameWidth)
vs.set(cv.CAP_PROP_FRAME_HEIGHT, frameHeight)
vs.set(cv.CAP_PROP_BRIGHTNESS, 0.5)
time.sleep(2.0)


# Show the resulting frame
while vs.isOpened():
    ret, image = vs.read()
    if not ret:
        break

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    cv.imshow("Frame", image)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
vs.release()