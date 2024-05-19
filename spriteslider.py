import json
import shutil
from configparser import ConfigParser

from Sprite.PicConf import PicConf
from Template import Template
from Tool import FileTool


def slider(conf: PicConf, work_dir: str):
    """
    slide image
    """
    conf.print()
    if conf.need_preview:
        conf.input_img.save(f"{work_dir}/{conf.input_img_name}_resize.png")

    # create type dir
    type_dir = f"{work_dir}/{conf.pic_type.value.dir_name}"
    FileTool.mkdir(f"{type_dir}")

    # load type template
    template = Template.load_template(conf)

    # slide sprites
    output_index = 1
    for sprite_index in range(0, conf.max_sprite_num):
        output_index = sprite_save(conf, output_index, sprite_index, type_dir, template)

    print(f"finally saved {output_index-1} {conf.pic_type.name}s to {type_dir}")


def sprite_save(conf, output_index, sprite_index, type_dir, template) -> int:
    sprite = Template.create_sprite(conf, sprite_index)

    if sprite.is_blank():
        return output_index

    # create sprite dir
    sprite_dir = f"{type_dir}/{conf.input_img_name}_{output_index}"
    FileTool.mkdir(sprite_dir)

    # save sprite img
    sprite.save_sprite(sprite_dir)

    # save sprite json
    sprite.save_json(sprite_dir=sprite_dir,
                     template=template,
                     output_index=output_index)

    return output_index + 1


def gen_manifest(config: dict,pack_mode: str):
    manifest_dict = Template.get_manifest(pack_mode)
    work_dir = config["name"]
    with open(f"{work_dir}/manifest.json", mode="w", encoding="utf-8") as f:
        json.dump(dict(config, **manifest_dict), f, indent=2, ensure_ascii=False)

    print(f"save mod manifest to {work_dir}/manifest.json success")


def main():
    # 读取配置文件
    config = ConfigParser()
    config.read('config.ini')

    # 读取运行时配置
    try:
        pack_mode = config["run"]["pack_mode"]
        config.pop("run")
    except Exception:
        pack_mode = "FS"
    print(f"run in {pack_mode} mode")

    # 建立输出文件夹
    work_dir = config["manifest"]["Name"]
    FileTool.mkdir(f"{work_dir}")
    print(f"work dir:{work_dir}")

    # 生成manifest.json
    gen_manifest(dict(config["manifest"]),pack_mode)
    config.pop("manifest")

    for pack_config in config.sections():
        print(f"\nloading pack {pack_config}...")
        slider(PicConf(config[pack_config],pack_mode), work_dir)
        print(f"pack {pack_config} load success.")

    shutil.make_archive(work_dir, 'zip', work_dir)
    print(f"\nzip work dir to {work_dir}.zip.")
    # shutil.rmtree(work_dir)
    # print(f"clean work dir success.")


if __name__ == '__main__':
    print("===start===")
    main()
    print("===end===")
