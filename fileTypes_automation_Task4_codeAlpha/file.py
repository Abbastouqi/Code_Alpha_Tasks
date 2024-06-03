import os
import shutil
import logging

def organize_files(directory):
    logging.basicConfig(filename='file_organizer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Define the mapping of file extensions to folder names
    file_types = {
        'txt': 'textfiles',
        'jpg': 'images',
        'jpeg': 'images',
        'png': 'images',
        'gif': 'images',
        'pdf': 'PDFs',  # Assuming PDFs is the intended folder name
        'docx': 'Documents',  # Assuming Documents is the intended folder name
        'xlsx': 'Spreadsheets',  # Assuming Spreadsheets is the intended folder name
        'csv': 'Spreadsheets',  # Assuming Spreadsheets is the intended folder name
        'mp3': 'Audio',  # Assuming Audio is the intended folder name
        'mp4': 'Videos',  # Assuming Videos is the intended folder name
        'zip': 'Archives',  # Assuming Archives is the intended folder name
        # Add more extensions and their corresponding folders as needed
    }

    for filename in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, filename)):
            continue

        file_extension = filename.split('.')[-1].lower()

        if file_extension in file_types:
            folder_name = file_types[file_extension]
            folder_path = os.path.join(directory, folder_name)

            if not os.path.exists(folder_path):
                try:
                    os.makedirs(folder_path)
                    logging.info(f"Created directory: {folder_path}")
                except Exception as e:
                    logging.error(f"Failed to create directory {folder_path}: {e}")
                    continue

            try:
                shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))
                logging.info(f"Moved {filename} to {folder_path}")
                print(f"Moved {filename} to {folder_path}")
            except Exception as e:
                logging.error(f"Failed to move {filename} to {folder_path}: {e}")

if __name__ == "__main__":
    directory_to_organize = r'E:\file types'  # Use raw string to avoid escape sequence issues
    organize_files(directory_to_organize)
