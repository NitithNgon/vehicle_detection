import cv2
import os
import math
OUTPUT_FOLDER = './raw_data_set_2_from_video'

def extract_frames(video_path , interval=1):
    # Create output folder if it doesn't exist
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file")
        return

    frame_count = 0
    fps = cap.get(cv2.CAP_PROP_FPS)
    print ("Actual frame rate: ",fps)
    fps = round(fps, 0)
    print ("Calculate fps:", fps)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        #print ("current frame", frame_count)

        # Calculate time in seconds
        current_time = frame_count / fps
        #print (current_time)
        # Check if the current time is a multiple of the interval
        if frame_count % (fps*interval) == 0:
            # Save the frame
            path_component = (video_path.split('\\'))
            file_name = path_component[-2]
            output_path = os.path.join(OUTPUT_FOLDER, f"{file_name}_frame_{frame_count}.jpg")
            cv2.imwrite(output_path, frame)

    # Release video capture object
    cap.release()
    print(f"Frames extracted at {interval} second interval and saved to {OUTPUT_FOLDER}")