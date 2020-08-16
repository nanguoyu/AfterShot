## Introduction

[中文介绍](./README_CN.md)

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
 
1. Start service

    ``` 
    python main.py
    ``` 

2. Take a screenshot 
 
    I recommend you to use [snipaste](https://zh.snipaste.com/) get a screen capture. For example, F1 is the hot key to
    get screenshot in my MacBookPro. Then I copy the imag in the clipboard.
    
3. Recognition
    
    Press F2, this tool would try to convert the image in the clipboard to words and then copy results to the clipboard.
    
 