# Copyright (C) Rogan Johnston 2025 all rights reserved
from dataclasses import dataclass
from typing import List, Dict
from enum import StrEnum

@dataclass
class GoogleSheetUrl:
    
    sheet_name : str
    doc_url : str
    export_type : str
    sheet_id : str

    def get_export_url(self) -> str:
        return f'{self.doc_url}/export?format={self.export_type}&gid={self.sheet_id}'
    
    def get_export_extension(self) -> str:
        return f'.{self.export_type}'
    
@property
class ESetInfoColumns(StrEnum):
    NAME = 'name'
    SET_CODE = 'set_code'
    SET_TYPE = 'set_type'
    SET_SIZE = 'set_size'
    VERSION = 'version'
    RELEASE_DATE = 'release_date'

@property
class ECardSheetColumns(StrEnum):

    CARD_CODE = 'card_code'
    NAME = 'name'
    MANACOST = 'manacost'
    ART_URL = 'art'
    TYPE = 'type'
    ABILITY = 'ability'
    PT = 'pt'
    LOYALTY = 'loyalty'
    NOTES = 'notes'


