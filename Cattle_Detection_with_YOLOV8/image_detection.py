import cv2
from ultralytics import YOLO
import gradio as gr
import os


__file__= "HUGGINGFACE _MODELS_AND_SPACES"
current_dırectory= os.path.dirname(os.path.abspath(__file__))
folder= os.path.join(current_dırectory,"Cattle_Detection_with_YOLOV8")
pt= os.path.join(folder, "best.pt")
py= os.path.join(folder, "image_detection.py")
rqrmt= os.path.join(folder, "requirements.txt")
example_img= os.path.join(folder, "images.jpeg")


def fonk(img_path):
  
    model=YOLO(pt) 
    
    img= cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

    results= model(img)
    for result in results:
        if result.boxes is not None and len(result.boxes):
            box = result.boxes
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            print(x1, y1, x2, y2)
            img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return img


demo = gr.Interface(fonk,
                    inputs= gr.Image(type="filepath", label= "Input image"),
                    outputs=gr.Image(label= "Output image"),
                    examples= [example_img],
                    title= "Detection Cattle from Image"
                    )
demo.launch()
    
