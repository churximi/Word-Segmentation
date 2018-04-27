#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：
时间：
"""

import codecs

f = open(u"全部书评词性标注.txt")

fnew = codecs.open("newtxt.txt", "a", "utf-8")
dic = []
for line in f:
    temp = line.strip().split("\t")
    for item in temp:
        if item not in dic:
            dic.append(item)
            fnew.write(item.decode("utf-8") + "\n")

fnew.close()
f.close()
if __name__ == "__main__":
    pass
