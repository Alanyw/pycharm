# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 创建BeautifulSoup对象
soup = BeautifulSoup(html, "lxml")

# 利用本地HTML文件创建对象
# soup = BeautifulSoup(open('index.html'))

# print soup.prettify()
# print soup.title
# print soup.head

# 验证对象类型
# print type(soup.a)

# soup 对象本身比较特殊，它的 name 即为 [document]，对于其他内部标签，输出的值便为标签本身的名称。
# print soup.name
# print soup.head.name

# 打印标签的所有属性,得到的类型是一个字典
# {'class': ['title'], 'name': 'dromouse'}
# print soup.p.attrs
# 单独获取某个属性
# print soup.p['class']

