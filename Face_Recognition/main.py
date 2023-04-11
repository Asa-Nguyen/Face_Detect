import cv2
import dlib

img = cv2.imread("bomman.jpg")

#convert img to process
gray = cv2.cvtColor(src = img , code = cv2.COLOR_BGR2GRAY)

#Find Face
face_detect = dlib.get_frontal_face_detector()
faces = face_detect(gray)
for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
    cv2.rectangle(img = img , pt1 = (x1,y1) , pt2=(x2,y2) , color = (0,255,0), thickness = 3 )
    

#show image
cv2.imshow(winname="Find Face",mat=img) 

#wait for user press the key to exit
cv2.waitKey(delay=0)

#Close App
cv2.destroyAllWindows()

