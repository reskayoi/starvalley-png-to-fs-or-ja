from PIL import Image
from Tool.FileTool import Rectangle
import json


class ObjectSprite:

    def __init__(self, slide_img: Image, slide_height: int, slide_width: int, slide_num: int,
                 sprite_index: int) -> None:
        self.slide_num = slide_num
        self.slide_height = slide_height
        self.slide_img = slide_img
        self.slide_width = slide_width
        self.sprite_index = sprite_index
        self.load_sprite_img()

    def load_sprite_img(self) -> None:
        slider_rect = Rectangle(self.sprite_index * self.slide_width % self.slide_img.width,
                                int(self.sprite_index * self.slide_width /
                                    self.slide_img.width) * self.slide_height * self.slide_num,
                                self.slide_width,
                                self.slide_height * self.slide_num)
        self.img = self.slide_img.crop((slider_rect.get_left(
        ), slider_rect.get_upper(), slider_rect.get_right(), slider_rect.get_lower()))

    def is_blank(self) -> bool:
        pixels = self.img.getdata()
        for pixel in pixels:
            if pixel[3] != 0:
                return False
        return True

    def save_sprite(self, dir: str, json_template: dict, name_prefix: str, file_name: str, output_index=-1) -> None:
        if output_index == -1:
            output_index = self.sprite_index

        # blank img will not output
        if self.is_blank():
            return

        self.img.save(f"{dir}/{file_name}.png")
        self.save_json(f"{name_prefix}_{output_index}", dir, json_template, file_name)

    def save_json(self, name: str, dir: str, template: dict, file_name: str) -> None:
        template["Name"] = name
        with open(f"{dir}/{file_name}.json", mode="w") as f:
            json.dump(template, f, indent=2, ensure_ascii=False)