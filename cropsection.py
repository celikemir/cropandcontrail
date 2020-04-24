import cv2


class CropRegion:
    def __init__(self,frame,mainframe):
        self.frame = frame
        self.mainframe = mainframe
        self.roi_x=0
        self.roi_y=0
        self.roi_w=0
        self.roi_h=0


    def select(self):
       
        ROI = cv2.selectROI("Alan Secimi", self.frame, False, False)
        self.roi_x = ROI[0]
        self.roi_y = ROI[1]
        self.roi_w = ROI[2]
        self.roi_h = ROI[3]

        cv2.destroyAllWindows()
       
        selected_region = [self.roi_x, self.roi_y, self.roi_w, self.roi_h]
        cv2.rectangle(self.mainframe, (selected_region[0], selected_region[1]),(selected_region[0] + selected_region[2], selected_region[1] + selected_region[3]), (0, 0, 255), 2)

        return selected_region

    