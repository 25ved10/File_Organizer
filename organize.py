#protptype

import os
import glob
import shutil

#Downloads folder orgnizing
source_path = "D:\Downloads" 
file_type = ["*.otf", "*.png", "*.jpg", "*.webp", "*.pdf", "*.zip", "*.mp3", "*.mp4"] #otf = font

destination_path = "D:\Downloads\PDF"


allfiles = glob.glob(os.path.join(source_path, '*.pdf'), recursive=True)
print("Files to move", allfiles)

for file_path in allfiles:
    dst_path = os.path.join(destination_path, os.path.basename(file_path))
    shutil.move(file_path, dst_path)
    print(f"Moved {file_path} -> {dst_path}")
