## Introduction

This is an OCR tool without any function of screenshot. There are
a lot of screen capture tools and no needs to build a new one. 
This tool tries to recognise an image file in clipboard.

## Install

``` 
git https://github.com/nanguoyu/AfterShot.git
cd AfterShot
pip install .
```

## Config your api

> This tool only supports the OCR API of Baidu

Fill APIKey and SecretKey in  config.yaml 

## Quick start
 
Start service
``` 
run main.py
```

When you get a screen capture, you press F2 and the result will be copied to clipboard