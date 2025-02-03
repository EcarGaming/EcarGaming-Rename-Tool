# EcarGaming-Rename-Tool
EcarGaming Rename Tool is a simple program that automatically renames image and video files based on their capture date. It supports multiple formats like JPG, HEIC, PNG, MP4, and MOV. If a file lacks metadata, it is marked as "NoDate". The tool works by placing it directly in the folder containing the files.


Program Name: EcarGaming Rename Tool

Description:
This program automatically renames image and video files in the folder where it is executed. It supports a wide range of file formats and ensures that all files are renamed in a consistent and organized manner.

How it works:
1. The program scans all image and video files in the folder.
2. Files are sorted by capture date (if available) or by their last modification date.
3. Each file is renamed using the following format:
   - Images: `image_<unique code>_<sequence number>.ext`
   - Videos: `video_<unique code>_<sequence number>.ext`
   - Unique code is a random 5-character alphanumeric string that remains the same for all files during a renaming session.
   - Sequence number starts at 0001 and increments by 1 for each file.

Supported file formats:
- Images: `.jpg`, `.jpeg`, `.png`, `.heic`, `.tiff`, `.bmp`, `.gif`
- Videos: `.mp4`, `.mov`, `.avi`, `.mkv`, `.wmv`, `.flv`, `.mpeg`, `.webm`

Note:
- Files that are not in the supported formats will be ignored.
- If the program cannot find the capture date for a file, the file's last modification date is used instead.

How to use:
1. Copy the program (`rename.exe`) to the desired folder.
2. Double-click the program to execute it.
3. Follow the on-screen instructions.

For questions or support, contact EcarGaming.
