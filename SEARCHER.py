import base64
import os


def file_to_base64(file_path):
    with open(file_path, "rb") as file:
        base64_string = base64.b64encode(file.read()).decode("utf-8")
    return base64_string


def find_matching_text(base64_string, text_files_folder):
    # Get a list of all text files in the folder
    text_files = [f for f in os.listdir(text_files_folder) if f.endswith(".txt")]

    # Search for the base64 string in each text file
    matching_files = []
    for text_file in text_files:
        with open(os.path.join(text_files_folder, text_file), "r") as file:
            content = file.read()
            if base64_string in content:
                matching_files.append(text_file)

    return matching_files


# Path to the image or video file you want to convert
file_path = "C:\\Users\\samke\\Pictures\\New folder\\frame_507.jpg"  # Replace with your file path

# Convert the file to base64
base64_string = file_to_base64(file_path)

# Folder containing text files to search for matching text
text_files_folder = "C:\\Users\\samke\\Pictures\\source"  # Replace with the folder containing your text files

# Find text files containing the matching base64 string
matching_files = find_matching_text(base64_string, text_files_folder)

if matching_files:
    print("Matching text found in the following files:")
    for file in matching_files:
        print(file)
else:
    print("No matching text found in any of the files.")
