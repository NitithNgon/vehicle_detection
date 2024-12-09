import os
from ultralytics import YOLO
import cv2


VIDEOS_DIR = os.path.join('.', 'test_image')

image_path = os.path.join(VIDEOS_DIR, 'test2')
image_path_out = os.path.join(VIDEOS_DIR, 'result2')

model_path = os.path.join('.', 'runs', 'detect', 'train', 'weights', 'last.pt')

# Load a model
model = YOLO(model_path)  # load a custom model

# Threshold for object detection
threshold = 0.0

# Process all images in the input folder
for file_name in os.listdir(image_path):
    if file_name.lower().endswith((".jpg", ".jpeg", ".png")):
        # Input image path
        input_path = os.path.join(image_path, file_name)

        # Read the image
        image = cv2.imread(input_path)
        if image is None:
            print(f"Error: Unable to read image {input_path}")
            continue

        # Run YOLO model on the image
        results = model(image)[0]

        # Draw detections on the image
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result
            if score > threshold:
                # Draw rectangle
                cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

                # Add label
                label = f"{results.names[int(class_id)].upper()} {score:.2f}"
                cv2.putText(image, label, (int(x1), int(y2) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Save the resulting image to the output folder
        base_name, ext = os.path.splitext(file_name)
        output_path = os.path.join(image_path_out, "{}_out{}".format(base_name, ext))
        cv2.imwrite(output_path, image)
        print(f"Processed and saved: {output_path}")