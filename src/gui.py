import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import json

root = tk.Tk()
root.title("Cockatrice Card Set Generator")
root.geometry("400x300")

sheet_entry_frame = tk.Frame(root)
sheet_entry_frame.pack(pady=20, padx=20, fill="x")

sheet_label = tk.Label(sheet_entry_frame, text="Google sheet url that holds your card data.", font=("Arial", 12))
sheet_label.pack(pady=20, anchor="w")

sheet_entry = tk.Entry(sheet_entry_frame, width=30)
sheet_entry.pack(fill="x", expand=True)

save_path_frame = tk.Frame(root)
save_path_frame.pack(pady=20, padx=20, fill="x")

save_path_label = tk.Label(save_path_frame, text="Where do you want the XML saved to?", font=("Ariel", 12))
save_path_label.pack(pady=20, anchor="w")

save_path_entry_frame = tk.Frame(save_path_frame)
save_path_entry_frame.pack(fill="x", expand=True)

save_path_entry = tk.Entry(save_path_entry_frame)
save_path_entry.pack(side="left", fill="x", expand=True)

browse_button = tk.Button(save_path_entry_frame, text="Browse", command=lambda:_browse_folder())
browse_button.pack(padx=20, side="right")

def _browse_folder():
    folder_path = filedialog.askdirectory(title="Select a folder")

    if folder_path:
        save_path_entry.delete(0, tk.END)
        save_path_entry.insert(0, folder_path)

navigation_frame = tk.Frame(root)
navigation_frame.pack(padx=20, pady=20)

back_button = tk.Button(navigation_frame, text="Back", command=lambda:_navigate_back())
back_button.pack(padx=20, side="left")

next_button = tk.Button(navigation_frame, text="Next", command=lambda:_navigate_next())

def _navigate_back():
    pass

def _navigate_next():
    pass

root.mainloop()