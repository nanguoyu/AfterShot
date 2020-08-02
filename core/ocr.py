# encoding:utf-8

import requests
import base64


class baiduOCR(object):
    def __init__(self, AK, SK):
        assert isinstance(AK, str) and isinstance(SK, str)
        self.access_token = self._get_access_token(AK, SK)
        if self.access_token is None:
            raise ValueError("get access_token fail")

    def _get_access_token(self, AK, SK):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (
        AK, SK)
        response = requests.get(host)
        if response:
            access_token = response.json()['access_token']
            return access_token
        else:
            return None

    def ocr(self, img):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"

        params = {"image": img}
        access_token = self.access_token
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())