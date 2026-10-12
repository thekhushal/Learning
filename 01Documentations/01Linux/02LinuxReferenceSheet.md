# Linux Commands Cheat Sheet (Data Science)

# 1. Open JupyterLab in Browser

```bash
jupyter lab --port=8888 --no-browser --allow-root
```

---

# 2. Download Datasets from a Direct Link

```bash
wget "link"
```

Resume an interrupted download:

```bash
wget -c "link"
```

Save with a different filename:

```bash
wget -O filename.csv "link"
```

> **Note:** `wget` works only when the URL points directly to the file.

---

# 3. Download Datasets from Google Drive

## Single File

```bash
gdown "google_drive_link"
```

## Entire Folder

```bash
gdown --folder "google_drive_folder_link"
```

> **Note:** Use `gdown` when the dataset is hosted on Google Drive instead of a direct download URL.

---

# 4. Clone a GitHub Repository

```bash
git clone repository_url
```

Example:

```bash
git clone https://github.com/user/project.git
```

---

# 5. Create a Python Virtual Environment

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Deactivate it:

```bash
deactivate
```

---

# 6. Install Python Packages

Install a package:

```bash
pip install package_name
```

Install packages from a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Generate a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

---

# 7. Navigate Directories

Show current directory:

```bash
pwd
```

List files and folders:

```bash
ls
```

Detailed list (including hidden files):

```bash
ls -la
```

Change directory:

```bash
cd folder_name
```

Go back one directory:

```bash
cd ..
```

Go to the home directory:

```bash
cd ~
```

---

# 8. Create and Remove Directories

Create a directory:

```bash
mkdir folder_name
```

Create nested directories:

```bash
mkdir -p parent/child
```

Remove an empty directory:

```bash
rmdir folder_name
```

Remove a directory and all its contents:

```bash
rm -rf folder_name
```

---

# 9. Copy and Move Files

Copy a file:

```bash
cp source destination
```

Copy a directory:

```bash
cp -r source_folder destination
```

Move or rename a file:

```bash
mv old_name new_name
```

---

# 10. Delete Files

Delete a file:

```bash
rm filename
```

Delete multiple files:

```bash
rm file1 file2
```

---

# 11. Search for Files

Find a file by name:

```bash
find . -name "filename"
```

Find all CSV files:

```bash
find . -name "*.csv"
```

---

# 12. Extract Compressed Files

Extract a ZIP archive:

```bash
unzip file.zip
```

Extract a `.tar.gz` archive:

```bash
tar -xzf file.tar.gz
```

---

# 13. Check Python and pip

Python version:

```bash
python3 --version
```

pip version:

```bash
pip --version
```

List installed Python packages:

```bash
pip list
```

---

# 14. Check Disk Usage

Show the size of the current directory:

```bash
du -sh .
```

Show disk usage:

```bash
df -h
```

---

# 15. Check Running Processes

List all running processes:

```bash
ps aux
```

Interactive process monitor:

```bash
htop
```

---

# 16. Kill a Process

Terminate a process:

```bash
kill PID
```

Force terminate a process:

```bash
kill -9 PID
```
