# Date : 2020-07-17
# Author : Dong Wang

from PIL import ImageGrab
from PIL import Image
import base64
import yaml
from pynput import keyboard
from core import baiduOCR
from io import BytesIO
with open('config.yml', 'r') as f:
    config = yaml.load(f.read())
if not config:
    raise ValueError("wrong config")
bd = baiduOCR(AK=config['baidu']['APIKey'], SK=config['baidu']['SecretKey'])


def copy_img():
    img = ImageGrab.grabclipboard()
    if isinstance(img, Image.Image):
        img_buffer = BytesIO()
        img.save(img_buffer, 'png')
        img = base64.b64encode(img_buffer.getvalue())
        bd.ocr(img)


def on_press(key):
    pass
    # try:
    #     print('alphanumeric key {0} pressed'.format(
    #         key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))


def on_release(key):
    # print('{0} released'.format(
    #     key))
    if key == keyboard.Key.f2:
        copy_img()


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
