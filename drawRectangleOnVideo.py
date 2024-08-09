import cv2

cap = cv2.VideoCapture(0)

# CALLBACK FUNCTION RECTANGLE
def changeGlobalVar(event, x, y, flags, param):
    global pt1, pt2, topLeftClicked, bottomRightClick

    if event == cv2.EVENT_LBUTTONDOWN:
        if bottomRightClick == True or topLeftClicked == False:
            topLeftClicked = True
            bottomRightClick = False
            pt1 = (x,y)
            pt2 = (0,0)
        else:
            bottomRightClick = True
            pt2 = (x,y)
def drawRectangle():
    global pt1, pt2, topLeftClicked, bottomRightClick

    if topLeftClicked:
        cv2.circle(frame, center = pt1, radius = 5, color = (0,255,0), thickness = -1)
        if bottomRightClick:
            cv2.rectangle(frame, pt1, pt2, (0,255,0), 3)
# GLOBAL VARIABLES
pt1 = (0,0)
pt2 = (0,0)
topLeftClicked = False
bottomRightClick = False
# CONNECT TO THE CALLBACK
cv2.namedWindow('Test')
cv2.setMouseCallback('Test', changeGlobalVar)

witdth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    drawRectangle()
    if ret == False:
        print("Error, cannot get a frame")
    cv2.imshow('Test', frame)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
