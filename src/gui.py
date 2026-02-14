import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import json

root = tk.Tk()
root.title("Cockatrice Card Set Generator")
root.geometry("400x300")

class SheetPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        sheet_entry_frame = tk.Frame(root)
        sheet_entry_frame.pack(pady=20, padx=20, fill="x")

        sheet_label = tk.Label(sheet_entry_frame, text="Google sheet url that holds your card data.", font=("Arial", 12))
        sheet_label.pack(pady=20, anchor="w")

        sheet_entry = tk.Entry(sheet_entry_frame, width=30)
        sheet_entry.pack(fill="x", expand=True)

class SaveDestinationPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):

        self.save_path_label = tk.Label(self, text="Where do you want the XML saved to?", font=("Ariel", 12))
        self.save_path_label.pack(pady=20, anchor="w")

        self.save_path_entry_frame = tk.Frame(self)
        self.save_path_entry_frame.pack(fill="x", expand=True)

        self.save_path_entry = tk.Entry(self.save_path_entry_frame)
        self.save_path_entry.pack(side="left", fill="x", expand=True)

        self.browse_button = tk.Button(self.save_path_entry_frame, text="Browse", command=lambda:self._browse_folder())
        self.browse_button.pack(side="right")

    def _browse_folder(self):
        folder_path = filedialog.askdirectory(title="Select a folder")
    
        if folder_path:
            self.save_path_entry.delete(0, tk.END)
            self.save_path_entry.insert(0, folder_path)

class NavigationBar(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
    
    def create_widgets(self):
        navigation_frame = tk.Frame(root)
        navigation_frame.pack(padx=20, pady=20, anchor="s")

        back_button = tk.Button(navigation_frame, text="Back", command=lambda:self._navigate_back())
        back_button.pack(padx=20, side="left")

        next_button = tk.Button(navigation_frame, text="Next", command=lambda:self._navigate_next())
        next_button.pack(padx=20, side="left")

    def _navigate_back(self, event=None):
        pass

    def _navigate_next(self, event=None):
        pass

sheet_panel = SheetPanel(root)

save_destination_panel = SaveDestinationPanel(root)
save_destination_panel.pack(padx=20, pady=20, fill="x", expand=True)

navigation_bar = NavigationBar(root)

root.mainloop()