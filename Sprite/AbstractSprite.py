from abc import abstractmethod, ABC

from Sprite.PicConf import PicConf
from Tool.FileTool import Rectangle


class AbstractSprite(ABC):

    def __init__(self, conf: PicConf, sprite_index: int) -> None:
        self.img = None
        self.conf = conf
        self.sprite_index = sprite_index
        self.load_sprite_img()

    def load_sprite_img(self) -> None:
        slider_rect = Rectangle(x=self.sprite_index * self.conf.slide_width % self.conf.input_img.width,
                                y=int(self.sprite_index * self.conf.slide_width /
                                      self.conf.input_img.width) * self.conf.slide_height * self.conf.slide_num,
                                width=self.conf.slide_width,
                                height=self.conf.slide_height * self.conf.slide_num)
        self.img = self.conf.input_img.crop((slider_rect.get_left(), slider_rect.get_upper(),
                                             slider_rect.get_right(), slider_rect.get_lower()))

    def is_blank(self) -> bool:
        pixels = self.img.getdata()
        for pixel in pixels:
            if pixel[3] != 0:
                return False
        return True

    @abstractmethod
    def save_sprite(self, sprite_dir: str) -> None:
        """
        sprite保存
        """

    @abstractmethod
    def save_json(self, sprite_dir: str, template: dict, output_index=-1) -> None:
        """
        json
        """