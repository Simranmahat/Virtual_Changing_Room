import cv2
import  cvzone
import sys
CurrentProduct=sys.argv[1]
int(CurrentProduct)
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')



while True:
    k=cv2.waitKey(100)
    
 
    
   
    overlay = cv2.imread('FilterApply/Glasses/glass{}.png'.format(str(CurrentProduct)), cv2.IMREAD_UNCHANGED)
         
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for (x, y, w, h) in faces:
        #cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
        overlay_resize = cv2.resize(overlay,(w,int(h*0.8)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x, y])
    cv2.imshow('Virtual Changing Room-Opera', frame)
    if cv2.waitKey(10) == ord('q') :
        break
  
cap.release()
cv2.destroyAllWindows()
