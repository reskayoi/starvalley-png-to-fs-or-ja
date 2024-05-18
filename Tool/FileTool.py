import os
from PIL import Image


class Rectangle:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, offset_x=0, offset_y=0):
        self.x += offset_x
        self.y += offset_y

    def get_left(self):
        return self.x

    def get_right(self):
        return self.x + self.width

    def get_upper(self):
        return self.y

    def get_lower(self):
        return self.y + self.height

    def get_new_move(self, offset_x=0, offset_y=0):
        return Rectangle(self.x + offset_x, self.y + offset_y, self.width, self.height)


def load_no_blank_img(input_img_name: str, sprite_width: int, sprite_hight: int,need_resize) -> Image:
    """
    加载去除空白的原始图片
    """
    img = Image.open(input_img_name)
    return remove_img_blank(img, sprite_width, sprite_hight, need_resize)


def is_blank(img: Image) -> bool:
    """
    判断图片是否为空
    """
    pixels = img.getdata()
    for pixel in pixels:
        if pixel[3] != 0:
            return False
    return True


def get_slide_img(img: Image, slide_rect: Rectangle) -> Image:
    """
    剪裁rect为图片
    """
    rect = (slide_rect.get_left(), slide_rect.get_upper(), slide_rect.get_right(), slide_rect.get_lower())
    return img.crop(rect)


def resize_img(img: Image) -> Image:
    """
    去除空白边缘
    """
    return img.crop(img.getbbox())


def remove_img_blank(img: Image, sprite_width: int, sprite_hight: int, need_resize: bool) -> Image:
    """
    将图片以sprite大小分割，去除空白sprite后重新拼接
    """
    if need_resize:
        img = resize_img(img)
    no_blank_img = Image.new("RGBA", (img.width, img.height))
    max_sprite_num_x = int(img.width / sprite_width)
    max_sprite_num_y = int(img.height / sprite_hight)

    slide_rect_zero = Rectangle(0, 0, sprite_width, sprite_hight)
    now_x_num = 0
    now_y_num = 0
    max_x_size = 0

    for y in range(max_sprite_num_y):
        for x in range(max_sprite_num_x):
            # 滑动到对应的rect
            slide_rect = slide_rect_zero.get_new_move(x * sprite_width, y * sprite_hight)
            slide_img = get_slide_img(img, slide_rect)
            if not is_blank(slide_img):
                # sprite不为空时，粘贴到新图片中
                no_blank_img.paste(slide_img, (now_x_num * sprite_width, now_y_num * sprite_hight))
                now_x_num += 1
        # 当前行有内容时，进入下一行
        if now_x_num != 0:
            now_y_num += 1
        # 计算最大值
        max_x_size = now_x_num * sprite_width if max_x_size < now_x_num*sprite_width else max_x_size
        # 重置x轴到0
        now_x_num = 0

    return get_slide_img(no_blank_img, Rectangle(0, 0, max_x_size, now_y_num * sprite_hight))


def mkdir(path: str):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
