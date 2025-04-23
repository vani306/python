import os
import shutil

def copy_file_to_new_subdir(source_dir, filename, new_subdir):

    if not os.path.exists(new_subdir):
        os.makedirs(new_subdir)
        print(f"Created new subdirectory: {new_subdir}")
    
    source_path = os.path.join(source_dir, filename)
    dest_path = os.path.join(new_subdir, filename)
                             
    if os.path.isfile(source_path):
        shutil.copy(source_path, dest_path)
        print(f"Copied '{filename}' from '{source_dir}' to '{new_subdir}'")
    else:
        print(f"File '{filename}' not found in '{source_dir}'.")

source_directory = 'source_folder'       
file_to_copy = 'example.txt'             
destination_subdirectory = 'new_folder'

copy_file_to_new_subdir(source_directory, file_to_copy, destination_subdirectory)
