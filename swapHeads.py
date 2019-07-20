import cv2
import numpy

# load images
img1 = cv2.imread("./photos/goodHead.jpg", cv2.IMREAD_COLOR)
img2 = cv2.imread("./photos/badHead.jpg", cv2.IMREAD_COLOR)

# show images
cv2.imshow("goodHead", img1)
cv2.imshow("badHead", img2)

# close images
cv2.waitKey(0)
cv2.destroyAllWindows()
