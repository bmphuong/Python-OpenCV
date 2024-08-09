import cv2

cap = cv2.VideoCapture(0)
hand = cv2.imread('DATA/hand.jpg')
height, width, channels = hand.shape

cv2.namedWindow('Image')
cv2.imshow('Image', hand)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    res = cv2.matchTemplate(frame, hand, cv2.TM_CCOEFF_NORMED)

    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)

    topLeft = maxLoc
    bottomRight = (topLeft[0]+width, topLeft[1]+height)

    cv2.rectangle(frame, topLeft, bottomRight, color=(0,255,0), thickness=10)

    cv2.imshow('Detect', frame)

    if cv2.waitKey(20) &0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()