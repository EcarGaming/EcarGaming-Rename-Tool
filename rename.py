import os
import sys
import random
import string
import datetime
import exifread

# Find folder path based on executable or script location
folder_path = os.path.dirname(os.path.abspath(sys.executable))

# Define allowed image and video formats
allowed_image_formats = [".jpg", ".jpeg", ".png", ".heic", ".tiff", ".bmp", ".gif"]
allowed_video_formats = [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".mpeg", ".webm"]
allowed_formats = allowed_image_formats + allowed_video_formats

# Generate a random 5-character identifier for this renaming session
unique_identifier = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

# Sort files based on creation or modification time
def get_file_date(file_path):
    try:
        with open(file_path, 'rb') as f:
            tags = exifread.process_file(f, stop_tag="EXIF DateTimeOriginal")
            if "EXIF DateTimeOriginal" in tags:
                return datetime.datetime.strptime(str(tags["EXIF DateTimeOriginal"]), "%Y:%m:%d %H:%M:%S")
    except Exception:
        pass
    return datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

def main():
    print(f"Kører i mappen: {folder_path}")

    # Collect and sort valid files
    files = [
        file_name for file_name in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, file_name)) and
           os.path.splitext(file_name.lower())[1] in allowed_formats
    ]

    if not files:
        print("Ingen understøttede filer fundet i mappen.")
        input("Tryk på Enter for at afslutte...")
        return

    # Sort files by their date (oldest to newest)
    files.sort(key=lambda f: get_file_date(os.path.join(folder_path, f)))

    # Rename files
    for i, file_name in enumerate(files, start=1):
        file_path = os.path.join(folder_path, file_name)
        file_ext = os.path.splitext(file_name)[1].lower()

        # Determine prefix based on file type
        if file_ext in allowed_image_formats:
            prefix = "image"
        elif file_ext in allowed_video_formats:
            prefix = "video"
        else:
            # Skip unsupported files (should not happen due to filtering above)
            continue

        # Generate new file name
        new_file_name = f"{prefix}_{unique_identifier}_{i:04}{file_ext}"
        new_file_path = os.path.join(folder_path, new_file_name)

        try:
            os.rename(file_path, new_file_path)
            print(f"Omdøbt: {file_name} -> {new_file_name}")
        except Exception as e:
            print(f"Fejl ved omdøbning af {file_name}: {e}")

    print("Omdøbning færdig!")
    input("Tryk på Enter for at afslutte...")

if __name__ == "__main__":
    main()
