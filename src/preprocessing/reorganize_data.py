import os
import shutil
import time

# Code by ChatGPT o1-preview

def extract_class_label(filename):
    """
    Extract the class label from the filename.
    Assumes the filename format is: <ID>-<CLASS>.jpg
    """
    # Split the filename at the first dash
    parts = filename.split('-', 1)
    if len(parts) > 1:
        # The class label is everything after the first dash, without the file extension
        class_label_with_ext = parts[1]
        class_label = os.path.splitext(class_label_with_ext)[0]
        return class_label
    else:
        # If no dash is found, use the entire filename without extension
        class_label = os.path.splitext(filename)[0]
        return class_label

# Paths to your datasets
data_dirs = ['../../dataset/validation', '../../dataset/test']  # Update paths as needed

for data_dir in data_dirs:
    print(f"Processing directory: {data_dir}")

    start = time.time()

    # List all files in the directory
    file_list = os.listdir(data_dir)
    
    for filename in file_list:
        # Full path to the file
        file_path = os.path.join(data_dir, filename)
        if os.path.isfile(file_path):
            # Skip hidden files or system files
            if filename.startswith('.'):
                continue
            # Extract the class label from the filename
            class_label = extract_class_label(filename)
            # Directory for the class
            class_dir = os.path.join(data_dir, class_label)
            # Create the class directory if it doesn't exist
            os.makedirs(class_dir, exist_ok=True)
            # Destination path for the file
            dest_path = os.path.join(class_dir, filename)
            # Move the file to the class directory
            shutil.move(file_path, dest_path)
        else:
            print(f"Skipping {file_path}, not a file")
    
    end = time.time()

    print(f"Successfully processed directory: {data_dir} in {round(end - start)} seconds")
