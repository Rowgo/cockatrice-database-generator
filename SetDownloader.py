# Copyright (C) Rogan Johnston 2025 all rights reserved
from urllib.request import urlretrieve
import os
from mtg_sheet import GoogleSheetUrl

class SetDownloader:
    """This class downloads the CSV files from google sheets"""

    @staticmethod
    def pull_and_save(google_sheet: GoogleSheetUrl, download_folder) -> str:

        os.makedirs(download_folder, exist_ok=True)
        file_name = f'{google_sheet.sheet_name}{google_sheet.get_export_extension()}'
        file_path = os.path.join(download_folder, file_name)
        url = google_sheet.get_export_url()

        urlretrieve(url, file_path)
        print(f"file saved to: {file_path}")
    
        return file_path