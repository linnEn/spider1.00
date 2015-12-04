# -*- coding: utf-8 -*-
import string

__author__ = 'admin'
import urllib

url_postfix=''
next_page=True

while next_page:
    page = urllib.urlopen('http://www.heibanke.com/lesson/crawler_ex00/'+url_postfix)
    next_page=False
    for line in page:
        line = line.decode('utf-8')
        if u'数字' in line:
            num = string.find(line, u'数字')
            for char in line:
                if char.isdigit:
                    first_num=char
                    break
            num = string.find(line,first_num)
            url_postfix = line[num:num+5]
            url_postfix = url_postfix.encode('ascii','replace')
            print url_postfix
            next_page=True
            break


print 'well done'
