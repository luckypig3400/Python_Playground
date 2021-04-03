"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(1)

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"


    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    outputFrame = cv2.flip(frame, 1)
	# cv2 flip image:https://techtutorialsx.com/2019/04/21/python-opencv-flipping-an-image/
    cv2.putText(outputFrame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.putText(outputFrame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(outputFrame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    
    cv2.imshow("Demo", outputFrame)

    if cv2.waitKey(1) == 27:
        break
