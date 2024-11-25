import os
import shutil

# use recursive function.
def iterate_save_data_set(superfolder_path: str) -> None:
    
    # serching event.text directory
    for folder in os.listdir(superfolder_path):
        current_sub_event_location = os.path.join(superfolder_path, folder)
        if any('.jpg' in file_name for file_name in os.listdir(current_sub_event_location)):
            for file_name in os.listdir(current_sub_event_location):
                if '.jpg' in file_name and not 'plate.jpg' in file_name:
                    path_component =current_sub_event_location.split("\\")
                    destination_path = os.path.join("data\\images\\train", f'{path_component[1]}_{file_name}')
                    shutil.copy(os.path.join(current_sub_event_location, file_name), destination_path)    
        else:
            iterate_save_data_set(current_sub_event_location)
    return None

iterate_save_data_set("raw_data_set")