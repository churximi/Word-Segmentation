#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：主程序调用接口
时间：2018年04月13日23:18:26
"""

from util import jieba_seg, get_wordfre

# 分词
all_words = jieba_seg("data/test.txt")

# 词频统计
word_fre = get_wordfre(all_words)

if __name__ == "__main__":
    pass
