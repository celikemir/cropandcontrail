import cv2
from collections import deque

class CenterPoint:
    pts = deque(maxlen=2)
    
    def __init__(self,frame,mainframe,startX,startY,endX,endY):
        self.frame = frame
        self.mainframe = mainframe
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY


    def getpoint(self): 
        
        center = None 
        imgray = cv2.cvtColor(self.frame[self.startY:self.endY, self.startX:self.endX], cv2.COLOR_BGR2GRAY) 
        contours , hierarchy = cv2.findContours(imgray,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        self.pts.appendleft(center)
        #print(self.pts)

        cv2.circle(self.mainframe[self.startY:self.endY, self.startX:self.endX], center, 5, (0, 0, 0), -1)

        return center


