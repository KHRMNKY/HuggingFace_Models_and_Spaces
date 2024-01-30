import cv2
from ultralytics import YOLO

model=YOLO("/home/kahraman/Masaüstü/best.pt")

cap=cv2.VideoCapture(0)

while cap:
    ret, frame= cap.read()
    if not ret:
      break

    results = model(frame)
    cv2.imshow("img", frame)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()