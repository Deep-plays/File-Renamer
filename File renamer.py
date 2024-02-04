import os
import tkinter as tk
from tkinter import filedialog

def rename_files(directory_path, message_var):
    try:
        files = os.listdir(directory_path)
        files.sort()

        for i, file_name in enumerate(files, start=1):
            file_path = os.path.join(directory_path, file_name)
            file_base, file_ext = os.path.splitext(file_name)

            # Construct the new filename with a number
            new_file_name = f"{i}{file_ext}"
            new_file_path = os.path.join(directory_path, new_file_name)

            # Check if the original filename already exists
            while os.path.exists(new_file_path) and new_file_path != file_path:
                # If it does and the new name is different from the original name, append a suffix to the filename
                i += 1
                new_file_name = f"{file_base} ({i}){file_ext}"
                new_file_path = os.path.join(directory_path, new_file_name)

            # If the new name is different from the original name, rename the file
            if new_file_path != file_path:
                os.rename(file_path, new_file_path)

        message_var.set("Files renamed successfully.")
    except Exception as e:
        message_var.set(f"An error occurred: {e}")

def browse_button(directory_entry):
    folder_selected = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, folder_selected)

def rename_button_click(directory_entry, message_var):
    directory_path = directory_entry.get()
    if os.path.isdir(directory_path):
        rename_files(directory_path, message_var)
    else:
        message_var.set("Invalid directory path.")

def browse_button_callback(directory_entry):
    folder_selected = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, folder_selected)

def rename_button_click(directory_entry, message_var):
    directory_path = directory_entry.get()
    if os.path.isdir(directory_path):
        rename_files(directory_path, message_var)
    else:
        message_var.set("Invalid directory path.")

# Create the main window
window = tk.Tk()
window.title("File Renamer")

# Create and place widgets
label = tk.Label(window, text="Select a folder:")
label.pack(pady=10)

directory_entry = tk.Entry(window, width=50)
directory_entry.pack(pady=10)

browse_button = tk.Button(window, text="Browse", command=lambda: browse_button_callback(directory_entry))
browse_button.pack(pady=10)

message_var = tk.StringVar()
message_label = tk.Label(window, textvariable=message_var, fg="red")
message_label.pack(pady=10)

rename_button = tk.Button(window, text="Rename Files", command=lambda: rename_button_click(directory_entry, message_var))
rename_button.pack(pady=10)

# Run the main loop
window.mainloop()
