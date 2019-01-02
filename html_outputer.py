# -*- coding: utf-8 -*-
# @Time    : 2019/1/2  10:39
# @Author  : zhangxinxin
# @Email   : 778786617@qq.com
# @Software: PyCharm


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def output_html(self):
        file = open('output.html', mode='w')
        file.write('<html>')
        file.write('<body>')
        for row in self.datas:
            file.write('<tr>')
            file.write(f'<td>链接:{row[0]}</td><br>')
            file.write(f'<td>标题：{row[1]["title"]}</td><br>')
            file.write(f'<td>简介：{row[1]["summary"]}</td><br>')

            file.write('</tr>')
        file.write('</body>')
        file.write('</html>')

    def collect_data(self, new_url, new_data):
        assert new_url is not None
        assert new_data is not None
        self.datas.append((new_url, new_data))

