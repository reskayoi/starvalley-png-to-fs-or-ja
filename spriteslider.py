import json
import shutil
from configparser import ConfigParser, SectionProxy

from FSTemplate.FS import FS
from Sprite.ObjectSprite import ObjectSprite
from Tool.FileTool import mkdir, load_no_blank_img


def slider(config: SectionProxy, work_dir: str):
    """slide image"""
    input_img_name = str(config["input_img_name"])
    prefix = str(config["prefix"])
    fs_type = FS.get_type(str(config["FS_type"]))
    slide_height = config.getint("slide_height") if "slide_height" in config.keys() else fs_type.slide_height
    slide_width = config.getint("slide_width") if "slide_width" in config.keys() else fs_type.slide_width
    slide_num = config.getint("slide_num") if "slide_num" in config.keys() else fs_type.slide_num
    need_resize = bool(config["resize"]) if "resize" in config.keys() else False
    need_preview = bool(config["preview"]) if "preview" in config.keys() else False

    img = load_no_blank_img(f"{input_img_name}.png",slide_width,slide_height,need_resize)
    if need_preview:
        img.save(f"{work_dir}/{input_img_name}_resize.png")

    print(f"loaded {input_img_name}.png, img width={img.width}, img height={img.height}")

    work_dir = f"{work_dir}/{fs_type.dir_name}"
    json_template = f"./FSTemplate/{fs_type.file_name}.json"
    mkdir(f"{work_dir}")

    max_sprite_num = int(img.width / slide_width) * int(img.height / (slide_height * slide_num))
    print(
        f"slide height={slide_height}, slide width={slide_width}, sprite slide num={slide_num}, max sprite num={max_sprite_num}")

    with open(json_template, mode="r", encoding="utf-8") as f:
        template = json.load(f)

    output_index = 0
    for sprite_index in range(0, max_sprite_num):
        sprite = ObjectSprite(
            img, slide_height, slide_width, slide_num, sprite_index)
        if sprite.is_blank():
            continue
        output_index += 1
        dir_name = f"{work_dir}/{input_img_name}_{output_index}"
        mkdir(dir_name)
        sprite.save_sprite(dir=dir_name,
                           json_template=template,
                           name_prefix=prefix,
                           file_name=fs_type.file_name,
                           output_index=output_index)

    print(f"finally saved {output_index} objects to {work_dir}")


def manifest(config: dict):
    manifest_dict = {
        "UpdateKeys": [],
        "Dependencies": [],
        "ContentPackFor": {
            "UniqueID": "PeacefulEnd.FashionSense",
            "MinimumVersion": "6.0.0"
        }
    }
    work_dir = config["name"]
    with open(f"{work_dir}/manifest.json", mode="w", encoding="utf-8") as f:
        json.dump(dict(config, **manifest_dict), f, indent=2, ensure_ascii=False)

    print(f"save mod manifest to {work_dir}/manifest.json success")


def main():
    # 读取配置文件
    config = ConfigParser()
    config.read('config.ini')

    # 建立输出文件夹
    work_dir = config["manifest"]["Name"]
    mkdir(f"{work_dir}")
    print(f"work_dir:{work_dir}")

    # 生成manifest.json
    manifest(dict(config["manifest"]))
    config.pop("manifest")

    for pack_config in config.sections():
        print(f"\nloading pack {pack_config}...")
        slider(config[pack_config], work_dir)
        print(f"pack {pack_config} load success.")

    shutil.make_archive(work_dir, 'zip', work_dir)
    print(f"\noutput {work_dir}.zip.")
    shutil.rmtree(work_dir)
    print(f"clean temp dir success.")


if __name__ == '__main__':
    print("===start===")
    main()
    print("===end===")
