import cv2
import numpy

# load images
img1 = cv2.imread("./photos/goodHead.jpg", cv2.IMREAD_COLOR)
img2 = cv2.imread("./photos/badHead.jpg", cv2.IMREAD_COLOR)

# using the haarcascades - frontal face default
# https://github.com/opencv/opencv/tree/master/data/haarcascades
#
# load the cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
#face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
#face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt_tree.xml")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# find the faces in images
faces1 = face_cascade.detectMultiScale(img1, 1.2, 2)
faces2 = face_cascade.detectMultiScale(img2, 1.2, 1)
# draw box around faces

for (x, y, w, h) in faces1:
    cv2.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 0), 2)
for (x, y, w, h) in faces2:
    cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 2)

# show images
cv2.imshow("goodHead", img1)
cv2.imshow("badHead", img2)

# close images
cv2.waitKey(0)
cv2.destroyAllWindows()
