import cv2
from Hand_Gestures import HandTrackingModule

from UI import Button
from UI import Delete
from UI import Equals
from UI import Input

##############################
# getting real time webcam feed
##############################
cap = cv2.VideoCapture(0)
detector = HandTrackingModule.HandTracker(maxHands=1, detectionConfidence=0.5, trackingConfidence=0.5)

# defining buttons
buttonListValue = [['7', '8', '9', '/'],
                   ['4', '5', '6', '*'],
                   ['1', '2', '3', '-'],
                   ['0', '.', 'AC', '+']]
buttonList = []
for x in range(4):
    for y in range(4):
        xpos = x * 100 + 600
        ypos = y * 100 + 100
        buttonList.append(Button((xpos, ypos), 100, 100, buttonListValue[y][x]))
# defining buttons end

# Variables
myEquation = ""
delayCounter = 0

# delete button image
deleteButtonImg = cv2.imread('deleteButton.jpg')
deleteButtonImg = cv2.resize(deleteButtonImg, (50, 50))

while True:
    success, frame = cap.read()
    frame = cv2.resize(frame, (1080, 720))
    frame = cv2.flip(frame, 1)

    #########################
    # drawing hand landmarks
    #########################
    # detect landmarks
    image, results = detector.findLandmarks(frame)
    # detect landmarks end

    # draw UI
    # input area
    inputArea = Input((600, 0), 400, 100, myEquation)
    inputArea.draw(frame)
    # delete button
    deleteButton = Delete((925, 25), 50, 50)
    deleteButton.draw(frame, deleteButtonImg)
    # buttons
    for button in buttonList:
        button.draw(frame)
    # equal to button
    equalArea = Equals((600, 500), 400, 70)
    equalArea.draw(frame)
    # draw UI end

    # draw landmarks
    if results.multi_hand_landmarks:
        detector.drawLandmarks(frame, results, False, 8, 4, True, True, 50)
        distance = detector.getDistance()
        if distance[0] < 50:
            for i, button in enumerate(buttonList):
                if button.buttonClicked(frame, distance[1], distance[2]) and delayCounter == 0:
                    if myEquation == "Error":
                        myEquation = ""
                    valueAtButtonClicked = buttonListValue[int(i % 4)][int(i / 4)]
                    myEquation += valueAtButtonClicked
                    if valueAtButtonClicked == "AC":
                        myEquation = ""
                if equalArea.equalsClicked(frame, distance[1], distance[2]):
                    try:
                        myEquation = str(eval(myEquation))
                    except:
                        myEquation = "Error"
                if deleteButton.deleteButtonClicked(frame, distance[1], distance[2]) and delayCounter == 0:
                    temp = ""
                    for j in range(0, len(myEquation) - 1):
                        temp += myEquation[j]
                    myEquation = temp
                    delayCounter = 1
            delayCounter = 1

    # Avoid duplicates
    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 5:
            delayCounter = 0
    # draw landmarks end

    cv2.imshow("Raw web cam feed", frame)

    # defining when to close the webcam
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
