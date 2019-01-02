# -*- coding: utf-8 -*-
# @Time    : 2019/1/2  10:39
# @Author  : zhangxinxin
# @Email   : 778786617@qq.com
# @Software: PyCharm


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        """
        添加一个新链接
        :param url:
        :return:
        """
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def has_new_url(self):
        """
        还有没有待爬取的url
        :return:
        """
        if len(self.new_urls) > 0:
            return True
        else:
            return False


    def get_new_url(self):
        """
        取一个新的url 准备请求它
        :return:
        """
        new_url = self.new_urls.pop()    # 随机删除一个元素并返回
        return new_url

    def add_new_urls(self, urls):
        """
        一个词条上的所有链接加入self.new.urls中
        :param urls:
        :return:
        """
        assert urls is not None, 'URLS 不能为空'
        for url in urls:
            self.new_urls.add(url)