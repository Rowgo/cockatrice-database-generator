```markdown
# Google Sheets to Cockatrice Card Database Converter

This project provides a Python script to generate card databases for Cockatrice from data stored in Google Sheets.

## Description

Currently, this tool primarily supports Magic: The Gathering (MTG) cards, but it is designed with the potential for expansion to other card games.

## Usage

1.  **Install Python:** Ensure you have a Python interpreter installed. This project was developed and tested with Python 3.11.9.

2.  **Configure Google Sheet URLs:**
    * Open the `main.py` file.
    * Locate the constants `DOCURL`, `SETINFO_URL`, and `CARDSHEET_URL_LIST`.
    * Update these constants to point to your specific Google Sheet document and its individual sheets.

    **Finding your Google Sheet URLs and IDs:**
    When you open a Google Sheet, your URL will typically look like this:
    `https://docs.google.com/spreadsheets/d/YOUR_DOC_URL/edit?gid=YOUR_SHEET_ID#gid=YOUR_SHEET_ID`

    * `YOUR_DOC_URL`: This portion (e.g., `yourdocurl`) should be used for the `DOCURL` constant.
    * `YOUR_SHEET_ID`: This numerical ID (e.g., `yoursheetid`) should be used for the `id` parameter within the `GoogleSheet` objects in `SETINFO_URL` and `CARDSHEET_URL_LIST`.

3.  **Run the Script:** Execute the `main.py` file:
    ```bash
    python main.py
    ```

## Important Considerations

* **`EXPORT_TYPE` Variable:** Do not modify the `EXPORT_TYPE` variable. The project currently only supports exporting data in CSV format.
* **Data Starting Point:** The data block within your Google Sheets must begin at cell `A1` (row 0, column A).
* **Sheet Structure:**
    * Your Google Sheet document **must** contain a "Set Info" sheet and one or more sheets for card lists.
* **Header Names - Set Info Sheet:**
    The "Set Info" sheet must use the following header names exactly (case-insensitive and leading/trailing spaces are ignored):
    | Name | Set Code | Set Type | Set Size | Version | Release Date |
    | :--- | :------- | :------- | :------- | :------ | :----------- |
* **Header Names - Card Sheets:**
    Card sheets must use the following header names (case-insensitive and leading/trailing spaces are ignored):
    | Card Code | Name | Manacost | Art | Type | Ability | PT | Notes |
    | :-------- | :--- | :------- | :-- | :--- | :------ | :- | :---- |
    * `Card Code` must be the first column.
    * `Notes` is an optional column, but if present, it must be the last column in the table. Data within the `Notes` column will be ignored.
* **Card Code Format:**
    For a row to be recognized as a card entry, the first cell in that row (`Card Code` column) must use a card code following the format: `AA00`.
    | Format | Rarity Determination |
    | :----- | :------------------- |
    | `C` | Common |
    | `U` | Uncommon |
    | `R` | Rare |
    | `M` | Mythic |
    The first letter of a card code is used to determine the card's rarity.
* **Header Name Flexibility:**
    The script has some forgiveness for how header names are typed:
    * Headers are not case-sensitive.
    * Leading or trailing spaces in header names will not affect the code's ability to use the data from that header.
```