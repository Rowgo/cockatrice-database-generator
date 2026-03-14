from PIL import Image
from pathlib import Path
from mtg_set import MtgCard, SetData

FRAMES: list[Path] = [
    "assets/frames/colorless_frame.png", 
    "assets/frames/white_frame.png", 
    "assets/frames/blue_frame.png",
    "assets/frames/black_frame.png",
    "assets/frames/red_frame.png",
    "assets/frames/green_frame.png",
    "assets/frames/gold_frame.png",
    "assets/frames/artifact_frame.png",
    "assets/frames/land_frame.png"
    ]

PT_BOXES: list[Path] = [
    "assets/pt_boxes/colorless_pt_box.png",
    "assets/pt_boxes/white_pt_box.png",
    "assets/pt_boxes/blue_pt_box.png",
    "assets/pt_boxes/black_pt_box.png",
    "assets/pt_boxes/red_pt_box.png",
    "assets/pt_boxes/green_pt_box.png",
    "assets/pt_boxes/gold_pt_box.png"
]

HOLO_FOIL_STAMP: Path = "asssets/holo_foil_stamp.png"

SET_SYMBOLS: list[Path] = []

WATER_MARKS: list[Path] = []

FONTS: list[Path] = []

class SpriteSheet:

    def __init__(self, sprite_sheet: Path, sprite_height: int, sprite_width: int, rows: int, columns: int):
        self.sprite_sheet: Image = Image.open(sprite_sheet)
        self.sprite_height : int
        self.sprite_width : int
        self.rows : int
        self.columns : int
    
    def GetSprite(self, frame: int):
        pass

class ImageGenerator:
    def generate_set_images(self, set: SetData) -> list[Image.Image]:
        for card in SetData.card_list:
            card.card_image = self.generate_card_image(card)

    def generate_card_image(self, card: MtgCard) -> Image.Image:
        card_image = Image.new("RGBA", (0, 0))

        self._generate_art_layer()
        self._generate_frame()
        self._generate_name()
        self._generate_cost()
        self._generate_typing()
        self._generate_set_symbol()
        self._generate_ability_text()
        
        return card_image

    def _generate_art_layer():
        pass

    def _generate_frame():
        pass

    def _generate_cost():
        pass

    def _generate_typing():
        pass

    def _generate_ability_text():
        pass

    def _generate_name():
        pass

    def _generate_set_symbol():
        pass

