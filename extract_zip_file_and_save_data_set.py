import os
import zipfile
import shutil

# use recursive function.
def extract_and_delete_zip_file(superfolder_path: str ={}) -> None:
    # serching zip directory
    for folder in os.listdir(superfolder_path):
        if ".zip" in folder:
            with zipfile.ZipFile(os.path.join(superfolder_path,folder), 'r') as zip_ref:
                    zip_ref.extractall(os.path.join(superfolder_path,folder.strip(".zip")))
                    print(f"Extracted files: {zip_ref.namelist()}")
            os.remove(os.path.join(superfolder_path,folder))   
    return None


# use recursive function.
def iterate_save_data_set(superfolder_path: str) -> None:
    
    # serching event.text directory
    for folder in os.listdir(superfolder_path):
        current_sub_event_location = os.path.join(superfolder_path, folder)
        if any('.jpg' in file_name for file_name in os.listdir(current_sub_event_location)):
            for file_name in os.listdir(current_sub_event_location):
                if '.jpg' in file_name and not 'plate.jpg' in file_name:
                    path_component =current_sub_event_location.split("\\")
                    os.makedirs(f"data_{SITE}\\images\\train", exist_ok=True)    # Create the directory if it does not exist 
                    destination_path = os.path.join(f"data_{SITE}\\images\\train", f'{path_component[-1]}_{file_name}')
                    shutil.copy(os.path.join(current_sub_event_location, file_name), destination_path)    
        else:
            iterate_save_data_set(current_sub_event_location)
    return None


SITE='02'
SUPER_COLLECTOR = './raw_data_each_site'
SUPER_FOLDER = os.path.join(SUPER_COLLECTOR,SITE)

# extract_and_delete_zip_file(SUPER_COLLECTOR)
# for i in os.listdir(SUPER_FOLDER):
#     extract_and_delete_zip_file(os.path.join(SUPER_FOLDER, i))
    
iterate_save_data_set(SUPER_FOLDER)