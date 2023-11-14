from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.train(data="dataset/bath.yaml", epochs=3,device="cpu", project="results")
model.export(format="onnx")