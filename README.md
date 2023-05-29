# avatar
Randomly generate avatars
from PIL import Image, ImageDraw
import random

def generate_cartoon_avatar(size):
    # 创建空白图像
    image = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(image)

    # 随机生成颜色
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 绘制圆形头像
    draw.ellipse([(0, 0), (size, size)], fill=color)

    # 绘制随机眼睛
    eye_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    eye_size = size // 8
    eye_x = size // 4
    eye_y = size // 4
    draw.ellipse([(eye_x, eye_y), (eye_x + eye_size, eye_y + eye_size)], fill=eye_color)
    draw.ellipse([(eye_x + size // 2, eye_y), (eye_x + size // 2 + eye_size, eye_y + eye_size)], fill=eye_color)

    # 绘制随机嘴巴
    mouth_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    mouth_width = size // 2
    mouth_height = size // 4
    mouth_x = (size - mouth_width) // 2
    mouth_y = (size - mouth_height) // 2
    draw.rectangle([(mouth_x, mouth_y), (mouth_x + mouth_width, mouth_y + mouth_height)], fill=mouth_color)

    # 保存头像图像
    image.save("cartoon_avatar.png")

# 调用函数生成卡通头像
generate_cartoon_avatar(300)
