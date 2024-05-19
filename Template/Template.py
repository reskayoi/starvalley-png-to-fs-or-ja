from Sprite.PicConf import PicConf
from Template.FSTemplate import FS
from Template.JATemplate import JA


def run_mode(mode: str):
    if mode == "JA":
        return JA
    else:
        return FS


def get_type(mode: str, t: str):
    return run_mode(mode).get_type(t)


def get_manifest(mode: str):
    return run_mode(mode).get_manifest()


def create_sprite(conf: PicConf, sprite_index: int):
    return run_mode(conf.pack_mode).create_sprite(conf, sprite_index)


def load_template(conf: PicConf):
    return run_mode(conf.pack_mode).load_template(conf.pic_type)
