import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import json
import os

window = tk.Tk()
window.title("My First Tkinter App")
window.geometry("400x300")

label = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=20)

entry_frame = tk.Frame(window)
entry_frame.pack(pady=20, padx=20, fill="x")

entry = tk.Entry(entry_frame, width=30)
entry.pack(side="left", fill="x", expand=True)

button = tk.Button(entry_frame, text="Submit", command=lambda:browse_folder())
button.pack(side="left", padx=(10,0))

options = ["Option1", "Option2", "Option3"]
dropdown = ttk.Combobox(window, values=options, state="readonly")
dropdown.pack()

def save_json():
    data = entry.get().strip()

    if not data:
        messagebox.showerror("warning", "Please enter some text!")
    
    user_data = {
        "text": data
    }
    
    try:
        existing_data = user_data

        with open("data.json", "w") as file:
            json.dump(existing_data, file, indent=4)
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {str(e)}")

def browse_file():
    """Open file explorer and get file path"""

    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[
            ("All files", "*.*"),
            ("Text files", "*.txt"),
            ("Python files", "*.py"),
            ("Image files", "*.png;*.jpg;*.jpeg;*.gif")
        ]
    )

def browse_folder():
    folder_path = filedialog.askdirectory(title="select a folder")

    if folder_path:
        entry.delete(0, tk.END)
        entry.insert(0, folder_path)

window.mainloop()