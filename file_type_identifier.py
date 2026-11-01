
filename = input("Enter file name: ")

extension = filename.split(".")[-1].lower()

file_types = {
    "pdf": "PDF Document",
    "txt": "Text File",
    "jpg": "Image File",
    "jpeg": "Image File",
    "png": "Image File",
    "py": "Python File",
    "docx": "Word Document",
    "mp3": "Audio File",
    "mp4": "Video File",
    "zip": "Compressed File"
}

if extension in file_types:
    print("File Type:", file_types[extension])
else:
    print("Unknown File Type")
