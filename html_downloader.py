# -*- coding: utf-8 -*-
# @Time    : 2019/1/2  10:38
# @Author  : zhangxinxin
# @Email   : 778786617@qq.com
# @Software: PyCharm
import requests


class HtmlDownloader(object):
    def download(self, url):
        # if url is None:
        #     # return None
        #     raise Exception('url 不能为空')
        assert url is not None, 'download()方法参数url不能为None'
        headers = {
            'Host': 'baike.baidu.com',
            # 'Host': 'gsp0.baidu.com',
            'Referer': 'https://baike.baidu.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f'请求失败， code{response.status_code}')
        return response.text


