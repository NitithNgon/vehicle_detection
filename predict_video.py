import os
from ultralytics import YOLO
import cv2


VIDEOS_DIR = os.path.join('.', 'videos')

file_name='truck3'
video_path = os.path.join(VIDEOS_DIR, '{}.mp4'.format(file_name))
video_path_out = os.path.join(VIDEOS_DIR, '{}_out.mp4'.format(file_name) )

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
H, W, _ = frame.shape
print(frame.shape)
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

model_path = os.path.join('.', 'runs', 'detect', 'train', 'weights', 'best.pt')

# Load a model
model = YOLO(model_path)  # load a custom model

threshold = 0.0
try:
    while ret:
        # H = 736
        # W = 1280
        results = model(frame, imgsz=(H, W))[0]

        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result

            if score > threshold:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                cv2.putText(frame, '{}-{}'.format(results.names[int(class_id)].upper(), score), (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

        out.write(frame)
        ret, frame = cap.read()
finally:
    cap.release()
    out.release()
    cv2.destroyAllWindows()
print(f"Video saved to: {video_path_out}")