import cv2
import base64

def frame_to_base64(frame):
    _, buffer = cv2.imencode('.jpg', frame)
    base64_string = base64.b64encode(buffer).decode("utf-8")
    return base64_string

def video_frames_to_base64(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Couldn't open the video file")
        return

    base64_strings = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        base64_strings.append(frame_to_base64(frame))

    cap.release()
    return base64_strings

def write_base64_to_file(base64_strings, output_file):
    with open(output_file, "w") as txt_file:
        for base64_string in base64_strings:
            txt_file.write(base64_string)
            txt_file.write("\n\n")  # Add a newline between each base64 string

# Path to the video file
video_path = "C:\\Users\\samke\\Videos\\Vengeance.mp4"  # Replace with your video file path

# Convert video frames to base64
base64_strings = video_frames_to_base64(video_path)

# Output text file to store base64 strings
output_file = "C:\\Users\\samke\\Pictures\\results.txt"  # Replace with desired output file name

# Write base64 strings to a text file
write_base64_to_file(base64_strings, output_file)

print("Base64 strings of all video frames have been written to", output_file)
