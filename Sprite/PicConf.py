import re
from configparser import SectionProxy

from Template import Template
from Tool.FileTool import load_no_blank_img


class PicConf:
    """
    pic config
    """

    def __init__(self, config: SectionProxy, pack_mode: str):
        self.pack_mode=pack_mode
        self.input_img_name = str(config["input_img_name"])
        self.prefix = str(config["prefix"])
        self.pic_type = Template.get_type(pack_mode,str(config["type"]))
        self.slide_height = int(
            config["slide_height"]) if "slide_height" in config.keys() else self.pic_type.value.slide_height
        self.slide_width = int(config["slide_width"]) if "slide_width" in config.keys() else self.pic_type.value.slide_width
        self.slide_num = int(config["slide_num"]) if "slide_num" in config.keys() else self.pic_type.value.slide_num
        self.need_resize = bool(config["resize"]) if "resize" in config.keys() else False
        self.need_preview = bool(config["preview"]) if "preview" in config.keys() else False
        self.sleeve = bool(config["sleeve"]) if "sleeve" in config.keys() else False
        self.sleeve_color = bool(config["sleeve_color"]) if "sleeve_color" in config.keys() else False
        if "cus_sleeve_color" in config.keys():
            self.cus_sleeve_color = []
            pixels = config["cus_sleeve_color"]
            it = re.finditer(r"\(([0-9])(.?),(.?)([0-9])\)", pixels)
            for match in it:
                self.cus_sleeve_color.append((int(match.group(1)),int(match.group(4))))

        else:
            self.cus_sleeve_color = [(0, 0), (0, 1), (0, 2)]

        self.input_img = load_no_blank_img(f"{self.input_img_name}.png",
                                           self.slide_width, self.slide_height, self.need_resize)
        self.max_sprite_num = (int(self.input_img.width / self.slide_width)
                               * int(self.input_img.height / (self.slide_height * self.slide_num)))

    def print(self):
        print(
            f"loaded {self.input_img_name}.png, img width={self.input_img.width}, img height={self.input_img.height}, "
            f"slide height={self.slide_height}, slide width={self.slide_width}, "
            f"sprite slide num={self.slide_num}, max sprite num={self.max_sprite_num}")
        if self.sleeve_color:
            print(f"sleeve get color for pixel {self.cus_sleeve_color}")
