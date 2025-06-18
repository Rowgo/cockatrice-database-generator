DESCRIPTION
-------------------------------------------------->
This is a project that is for creating card databases for cockatirice using google sheets.

Currently the data base only supports MTG cards, but it could be expanded to support others.


USING THE PROJECT
-------------------------------------------------->
1. Install a Python interpreter. This project was created using version 3.11.9
2. Within the file main change the constants DOCURL and the IDs within SETINFO_URL and CARDSHEET_URL_LIST to point at your google doc and it's sheets
    - When you go to google sheets you should find somthing like this: https://docs.google.com/spreadsheets/d/yourdocurl/edit?gid=yoursheetid#gid=yoursheetid
    - https://docs.google.com/spreadsheets/d/yourdocurl this part is what you should put in DOCURL
    - yoursheetid is what you should put in ID 
3. run the file main.py


MUST FOLLOW
-------------------------------------------------->
do not change the variable EXPORT_TYPE the project currently doesn't support any file types other than csv 

The data you wish to use in your google sheets must start at A-0

Your google sheet document must have a set info sheet and some sheets for card lists.

set info sheets must follow use the header names:
Name | Set Code | Set Type | Set Size | Version | Release Date

Card sheets must follow use the header names: 
Card Code | Name | Manacost | Art | Type | Ability | PT | Notes
    
    - notes is an optional name but must be placed at the end of the table. (The data within the notes column will be ignored)
    - the header 'Card Code' must be first
    - in order for a row to be recognized as a card row the first cell must use a card code that follows the format of: AA00
    - the first letter of a card code is used to determine thee cards rarity C = common U = Uncommon R = Rare M = Mythic

there is some forgivness to how header names can be typed
    - the headers are not case sensitive
    - and spaces before or after the column header will not effect the code's ability to use the data from that header.