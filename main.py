# Copyright (C) Rogan Johnston 2025 all rights reserved
from downloader import SetDownloader
from csv_processor import MTGSheetProcessor
from xml_builder import MTGDatabaseBuilder
from mtg_sheet import GoogleSheetUrl
from mtg_set import SetData

DOC_URL = 'https://docs.google.com/spreadsheets/d/1f3jWL21p7YiIwsrQ3gG59_kV5k5blZxJzk8c2dBEe0s'
EXPORT_TYPE = 'csv'

SETINFO_URL = GoogleSheetUrl(sheet_name='setinfo', doc_url=DOC_URL, export_type=EXPORT_TYPE, sheet_id='1329260583')

CARDSHEET_URL_LIST = [
    GoogleSheetUrl(sheet_name='white_cards', doc_url=DOC_URL, export_type=EXPORT_TYPE, sheet_id='939138215'),
    GoogleSheetUrl(sheet_name='blue_cards', doc_url=DOC_URL, export_type=EXPORT_TYPE, sheet_id='2066320701'),
    GoogleSheetUrl(sheet_name='black_cards', doc_url=DOC_URL, export_type=EXPORT_TYPE, sheet_id='1190842356'),
    GoogleSheetUrl(sheet_name='red_cards', doc_url=DOC_URL, export_type=EXPORT_TYPE, sheet_id='1155229247'),
    GoogleSheetUrl(sheet_name='green_cards', doc_url=DOC_URL, export_type=EXPORT_TYPE, sheet_id='54239636'),
    GoogleSheetUrl(sheet_name='multicolor_cards', doc_url=DOC_URL, export_type=EXPORT_TYPE, sheet_id='122032064'),
    GoogleSheetUrl(sheet_name='colorless_cards', doc_url=DOC_URL, export_type=EXPORT_TYPE, sheet_id='2064516960')
]

folder = 'wfa_sheets'
setinfo_path = SetDownloader.pull_and_save(SETINFO_URL, folder)

cardsheet_path_list = []
for cardsheet_url in CARDSHEET_URL_LIST:
    cardsheet_path = SetDownloader.pull_and_save(cardsheet_url, folder)
    cardsheet_path_list.append(cardsheet_path)

set_data: SetData = MTGSheetProcessor.get_setdata(setinfo_path, cardsheet_path_list)

MTGDatabaseBuilder.build_database(set_data)



#TODO:
    #Sorting specifications
        # Once the list is created it will need to be sorted based on set numbering rules for making that part of populating the data easy. (I'll need to find the right algorithim for this)

    #Card tag specifications
        #? How am I going to tell if a card relates to another card such as cards that make tokens? Maybe I can parse the text for the keyword token and then extract the properties of the token and do a look up using that?
        #? How am I going to tell if the card comes into play tapped? parse the text feild?
        #? is there a specific seperation needed for flavour text? how would I get it italisiced and have the dividing line?

    #Set Specifications
        # All of our card pictures can be hosted using Image BB https://imgbb.com/

