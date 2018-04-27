#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：哈工大LTP分词
时间：2017年08月25日09:22:59
备注：LTP提供个性化分词功能，详见
     http://pyltp.readthedocs.io/zh_CN/latest/api.html#id2
注意：需要提前下载LTP模型数据
"""

from pyltp import Segmentor


def ltp_seg(file_path):
    cws_model_path = "files/cws.model"  # 分词模型
    user_dic = "files/用户词典2.txt"  # 用户词典
    output = open("result/分词结果.txt", "w+")

    segmentor = Segmentor()  # 初始化实例
    segmentor.load_with_lexicon(cws_model_path, user_dic)

    with open(file_path) as f:
        for line in f:
            words = segmentor.segment(line.strip())  # 分词
            output.write(" ".join(words) + "\n")

    segmentor.release()  # 释放模型
    output.close()


if __name__ == "__main__":
    ltp_seg("files/待分词文本.txt")
