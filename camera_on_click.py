import cv2

cap = cv2.VideoCapture('Wildlife.mp4')

while (cap.isOpened()):
   ret, frame = cap.read()
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   cv2.imshow('frame', gray)
   if cv2.waitKey(1) & 0xFF == ord('q'):
       break

   while cv2.waitKey(1) & 0xFF != ord(' '):
       pass
cap.release()
cv2.destroyAllWindows()
