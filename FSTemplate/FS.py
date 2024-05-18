from enum import Enum


class FSType:
    def __init__(self, dir_name: str, file_name: str, slide_height: int, slide_width: int, slide_num: int) -> None:
        self.dir_name = dir_name
        self.file_name = file_name
        self.slide_height = slide_height
        self.slide_width = slide_width
        self.slide_num = slide_num


class FS(Enum):
    HAT = FSType("Hats", "hat", 20, 20, 4)
    SHIRT = FSType("Shirts", "shirt", 8, 8, 4)
    HAIR = FSType("Hairs", "hair", 32, 16, 3)

    def get_type(t: str):
        for fs in FS:
            if fs.name == t:
                return fs.value
        return FS.SHIRT.value
