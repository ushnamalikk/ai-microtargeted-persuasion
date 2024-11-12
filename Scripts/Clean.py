import os
import re

def rename_images_in_subfolders(base_path):
    # Iterate through each subdirectory in the base path
    for subfolder in os.listdir(base_path):
        subfolder_path = os.path.join(base_path, subfolder)
        
        # Check if the path is a directory
        if os.path.isdir(subfolder_path):
            print(f"Renaming files in: {subfolder_path}")
            
            # List all files in the subfolder and filter for .mp3 images
            image_files = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f)) and f.endswith('.mp3')]
            
            # Sort image files for consistent renaming order
            image_files.sort()
            
            # Rename each image in the subfolder
            for index, filename in enumerate(image_files):
                old_file_path = os.path.join(subfolder_path, filename)
                new_filename = f"{subfolder}_{index}.mp3"
                new_file_path = os.path.join(subfolder_path, new_filename)
                
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {filename} -> {new_filename}")
    
    print("All images have been renamed successfully.")

# Usage
folder_path = '/home/rafay/LUMS/Projects/PMT/Scripts/Audios/'
rename_images_in_subfolders(folder_path)
