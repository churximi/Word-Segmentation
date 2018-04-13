#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：1、结巴分词；2、结巴其他功能；3、词频统计
时间：2018年04月13日22:42:12
"""

import jieba
import jieba.posseg as pseg
from collections import Counter


def jieba_seg(input_file, output_file="result/分词结果.txt"):
    """
    结巴分词
    :param input_file: 输入文本
    :param output_file: 输出文本
    :return:
    """
    jieba.load_userdict("data/用户词典.txt")  # 加载自定义用户词典

    out = open(output_file, "w+")
    all_words = []
    with open(input_file) as f:
        for line in f:
            words = list(jieba.cut(line.strip()))
            all_words += words
            out.write(" ".join(words) + "\n")
    out.close()

    return all_words


def get_wordfre(all_words):
    """
    词频统计
    :param all_words: 输入全文词列表
    :return:
    """
    assert type(all_words) == list

    cnt = Counter(all_words)
    word_fre = cnt.most_common()
    with open("result/词频统计.txt", "w+") as out:
        for word, fre in word_fre:
            out.write("{} {}\n".format(word, fre))

    return word_fre


def jieba_others():
    """结巴其他功能"""

    seg = jieba.cut("这是一本关于信息检索的书。", cut_all=True)  # 全模式
    print("全模式分词: " + "/ ".join(seg))

    seg = jieba.cut("这是一本关于信息检索的书。", cut_all=False)  # 精确模式，默认
    print("精确模式分词: " + "/ ".join(seg))

    seg = jieba.cut_for_search("这是一本关于信息检索的书。")  # 搜索引擎模式
    print(", ".join(seg))

    words = pseg.cut("这是一本关于信息检索的书。")  # 词性标注
    for word, flag in words:
        print('{} {}'.format(word, flag))


if __name__ == "__main__":
    pass
