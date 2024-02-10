import cv2
from ultralytics import YOLO
import numpy as np
import os

__file__= "HUGGINGFACE _MODELS_AND_SPACES"
current_dırectory= os.path.dirname(os.path.abspath(__file__))
folder= os.path.join(current_dırectory,"yolov8_model_on_custom_data")
pt= os.path.join(folder, "best.pt")
video= os.path.join(folder, "cow-video-cows-mooing-and-grazing-in-a-field.mp4")
py= os.path.join(folder, "yolo.py")
rqrmt= os.path.join(folder, "requirements.txt")



model=YOLO(pt)

source=video

cap = cv2.VideoCapture(source)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)
    for result in results:
        box=result.boxes
        
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("img", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
