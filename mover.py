## A CLI-Based File Mover Using argparse

import os
import shutil
import argparse

parser = argparse.ArgumentParser(description="CLI-File-Mover")

parser.add_argument("--sourcepath", help="source path of files you want to move", default='images/')
parser.add_argument("--mapping", help="map file type to folder")

args = parser.parse_args()

# python mover.py --sourcepath " " --mapping ".png:images .pptx:ppt"
# general cmd: 'python mover.py --sourcepath <source_path_of_files_to_move> --mapping <extension:folder_to_move_to>

source_path = args.sourcepath.strip()
if not source_path:
    source_path = "."

mapping_list = str(args.mapping).split()
mapping_dict = {item.split(":")[0].lstrip(".").lower(): item.split(":")[1] for item in mapping_list}

print(mapping_list)


for filename in os.listdir(source_path):
    full_path = os.path.join(source_path, filename)
    if os.path.isfile(full_path):
        ext = os.path.splitext(filename)[1].lstrip('.').lower()
        if ext in mapping_dict:
            dest_dir = mapping_dict[ext]
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(full_path, os.path.join(dest_dir, filename))
            print(f"Moved {filename} to {dest_dir}/")

