import json

from Sprite.AbstractSprite import AbstractSprite


class ObjectSprite(AbstractSprite):

    def __init__(self, conf, sprite_index: int) -> None:
        super(ObjectSprite,self).__init__(conf, sprite_index)

    def save_sprite(self, sprite_dir: str) -> None:
        self.img.save(f"{sprite_dir}/{self.conf.pic_type.value.pic_name}.png")

    def save_json(self, sprite_dir: str, template: dict, output_index=-1) -> None:
        if output_index == -1:
            output_index = self.sprite_index
        template["Name"] = f"{self.conf.prefix}_{output_index}"
        template["Description"] = f"{self.conf.prefix}"
        with open(f"{sprite_dir}/{self.conf.pic_type.value.json_name}.json", mode="w") as f:
            json.dump(template, f, indent=2, ensure_ascii=False)