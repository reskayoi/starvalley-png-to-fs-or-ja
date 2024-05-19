from enum import Enum

from Sprite import JASprite
from Sprite.PicConf import PicConf
from Tool.FileTool import load_json


class JAType:
    def __init__(self, dir_name: str, json_name: str, slide_height: int, slide_width: int, slide_num: int,
                 pic_name="male") -> None:
        self.dir_name = dir_name
        self.slide_height = slide_height
        self.slide_width = slide_width
        self.slide_num = slide_num
        self.json_name = json_name
        self.pic_name = pic_name


class JAEnum(Enum):
    SHIRT = JAType("Shirts", "shirt", 8, 8, 4)
    HAT = JAType("Hats", "hat", 20, 20, 4)
    HAIR = JAType("Hairs", "hair", 32, 16, 3)


def get_manifest():
    return load_json("./Template/JATemplate/manifest.json")


def get_type(t: str):
    for ja in JAEnum:
        if ja.name == t:
            return ja
    return JAEnum.SHIRT


def create_sprite(conf: PicConf, sprite_index: int):
    return JASprite.ObjectSprite(conf, sprite_index)


def load_template(pic_type: JAEnum):
    return load_json(f"Template/JATemplate/{pic_type.value.json_name}.json")
