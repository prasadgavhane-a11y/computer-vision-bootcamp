import cv2
import numpy as np


canvas = np.zeros((512,512,3), dtype=np.uint8)

cv2.line(canvas, (0,0), (511, 511), (0,255,0), 5) # canvas, pt1, pt2, color, thickness
cv2.rectangle(canvas, (384,0), (510,128), (255,0,0), -1) # canvas, top-left corner, bottom-right-corner, color in bgr, -1 thickness i.e filled

cv2.putText(canvas, "OpenCV text addition", (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
# canvas/img, text, origin coordinate bottom-left corner, fontFace ,fontScale/dimension , color, thickness 

cv2.imshow("Canvas with Shapes", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()