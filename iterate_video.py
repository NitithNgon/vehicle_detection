import os
import shutil
from extract_frame import extract_frames

# use recursive function.
def iterate_save_data_set(superfolder_path: str) -> None:
    # serching event.text directory
    for folder in os.listdir(superfolder_path):
        current_sub_event_location = os.path.join(superfolder_path, folder)
        if 'event.txt' in os.listdir(current_sub_event_location):
            if 'video.mp4' in os.listdir(current_sub_event_location):
                video_path = os.path.join(current_sub_event_location, 'video.mp4')
                extract_frames(video_path, 2)
        else:
            iterate_save_data_set(current_sub_event_location)
    return None

iterate_save_data_set("C:\\Users\\eei-0\\Desktop\\python code\\assignment1\\to_Peiam")