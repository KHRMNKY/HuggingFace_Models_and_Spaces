import cv2
from ultralytics import YOLO
import numpy as np
import os
import gradio as gr


__file__= "HUGGINGFACE _MODELS_AND_SPACES"
current_dırectory= os.path.dirname(os.path.abspath(__file__))
folder= os.path.join(current_dırectory,"Cattle_Detection_with_YOLOV8")
pt= os.path.join(folder, "best.pt")
py= os.path.join(folder, "Detection_Video.py")
rqrmt= os.path.join(folder, "requirements.txt")
example_video= os.path.join(folder, "/home/kahraman/Masaüstü/HuggingFace_Models_and_Spaces/Cattle_Detection_with_YOLOV8/cow-video-cows-mooing-and-grazing-in-a-field.mp4")


def fonk(video_path):
  
  model=YOLO(pt)
  cap=cv2.VideoCapture(video_path)  

  frame_width = int(cap.get(3)) 
  frame_height = int(cap.get(4))
  size = (frame_width, frame_height)
  output_video= "filename.mp4"
  writer = cv2.VideoWriter(output_video,  
                         cv2.VideoWriter_fourcc(*"DIVX"), 
                         10, size) 

  
  while True:
    ret, frame= cap.read()

    if ret!=True:
      break

    results= model(frame)
    for result in results:
        if result.boxes is not None and len(result.boxes):
            box = result.boxes
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            print(x1, y1, x2, y2)
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        writer.write(frame)
      
      
  writer.release()
  cap.release()
  return output_video
 
demo = gr.Interface(fonk,
                    inputs= gr.Video(),
                    outputs=gr.Video(),
                    examples=[example_video],
                    title= "cows",
                    cache_examples=True)
demo.launch()
    
