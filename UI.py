import cv2


class Button:
    def __init__(self, position, width, height, text):
        self.position = position
        self.width = width
        self.height = height
        self.text = text

    def draw(self, image):
        # button
        cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                      (215, 215, 215), cv2.FILLED)
        # border
        cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                      (50, 50, 50), 3)
        # text
        cv2.putText(image, self.text, (self.position[0] + 20, self.position[1] + 40), cv2.FONT_HERSHEY_PLAIN, 2,
                    (50, 50, 50), 2)

    def buttonClicked(self, image, x, y):
        if self.position[0] < x < self.position[0] + self.width and \
                self.position[1] < y < self.position[1] + self.height:
            cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                          (255, 255, 255), cv2.FILLED)
            # border
            cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                          (50, 50, 50), 3)
            # text
            cv2.putText(image, self.text, (self.position[0] + 10, self.position[1] + 70), cv2.FONT_HERSHEY_PLAIN, 5,
                        (0, 0, 0), 5)
            return True
        else:
            return False


class Input:
    def __init__(self, position, width, height, text):
        self.position = position
        self.width = width
        self.height = height
        self.text = text

    def draw(self, image):
        cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                      (255, 255, 255), cv2.FILLED)
        cv2.rectangle(image, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(image, self.text, (self.position[0] + 10, self.position[1] + 70), cv2.FONT_HERSHEY_PLAIN, 2,
                    (50, 50, 50), 2)
