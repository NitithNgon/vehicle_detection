from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.yaml")  # build a new model from YAML

# Train the model
results = model.train(data="config.yaml", epochs=100)  #, imgsz=640 (downscale)

# Start training from a pretrained *.pt model
# yolo detect train data=config.yaml model=yolo11n.pt epochs=100 imgsz=640