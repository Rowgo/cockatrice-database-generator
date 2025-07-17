# Copyright (C) Rogan Johnston 2025 all rights reserved
import re
from enum import StrEnum
from dataclasses import dataclass
from typing import Optional

COLOR_ORDER = ['C', 'W', 'U', 'B', 'R', 'G']
TYPE_ORDER =  ['Instant', 'Sorcery', 'Enchantment', 'Artifact', 'Battle', 'Land', 'Creature', 'Planeswalker']

@property
class Rarity(StrEnum):
    C = "common"
    U = "uncommon"
    R = "rare"
    M = "mythic"

@dataclass
class SetInfo:

    longname: str 
    """Formating example: longname='Actually Apeshit Aligators' name='AAA'"""
    name: str 
    """Formating example: longname='Actually Apeshit Aligators' name='AAA'"""
    type: str
    size: int
    version: str = '0.0.0'
    release_date: str = 'TBD'


@dataclass
class MtgCard:

    name : str
    manacost : str
    type : str
    rarity: str

    art : str = 'https://ibb.co/mVKTwBqW' # this art is a placeholder
    ability : str = ''
    pt : str = None
    """this tag can be omited from the data base."""
    loyalty : str = None 
    """this tag can be omited from the data base."""
    set_code: str = 'AAA'

    def __post_init__(self):
        sorted_manacost = self._sort_manacost(self.manacost)
        self.manacost = sorted_manacost

    def get_maintype(self) -> str:

        type_order =  ['Instant', 'Sorcery', 'Enchantment', 'Artifact', 'Battle', 'Land', 'Creature', 'Planeswalker']
        matching_types = []
        for t in type_order:
            if t in self.type:
                matching_types.append(t)
        maintype = " ".join(matching_types)

        return maintype

    def get_cmc(self) -> int:

        cmc = 0
        digit_match = re.search(r'\d', self.manacost)
        if digit_match:
            cmc += int(digit_match.group())
        for match in re.finditer(r'[CWUBRG]', self.manacost):
            cmc += 1

        return cmc

    def get_colors(self) -> str:

        cost_color_set = set(re.findall(r'[WUBRG]', self.manacost))
        colors = self._sort_colors(cost_color_set)

        return colors

    def get_coloridentity(self) -> str:

        text_colors = ''.join(re.findall(r'\{([WUBRG])\}', self.ability))
        cost_colors = self.get_colors()
        card_color_set = set(f'{text_colors}{cost_colors}')
        color_identity = self._sort_colors(card_color_set)

        return color_identity
    
    def get_tablerow(self) -> int:
        type = self.type
        match type:
            case type if 'Creature' in type: # 'Creature' should be in an Enum
                return 2
            case type if 'Land' in type: # 'Land' should be in an Enum
                return 0
            case type if 'Instant' or 'Sorcery' in type: # 'Instant' and 'Sorcery' should be in an Enum
                return 3
            case _:
                return 1
        
    
    def _sort_manacost(self, manacost) -> str:

        digit_iterable = re.findall(r'\d', manacost)
        color_iterable = re.findall(r'CWUBRG', manacost)
        digits = ''.join(digit_iterable)
        colors = self._sort_colors(color_iterable)
        sorted_manacost = f'{digits}{colors}'

        return sorted_manacost

    @staticmethod
    def _sort_colors(iterable_colors) -> str:
        """ Used to sort an iterable object into a string that follows the order of CWUBRG. 
        This should be used to clean up any color based data that will be used for the database.
        """
        sorted_colors = ''
        for c in COLOR_ORDER:
            for item in iterable_colors:
                if c in item:
                    sorted_colors += c

        return sorted_colors

@dataclass
class SetData:

    setinfo: SetInfo
    card_list: list[MtgCard] 

    def __post_init__(self):
        """assign set code to each card"""
        for card in self.card_list:
            card.set_code = self.setinfo.name
    #TODO:
    # sort the cards by color order and alphabetically while giving them all a set number.
    # not sure if related cards should be a property assigned within the csv parser or if it should be assigned here in SetData


