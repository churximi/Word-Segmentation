#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：主程序调用接口
时间：2018年04月13日23:18:26
"""

from util import jieba_seg, get_wordfre, ngram

# 分词
all_words = jieba_seg("/Users/simon/Mycodes/Learn-Pandas/data.txt")

# 词频统计
word_fre = get_wordfre(all_words)
new_word_fre = ngram(all_words, 2)
with open("/Users/simon/Mycodes/Learn-Pandas/2gram_words.txt", "w+") as out:
    for item in new_word_fre:
        out.write("{}\t{}\n".format(item[0], item[1]))

if __name__ == "__main__":
    pass
