from ultralytics import YOLO
# model = YOLO("./model/best.pt") # bath-val
model = YOLO("./results/train/weights/best.pt") # bath-val3
model.val(project="results")