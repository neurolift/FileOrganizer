📂 Simple File Organizer
A Python script that cleans up your folders by sorting files into categories (Images, Documents, Code, etc.) based on their file extensions.

🚀 How to Use
Run the script: Open your terminal or IDE and run python your_script_name.py.

Enter Folder Name: Type the name of the folder on your Desktop you want to organize.

Sit Back: The script will automatically create sub-folders and move your files into them.

📁 How Files are Sorted
The script looks at the end of your filename (the extension) and matches it to a category:

Images: .jpg, .png, .gif, etc.

Documents: .pdf, .docx, .txt, etc.

Code: .py, .html, .js, etc.

Others: Any file that doesn't match a specific category.

🛠️ Requirements
Python 3.x

No extra libraries needed (uses built-in os and shutil).

⚠️ Safety Notes
The script only moves files. It will not touch or move existing folders.

If a file doesn't have an extension, it safely goes into the Others folder.