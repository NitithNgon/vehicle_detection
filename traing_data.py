from ultralytics import YOLO
import os



# Load a model
model = YOLO("yolo11n.yaml")  # build a new model from YAML

# Train the model
results = model.train(data="config.yaml", epochs=100)  #, imgsz=640 (downscale)

# Start training from a pretrained *.pt model
# yolo detect train data=config.yaml model=yolo11n.pt epochs=100 imgsz=640




# # train exiting model
# model_path = os.path.join('.', 'runs', 'detect', 'train', 'weights', 'last.pt')

# # Load the pre-trained model
# model = YOLO(model_path)

# # Train on a new dataset
# model.train(
#     data="config.yaml",        # Path to data.yaml
#     epochs=50,                 # Number of epochs to train
#     imgsz=640,                 # Image size
#     lr0=0.001,                 # Learning rate (optional)
# )
