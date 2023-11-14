from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.train(data="data/bath.yaml", epochs=3,device="cpu", project="results")
model.export(format="onnx")
# -v $(pwd)/data:/usr/src/app/data -v $(pwd)/results:/usr/src/app/results

# Dataset 'data/bath.yaml' images not found ⚠️, missing path '/usr/src/app/datasets/data/val/images'

