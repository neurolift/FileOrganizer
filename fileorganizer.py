import os
import shutil
FILE_CATEGORIES = {
"Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
"Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
"Spreadsheets": [".xls", ".xlsx", ".csv", ".ods"],
"Presentations": [".ppt", ".pptx", ".odp"],
"Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
"Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
"Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
"Code": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css"],
"Executables": [".exe", ".msi", ".apk", ".bat", ".sh"],
"System": [".dll", ".sys", ".tmp", ".log"],
"Others": []  # fallback category
}

def get_folder():
    folder_name = input("Enter the folder name on your Desktop: ").strip()
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    path = os.path.join(desktop, folder_name)

    if not os.path.exists(path):
        print(f"❌ Error: The folder '{folder_name}' was not found at {path}")
        return
    items = os.listdir(path)   # get everything inside the folder
    files=[]
    for item in items:
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            print("File:", item)
            files.append(item)
        elif os.path.isdir(full_path):
            print("Folder:", item)
    categorize(files,path)
def categorize(files, path):
    count=0
    for file_item in files:
        extensions = os.path.splitext(file_item)[1].lower() 
        found = False  # fall back if no match
        
        for category in FILE_CATEGORIES:
            if extensions in FILE_CATEGORIES[category]:
                dest_dir = os.path.join(path, category)
                source = os.path.join(path, file_item)
                
                os.makedirs(dest_dir, exist_ok=True) 
                move(dest_dir, source)
                count += 1
                found = True 
                break       

        if not found:
            others_dir = os.path.join(path, "Others")
            os.makedirs(others_dir, exist_ok=True)
            source = os.path.join(path, file_item)
            move(others_dir, source)
            count+=1
            print(f"No category for {file_item}, moved to Others.")       
    print(f"\n✅ Done! Successfully organized {count} files.")

def move(dest_dir,source):
    shutil.move(source, dest_dir)

if __name__=="__main__":
    get_folder()