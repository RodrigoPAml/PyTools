import mss
import numpy as np
import cv2

'''
Class to template match an image
'''
class TemplateMatcher:
    def __init__(self, template_image_path):
        self.template = cv2.imread(template_image_path, cv2.IMREAD_COLOR)
        
        if self.template is None:
            raise ValueError(f"Template image not found at {template_image_path}")
        
        self.template_gray = cv2.cvtColor(self.template, cv2.COLOR_BGR2GRAY)
        
        self.w, self.h = self.template_gray.shape[::-1]

    def match(self, frame, threshold=0.9):
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        result = cv2.matchTemplate(frame_gray, self.template_gray, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)

        bounding_boxes = []
        for pt in zip(*loc[::-1]):
            bounding_boxes.append((pt[0], pt[1], pt[0] + self.w, pt[1] + self.h))
        
        return bounding_boxes

    def draw_bounding_boxes(self, frame, bounding_boxes):
        for (x1, y1, x2, y2) in bounding_boxes:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        return frame
