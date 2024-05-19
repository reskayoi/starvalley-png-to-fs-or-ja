import json

from Sprite.AbstractSprite import AbstractSprite
from Sprite.PicConf import PicConf
from Tool.FileTool import get_img_pixel_rgb


class ObjectSprite(AbstractSprite):

    def __init__(self, conf: PicConf, sprite_index: int) -> None:
        super(ObjectSprite,self).__init__(conf, sprite_index)

    def save_sprite(self, sprite_dir: str) -> None:
        self.img.save(f"{sprite_dir}/{self.conf.pic_type.value.file_name}.png")

    def save_json(self, sprite_dir: str, template: dict, output_index=-1) -> None:
        if output_index == -1:
            output_index = self.sprite_index
        template["Name"] = f"{self.conf.prefix}_{output_index}"
        with open(f"{sprite_dir}/{self.conf.pic_type.value.file_name}.json", mode="w") as f:
            json.dump(template, f, indent=2, ensure_ascii=False)


class ShirtSprite(ObjectSprite):
    def __init__(self, conf: PicConf, sprite_index: int):
        super(ShirtSprite, self).__init__(conf, sprite_index)

    def save_json(self, sprite_dir: str, template: dict, output_index=-1) -> None:
        if not self.conf.sleeve:
            for key in template.keys():
                if key != "Name":
                    template[key]['DisableGrayscale'] = 'true'
                    if 'SleeveColors' in template[key].keys():
                        template[key].pop('SleeveColors')
        if self.conf.sleeve_color:
            for key in template.keys():
                if key != "Name":
                    template[key]['DisableGrayscale'] = 'true'
                    template[key]['SleeveColors'] = [get_img_pixel_rgb(self.img, self.conf.cus_sleeve_color[0]),
                                                     get_img_pixel_rgb(self.img, self.conf.cus_sleeve_color[1]),
                                                     get_img_pixel_rgb(self.img, self.conf.cus_sleeve_color[2])]

        super().save_json(sprite_dir, template, output_index)
