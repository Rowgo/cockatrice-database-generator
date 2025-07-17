# Copyright (C) Rogan Johnston 2025 all rights reserved
from mtg_set import SetData, SetInfo, MtgCard, Rarity
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import os

class MtgDatabaseBuilder:
    """This class creats an xml file that can be used for the cockatrice data base."""

    @classmethod
    def build_database(cls, set_data: SetData):
        tree = ET.parse('database_templates\carddatabase.xml')
        root = tree.getroot()
        sets_elem = root.find('sets')
        cards_elem = root.find('cards')

        cls._attach_set_elem(sets_elem, set_data.setinfo)

        for card in set_data.card_list:
            cls._attach_card_elem(cards_elem, card)

        os.makedirs('database', exist_ok=True)
        cls._save_xml_file(root, f'databases/{set_data.setinfo.longname}.xml')

    @staticmethod
    def _attach_set_elem(sets_elem: Element, setinfo: SetInfo):

        set_tree = ET.parse('database_templates\mtg_set.xml')
        set_elem = set_tree.getroot()

        set_elem.find('name').text = setinfo.name 
        set_elem.find('longname').text = setinfo.longname
        set_elem.find('settype').text = setinfo.type
        set_elem.find('releasedate').text = setinfo.release_date

        sets_elem.append(set_elem)
    
    @classmethod
    def _attach_card_elem(cls, cards_elem: Element, card: MtgCard):

        card_tree = ET.parse('database_templates\mtg_card.xml')
        card_elem = card_tree.getroot()

        name = card.name
        card_elem.find('name').text = card.name
        card_elem.find('text').text = card.ability

        prop_elem = card_elem.find('prop')
        cls._populate_prop_elem(prop_elem, card)

        card_elem.find('set').text = card.set_code
        # add set attributes

        # check for related cards.
        # if there are related cards
            # add related tag
            # related card tag.text = another card name

        card_elem.find('tablerow').text = str(card.get_tablerow())

        # check text for the line 'this card comes into play tapped'
        # if it has that line then 
            # add a 'cipt' tag and 
            # make it's text = 1

        # if it's a turn card then updsidedown tag would be made here

        cards_elem.append(card_elem)

    @staticmethod
    def _populate_prop_elem(prop_elem: Element, card: MtgCard):
        
        prop_elem.find('layout').text = 'normal'
        prop_elem.find('side').text = 'front' 
        prop_elem.find('type').text = card.type
        prop_elem.find('maintype').text = card.get_maintype()
        prop_elem.find('manacost').text = card.manacost
        prop_elem.find('cmc').text = str(card.get_cmc())

        colors = card.get_colors()
        if colors:
            colors_elem = ET.SubElement(prop_elem, 'colors')
            colors_elem.text = colors

        color_identity = card.get_coloridentity()
        if color_identity:
            coloridentity_elem = ET.SubElement(prop_elem, 'coloridentity')
            coloridentity_elem.text = color_identity
        if card.pt:
            pt_elem = ET.SubElement(prop_elem, 'pt')
            pt_elem.text = card.pt
        if card.loyalty:
            loyalty_elem = ET.SubElement(prop_elem, 'loyalty')
            loyalty_elem.text = card.loyalty
        format_standard_elem = ET.SubElement(prop_elem, 'format-standard')
        format_standard_elem.text = 'legal' # I'll hard code these values for now, but if Sam and I ever want to start deciding what cards should be legal for what then the MTGCard class should have a legal format list and should handle this logic.
        format_commander_elem = ET.SubElement(prop_elem, 'format-commander')
        format_commander_elem.text = 'legal' # I'll hard code these values for now, but if Sam and I ever want to start deciding what cards should be legal for what then the MTGCard class should have a legal format list and should handle this logic.
        format_modern_elem = ET.SubElement(prop_elem, 'format-modern')
        format_modern_elem.text = 'legal' # I'll hard code these values for now, but if Sam and I ever want to start deciding what cards should be legal for what then the MTGCard class should have a legal format list and should handle this logic.
        if card.rarity == Rarity.C.value or Rarity.U.value:
            format_pauper_elem = ET.SubElement(prop_elem, 'format-pauper')
            format_pauper_elem.text = 'legal' # I'll hard code these values for now, but if Sam and I ever want to start deciding what cards should be legal for what then the MTGCard class should have a legal format list and should handle this logic.    

    @staticmethod
    def _save_xml_file(xml_root, save_path):
        
        tree = ET.ElementTree(xml_root)
        ET.indent(tree, space="    ")
        tree.write(save_path, encoding="utf-8", xml_declaration=True)

# TODO:
    # break up this file into multiple parts. 
        # Set Builder
        # Card Builder
        # Utils
    
    # place everything into classes

    # Import constants or move color pie constants here

    # Make type order and main types into constant variables.