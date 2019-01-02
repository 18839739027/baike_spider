# -*- coding: utf-8 -*-
# @Time    : 2019/1/2  10:39
# @Author  : zhangxinxin
# @Email   : 778786617@qq.com
# @Software: PyCharm

import time
from . import html_downloader, html_outputer, html_parser, url_manager

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_outputer.HtmlOutputer()

    def craw(self, root_url, page_amount=5, time_sleep=None):
        count = 1
        # 添加第一个待爬取url
        self.urls.add_new_url(root_url)
        # 如果集合中有url, 就取出一个url 请求， 没有链接则跳出。
        while self.urls.has_new_url():
            try:
                # 开始爬取
                new_url = self.urls.get_new_url()
                print(f'craw{count}:{new_url}')
                # 请求url, 返回html
                html_content = self.downloader.download(new_url)
                # xpath 解析html，得到需要的数据
                new_urls, new_data = self.parser.parse(html_content)
                # 一个词条页面上关联的a 链表列表加入到url 管理器中待爬取
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_url, new_data)
                count += 1
                if count > page_amount:
                    break

                time.sleep(2)
            except Exception as e:
                print(e)
                print(f'抓取失败:{new_url}')
        self.output.output_html()
        # self.outputer.output_html()


if __name__ == '__main__':
    ROOT_URL = 'https://baike.baidu.com/item/Python/407313'
    # 第一个要爬取的页面
    PAGE_AMOUNT = 5
    # 总共请求多少页
    TIME_SLEEP = 2
    # 请求间隔
    spider = SpiderMain()
    spider.craw(ROOT_URL, PAGE_AMOUNT, TIME_SLEEP)