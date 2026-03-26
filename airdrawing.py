import cv2
import numpy as np

cap = cv2.VideoCapture(0)

canvas = None

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # detect blue color (use blue pen)
    lower_blue = np.array([100,150,0])
    upper_blue = np.array([140,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 800:
            x,y,w,h = cv2.boundingRect(cnt)
            cx = x + w//2
            cy = y + h//2

            cv2.circle(frame, (cx, cy), 5, (0,0,255), -1)

            # draw on canvas
            cv2.circle(canvas, (cx, cy), 5, (255,255,255), -1)

    # merge drawing + frame
    combined = cv2.add(frame, canvas)

    cv2.imshow("Air Drawing", combined)

    # press 'c' to clear
    if cv2.waitKey(1) & 0xFF == ord('c'):
        canvas = np.zeros_like(frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()