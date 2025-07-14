# 📁 CLI File Mover

A simple command-line utility to move files into folders based on their file extensions using Python's `argparse`.

---

## 🚀 Features

- ✅ Move files from a specified directory to subfolders by extension.
- ✅ Automatically creates destination folders if they don't exist.
- ✅ Lightweight and easy to use.

---

## 🛠️ Usage

```bash
python mover.py --sourcepath <source_path> --mapping <extension:folder> [<extension:folder> ...]
```
## 🔍 Example

```
python mover.py --sourcepath "." --mapping ".png:images .pptx:ppt"
```

This will:
- Move all .png files to the images/ directory
- Move all .pptx files to the ppt/ directory

| Argument       | Description                                      | Default    |
| -------------- | ------------------------------------------------ | ---------- |
| `--sourcepath` | Source folder where files are located            | `images/`  |
| `--mapping`    | Space-separated list of `extension:folder` pairs | *Required* |


## 📋 Notes
- File extensions are case-insensitive.
- If a folder in --mapping does not exist, it will be created.
- Files are moved, not copied.
- Only regular files are processed (directories are ignored).
