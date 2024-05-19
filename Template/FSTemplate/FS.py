from enum import Enum

from Sprite import FSSprite
from Tool.FileTool import load_json


class FSType:
    def __init__(self, dir_name: str, file_name: str, slide_height: int, slide_width: int, slide_num: int) -> None:
        self.dir_name = dir_name
        self.file_name = file_name
        self.slide_height = slide_height
        self.slide_width = slide_width
        self.slide_num = slide_num


class FSEnum(Enum):
    HAT = FSType("Hats", "hat", 20, 20, 4)
    SHIRT = FSType("Shirts", "shirt", 8, 8, 4)
    HAIR = FSType("Hairs", "hair", 32, 16, 3)


def get_manifest():
    return load_json("./Template/FSTemplate/manifest.json")


def get_type(t: str):
    for fs in FSEnum:
        if fs.name == t:
            return fs
    return FSEnum.SHIRT


def create_sprite(conf, sprite_index: int):
    if conf.pic_type == FSEnum.SHIRT:
        return FSSprite.ShirtSprite(conf, sprite_index)
    else:
        return FSSprite.ObjectSprite(conf, sprite_index)


def load_template(pic_type: FSEnum):
    return load_json(f"Template/FSTemplate/{pic_type.value.file_name}.json")
