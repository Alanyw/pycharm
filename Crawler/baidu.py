# -*- coding: utf-8 -*-
import re

import sys
from bs4 import BeautifulSoup
import urllib2
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class BaiDu:
    def __init__(self, baseUrl, seeLz):
        self.baseUrl = baseUrl
        self.seeLZ = "?see_lz=" + str(seeLz)

    # 转入页码，获取该页帖子的URL
    def getPage(self, pageNum):
        try:
            url = self.baseUrl + self.seeLZ + "&pn=" + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"URL错误，错误原因", e.reason
                return None


baseUrl = "http://tieba.baidu.com/p/3138733512"
baidu = BaiDu(baseUrl, 1)
url = baidu.getPage(4)
soup = BeautifulSoup(url, "lxml")
title = soup.find_all(class_=re.compile("core_title_txt pull-left text-overflow"))
print str(title).encode("utf-8")
