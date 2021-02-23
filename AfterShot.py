# Date : 2020-07-17
# Author : Dong Wang

import sys
from PIL import ImageGrab
from PIL import Image
import base64
import yaml
from pynput import keyboard
from core import baiduOCR
from io import BytesIO
import pyperclip
import argparse


def on_press(key):
    pass
    # try:
    #     print('alphanumeric key {0} pressed'.format(
    #         key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="AfterShot OCR Tool")
    parser.add_argument("--config", type=str, default='config.yml', help='config file')
    args = parser.parse_args()
    config_path = args.config
    with open(config_path, 'r') as f:
        config = yaml.load(f.read(), Loader=yaml.FullLoader)
    if not config:
        raise ValueError("wrong config")
    bd = baiduOCR(AK=config['baidu']['APIKey'], SK=config['baidu']['SecretKey'])


    def copy_img():
        img = ImageGrab.grabclipboard()
        if isinstance(img, Image.Image):
            img_buffer = BytesIO()
            img.save(img_buffer, 'png')
            img = base64.b64encode(img_buffer.getvalue())
            text = bd.ocr(img)
            pyperclip.copy(text)


    def on_release(key):
        if key == keyboard.Key.f2:
            copy_img()


    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
