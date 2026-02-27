import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from save_file_manager import SaveFileManager

class SheetPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.entry_list: list[tk.Entry] = []
        self.sheet_label = tk.Label(master=self, text="Google sheet url that holds your card data.", font=("Arial", 12))
        self.sheet_label.pack(pady=20, anchor="w")

        self.new_entry_btn = tk.Button(self, text="New Entry", command=self._new_entry)
        self.new_entry_btn.pack(anchor='e')
        
        self._new_entry()

    def _new_entry(self):
        entry_frame = tk.Frame(master=self)
        entry_frame.pack(before=self.new_entry_btn, fill="x", expand=True)

        new_entry = tk.Entry(master=entry_frame)
        new_entry.pack(fill="x", expand=True, side="left")
        self.entry_list.append(new_entry)

        delete_btn = tk.Button(master=entry_frame, text='X', command=lambda: self._remove_entry(master_frame=entry_frame, entry=new_entry))
        delete_btn.pack(side="left")

    def _remove_entry(self, master_frame: tk.Frame, entry: tk.Entry):
        self.entry_list.remove(entry)
        master_frame.destroy()

    @property
    def entry_data(self) -> dict:
        data: dict = {}
        data['sheet_url'] = self.sheet_entry.get()

        return data

class SaveDestinationPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):

        self.save_path_label = tk.Label(master=self, text="Where do you want the XML saved to?", font=("Ariel", 12))
        self.save_path_label.pack(pady=20, anchor="w")

        self.save_path_entry_frame = tk.Frame(master=self)
        self.save_path_entry_frame.pack(fill="x", expand=True)

        self.save_path_entry = tk.Entry(master=self.save_path_entry_frame)
        self.save_path_entry.pack(side="left", fill="x", expand=True)

        self.browse_button = tk.Button(master=self.save_path_entry_frame, text="Browse", command=lambda:self._browse_folder())
        self.browse_button.pack(side="right")

    def _browse_folder(self):
        folder_path = filedialog.askdirectory(title="Select a folder")
    
        if folder_path:
            self.save_path_entry.delete(0, tk.END)
            self.save_path_entry.insert(0, folder_path)

    @property
    def entry_data(self) -> dict:
        data: dict = {}
        data['xml_save_path'] = self.save_path_entry.get()
        
        return data

class SettingsWizard(tk.Tk):
    def __init__(self, config_frames: list[type[tk.Frame]]):
        super().__init__()
        self.title("Cockatrice Card Set Generator")
        self.geometry("400x300")

        self.frame_order = []
        self.current_index = 0
        self.frame_stack: list[tk.Frame] = []
        self.current_frame: tk.Frame = None

        self._setup_frames(config_frames=config_frames)
        self._setup_navigation()
        self._push_frame(self.frame_order[self.current_index])
    
    def _setup_frames(self, config_frames: list[type[tk.Frame]]):
        for Frame in config_frames:
            frame = Frame(self)
            self.frame_order.append(frame)
    
    def _setup_navigation(self):
        self.navigation_frame = tk.Frame(self)
        self.navigation_frame.pack(fill="x")

        self.back_button = tk.Button(self.navigation_frame, text="Back", command=lambda:self._navigate_back())

        self.next_button = tk.Button(self.navigation_frame, text="Next", command=lambda:self._navigate_next())
        self.next_button.pack(padx=20, side="left")

    def _navigate_next(self, event=None):

        self.current_index += 1
        SettingsWizard._try_save_frame_data(self.current_frame)

        if self.current_index > len(self.frame_order) - 1:
            self._quit()
            return

        self._push_frame(self.frame_order[self.current_index])

        if self.current_index == 1:
            self.back_button.pack(before=self.next_button, padx=20, side="left")

        if self.current_index == len(self.frame_order) - 1:
            self.next_button.config(text="Finish")
        else:
            self.next_button.config(text="Next")

    def _navigate_back(self, event=None):
        if self.current_index <= 0:
            return
        
        self._pop_frame()
        self.current_index -= 1

        if self.current_index == 0:
            self.back_button.pack_forget

    def _push_frame(self, frame_to_push: tk.Frame):
        """Put a frame onto the stack and make it visible"""
        if self.current_frame:
            self.current_frame.pack_forget()

        self.frame_stack.append(frame_to_push)
        frame_to_push.pack(before=self.navigation_frame, fill="both", expand=True)
        self.current_frame = frame_to_push

    def _pop_frame(self):
        """Return to the previous frame"""
        self.current_frame.pack_forget()
        previous_frame: tk.Frame = self.frame_stack.pop()

        if previous_frame:
            previous_frame.pack(fill="both", expand=True)
            self.current_frame = previous_frame

    @staticmethod
    def _try_save_frame_data(frame: tk.Frame):
        if hasattr(frame, "entry_data"):
            SaveFileManager.save(frame.__class__.__name__, frame.entry_data)

    def _quit(self):
        self.destroy()

panel_list = [SheetPanel, SaveDestinationPanel]
root = SettingsWizard(panel_list)

root.mainloop()