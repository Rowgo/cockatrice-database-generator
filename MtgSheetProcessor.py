# Copyright (C) Rogan Johnston 2025 all rights reserved
import re
import csv
from mtg_set import SetData, MtgCard, SetInfo, Rarity
from mtg_sheet import CardSheetColumns, SetInfoColumns

class MtgSheetProcessor:
    
    @classmethod
    def get_setdata(cls, setinfo_csvpath, cardsheet_csvpath_list: list) -> SetData:

        set_info = cls._get_setinfo(setinfo_csvpath)
        card_list = cls._get_card_list(cardsheet_csvpath_list)

        set_data = SetData(set_info, card_list)
        return set_data
    
    @classmethod
    def _get_setinfo(cls, csv_path) -> SetInfo:

        with open(csv_path, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)

            cleaned_dict = {}
            setinfo = next(reader) # there should only be one row.
            for key, value in setinfo.items():
                cleaned_key = cls._clean_key(key) # I've set it up so that you have to clean the keys to use SetInfoColumns. This is to give Sam and I some room for error when wrtiting the header for the google sheets
                cleaned_dict[cleaned_key] = value

            set_name = cleaned_dict.get(SetInfoColumns.NAME.value)
            set_code = cleaned_dict.get(SetInfoColumns.SET_CODE.value)
            set_type = cleaned_dict.get(SetInfoColumns.SET_TYPE.value)
            set_size = int(cleaned_dict.get(SetInfoColumns.SET_SIZE.value))
            set_version = cleaned_dict.get(SetInfoColumns.VERSION.value)
            set_release_date = cleaned_dict.get(SetInfoColumns.RELEASE_DATE.value)

            clean_setinfo = SetInfo(longname=set_name, name=set_code, type=set_type, size=set_size, version=set_version, release_date=set_release_date)

        return clean_setinfo

    @classmethod
    def _get_card_list(cls, csv_path_list: list) -> list[MtgCard]:

        card_list = []
        for csv_path in csv_path_list:
            cls._clean_cardsheet(csv_path)

            with open(csv_path, 'r', newline='') as csv_file:
                dict_reader = csv.DictReader(csv_file)

                for row in dict_reader:
                    card_code = row.get(CardSheetColumns.CARD_CODE.value)
                    card_rarity = Rarity[card_code[0]].value # this code kinda sucks. Not sure how else to do it. maybe a static method that is more robust? It works though sooo.
                    card_type = row.get(CardSheetColumns.TYPE.value)
                    card_cost = row.get(CardSheetColumns.MANACOST.value)
                    card_name = row.get(CardSheetColumns.NAME.value)
                    card_ability = row.get(CardSheetColumns.ABILITY.value)
                    if not card_name:
                        card_name = card_code
                    card = MtgCard(name=card_name, manacost=card_cost, type=card_type, rarity=card_rarity, ability=card_ability)
                    card_list.append(card)

        return card_list

    @classmethod
    def _clean_cardsheet(cls, csv_path):

        print('Cleaning: ' + csv_path)
        clean_cardsheet = []
        with open(csv_path, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
            new_header = []
            for i in range(len(header)):
                key = cls._clean_key(header[i])
                if key == CardSheetColumns.NOTES.value:
                    break
                new_header.append(key)

            clean_cardsheet.append(new_header)

            for row in reader:
                if re.fullmatch(r'\w\w\d\d', row[0]):
                    new_row = []
                    for i in range(len(new_header)):
                        new_row.append(row[i])
                    clean_cardsheet.append(new_row)

        with open(csv_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for row in clean_cardsheet:
                writer.writerow(row)


    @staticmethod
    def _clean_key(key: str):
        """format the key to be inline with cockatrice's tag naming conventions."""
        lower_key = key.lower()
        striped_key = lower_key.strip()
        snakecase_key = re.sub(r' ', '_', striped_key)
        cleaned_key = re.sub(r'[^a-zA-Z0-9_]', '', snakecase_key) # special characters \d = digits | \w = characters | [^...] = negation (!not) | + = repetitions of X. for example: (r'1+', '2' "ab111ab11ab1") --> ab2ab2ab2
        return cleaned_key