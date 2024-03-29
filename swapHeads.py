import cv2
import numpy

# load images
img1 = cv2.imread("./photos/goodHead.jpg", cv2.IMREAD_COLOR)
img2 = cv2.imread("./photos/badHead.jpg", cv2.IMREAD_COLOR)
good = img1.copy()
bad = img2.copy()

# using the haarcascades - frontal face default
# https://github.com/opencv/opencv/tree/master/data/haarcascades
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
font = cv2.FONT_HERSHEY_SIMPLEX

for (x, y, w, h) in faces1:
    positionString = str(x) + ", " + str(y) + ", " + str(w) + ", " + str(h)
    cv2.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.putText(img1, positionString, (x + w, y + h), font,
                1, (255, 0, 0), 2, cv2.LINE_AA)
goodROI = (730, 46, 100, 100)

for (x, y, w, h) in faces2:
    positionString = str(x) + ", " + str(y) + ", " + str(w) + ", " + str(h)
    cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.putText(img2, positionString, (x + w, y + h), font,
                1, (255, 0, 0), 2, cv2.LINE_AA)
badROI = (715, 0, 120, 120)

# show images
cv2.imshow("goodHead", img1)
cv2.imshow("badHead", img2)

# close images
cv2.waitKey(0)
cv2.destroyAllWindows()

# Off with their head !
goodHead = good[goodROI[1]: goodROI[1] + goodROI[2],
                goodROI[0]: goodROI[0] + goodROI[3]]
badHead = bad[badROI[1]: badROI[1] + badROI[2],
              badROI[0]: badROI[0] + badROI[3]]

cv2.imshow("goodHead", goodHead)
cv2.imshow("badHead", badHead)
cv2.waitKey(0)
cv2.destroyAllWindows()


method = [cv2.INTER_AREA, cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_AREA,
          cv2.INTER_CUBIC, cv2.INTER_LANCZOS4]

for m in method:
    resizedGoodHead = cv2.resize(
        goodHead, (badROI[2], badROI[3]), interpolation=m)

    # SwapHeads
    imgNew = bad

    imgNew[badROI[1]: badROI[1] + badROI[2],
           badROI[0]: badROI[0] + badROI[3]] = resizedGoodHead

    cv2.imshow(f"New Head {m}", imgNew)

cv2.waitKey(0)
cv2.destroyAllWindows()
