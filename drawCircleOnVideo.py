import cv2

cap = cv2.VideoCapture(0)

#Callback function
def mouseCallback(event, x, y, flags, param):
    global pt, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        pt = (x,y)
        clicked = True

def drawCircle():
    global pt, clicked
    if clicked == True:
        cv2.circle(frame, pt, radius=40, color=(255,0,0), thickness=3)

#Global Variable
pt = (0,0)
clicked = False

#setMouseCallback
cv2.namedWindow('Capture')
cv2.setMouseCallback('Capture', mouseCallback)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    drawCircle()

    cv2.imshow('Capture', frame)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
