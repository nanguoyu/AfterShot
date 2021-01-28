[English Introduction](./README.md)

AfterShot 是一个简单的OCR工具，支持截图、复制图片后的OCR。当你的剪切板里有一张需要OCR的图片时，按下F2，识别的内容就会存在你的剪切板。

AfterShot没有截图功能，需要依赖其他截图工具例如：snipaste、QQ、WeChat、windows与Mac自带的截图功能。
这里就要指出没有截图功能的原因：1.我习惯用snipaste 2.自己重复造轮子没意义 3.很多人说OCR工具就是调用大厂的API，所以这就是最简单的调用API。

最佳的使用组合是：
按下F1使用snipaste截图并复制，再按下F2在剪贴板中得到识别结果。

## 下载安装

```shell
git clone https://github.com/nanguoyu/AfterShot.git
cd AfterShot
pip install .
```

## 配置

修改config.yml中的APIKey和SecretKey

以百度智能云为例：
1. 登录https://ai.baidu.com/tech/ocr
2. 创建新应用，获得API Key和Secret Key
3. 填写在config.yml对应的位置

## 使用

1. 启动程序

	```python
	python main.py
	```

2. 将截图/网络图片/本地图片复制到剪贴板
3. 按下F2，获得识别结果。（根据网络状况不同，可能需要等待1秒）

