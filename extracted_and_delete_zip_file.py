import os
import zipfile

# use recursive function.
def extracted_and_delete_zip_file(superfolder_path: str ={}) -> None:
    # serching zip directory
    for folder in os.listdir(superfolder_path):
        if ".zip" in folder:
            with zipfile.ZipFile(os.path.join(superfolder_path,folder), 'r') as zip_ref:
                    zip_ref.extractall(os.path.join(superfolder_path,folder.strip(".zip")))
                    print(f"Extracted files: {zip_ref.namelist()}")
            os.remove(os.path.join(superfolder_path,folder))   
    return None

# extracted_and_delete_zip_file('./raw_data_each_site')

SUPER_FOLDER ="./raw_data_each_site/01"
for i in os.listdir(SUPER_FOLDER):
    extracted_and_delete_zip_file(os.path.join(SUPER_FOLDER, i))