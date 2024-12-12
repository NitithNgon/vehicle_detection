import cv2
import os
import shutil

# Configuration
SUPER_FOLDER ='./data_01'
IMAGES_DIR = os.path.join(SUPER_FOLDER,'./images/train')  # Path to folder with images
OUTPUT_DIR = os.path.join(SUPER_FOLDER,'./labels/train')  # Path to save label files
IMAGES_VAL_DIR = os.path.join(SUPER_FOLDER,'./images/val')  # Path to folder with images
CLASS_NAMES = [
    'truck',
]

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Global variables for bounding box drawing
drawing = False
ix, iy = -1, -1
bboxes = []
current_class = 0  # Default class index

def draw_bbox(event, x, y, flags, param):
    global ix, iy, drawing, bboxes
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button pressed
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:  # Mouse moving
        if drawing:
            image_copy = img.copy()
            cv2.rectangle(image_copy, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow('Image', image_copy)
    elif event == cv2.EVENT_LBUTTONUP:  # Left mouse button released
        drawing = False
        x_min, y_min = min(ix, x), min(iy, y)
        x_max, y_max = max(ix, x), max(iy, y)
        bboxes.append((x_min, y_min, x_max, y_max, current_class))
        cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        cv2.imshow('Image', img)

# Loop through all images
for file_name in os.listdir(IMAGES_DIR):
    if not file_name.endswith(('.jpg', '.png', '.jpeg')):
        continue
    
    image_path = os.path.join(IMAGES_DIR, file_name)
    if os.path.splitext(file_name)[0]+".txt" in os.listdir(OUTPUT_DIR):
        continue

    # !remove when label val images
    elif len(os.listdir(OUTPUT_DIR))>1000:
        shutil.move(image_path, IMAGES_VAL_DIR)
        print(f"File {file_name} moved to {IMAGES_VAL_DIR}")
        continue

    img = cv2.imread(image_path)
    h, w, _ = img.shape
    bboxes = []

    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', draw_bbox)

    print(f"Labeling {file_name}. Press 's' to save, 'n' for next, or 'q' to quit.")
    while True:
        cv2.imshow('Image', img)
        key = cv2.waitKey(1)

        if key == ord('c'):  # Switch class
            current_class = (current_class + 1) % len(CLASS_NAMES)
            print(f"Selected class: {CLASS_NAMES[current_class]}")

        elif key == ord('n'):  # Skip to next image
            print("Skipping to next image...")
            break

        elif key == ord('s'):  # Save annotations
            label_file_path = os.path.join(OUTPUT_DIR, file_name.replace('.jpg', '.txt').replace('.png', '.txt'))
            with open(label_file_path, 'w') as f:
                for bbox in bboxes:
                    x_min, y_min, x_max, y_max, class_id = bbox
                    x_center = (x_min + x_max) / 2 / w
                    y_center = (y_min + y_max) / 2 / h
                    box_width = (x_max - x_min) / w
                    box_height = (y_max - y_min) / h
                    f.write(f"{class_id} {x_center} {y_center} {box_width} {box_height}\n")
            print(f"Saved annotations for {file_name}")
            break

        elif key == ord('q'):  # Quit program
            print("Exiting...")
            cv2.destroyAllWindows()
            exit()

cv2.destroyAllWindows()
