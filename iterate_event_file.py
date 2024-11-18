import os
from typing import (
    List, 
    Dict,
    Any,
)

# use recursive function.
def iterate_event_file(superfolder_path: str ={}) -> None:
    
    # serching event.text directory
    for folder in os.listdir(superfolder_path):
        current_sub_event_location = os.path.join(superfolder_path, folder)
        if any(
            "_1.jpg" in file_name and
            "_2.jpg" in file_name and
            "_3.jpg" in file_name and
            "_4.jpg" in file_name
            for file_name in os.listdir(current_sub_event_location)
            ):
            # 123
            pass
            
            
        else:
            iterate_event_file(current_sub_event_location)
    return None