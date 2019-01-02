# -*- coding: utf-8 -*-
# @Time    : 2019/1/2  10:39
# @Author  : zhangxinxin
# @Email   : 778786617@qq.com
# @Software: PyCharm
from lxml import etree


class HtmlParser(object):
    def parse(self, html_content):
        """
        接收网页的html内容响应,xpath解析，返回想要的数据
        :param html_content:{str} '<html></html>'
        :return: 一个字典， 一个列表
        """
        assert html_content is not None, 'html_content 为空'
        dom = etree.HTML(html_content)
        title = dom.xpath('//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()')[0]
        summary = dom.xpath('//div[@class="lemma-summary"]/div/text()')[0]
        new_urls = dom.xpath('//div[@class="main-content"]//a[@target="_blank"]/@href')
        for index, href in enumerate(new_urls):
            # pattern_href[index] = 'https://baike.baidu.com' + href
            new_urls[index] = 'https://baike.baidu.com' + href
        new_data = {'title': title, 'summary': summary}
        return new_urls, new_data
