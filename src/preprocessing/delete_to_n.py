import os
import random

# Folder which houses all subdirectories to be purged
parent_folder = '../../dataset/train'

# List of subdirectories in the parent folder
folders = os.listdir(parent_folder)

# Set the target number of images (# of images that will remain)
target_num = 5000

# Iterate through each folder that contains images
for folder in folders:
    folder_path = os.path.join(parent_folder, folder)

    # List all files wihtin the current folder
    files = os.listdir(folder_path)

    image_files = [file for file in files if file.lower().endswith('.jpg')]

    # Check how many images are in the directory
    num_images = len(image_files)

    # If the number of images is greater than the target number, proceed to randomly delete files
    if num_images > target_num:
        # Calculate how many images need to be deleted
        images_to_delete = num_images - target_num
        
        # Randomly select images to delete
        images_to_delete_list = random.sample(image_files, images_to_delete)
        
        # Delete the selected images
        for image in images_to_delete_list:
            os.remove(os.path.join(folder_path, image))

        print(f"{images_to_delete} images deleted from {folder}. Now there are {target_num} images left.")
    else:
        print(f"No need to delete images from {folder}. The folder contains {num_images} images, which is less than or equal to {target_num}.")

