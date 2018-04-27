#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：哈工大语言云使用测试，API调用
时间：2017年08月25日14:31:47
环境：python3
参考：http://www.ltp-cloud.com/document/
"""

import requests
import traceback
import time


def ltp_cloud(p_text, p_pattern='ws', p_format='xml'):
    """通过LTP语言云API调用获取自然语言处理结果
    :param p_text:输入文本字符串
    :param p_pattern:指定LTP分析的格式
    :param p_format:返回结果的格式
    :return:分析结果
    """

    url_get_base = "http://api.ltp-cloud.com/analysis/"
    args = {
        'api_key': 'y622c3B38TKcVPeh1wAwrVTDCbCrfqxGplrhHQ7l',  # 用户注册语言云服务后获得的认证标识
        'text': p_text,
        'pattern': p_pattern,  # 指定分析模式，有ws、pos、ner、dp、sdp、srl和all
        'format': p_format  # 结果格式，有xml、json、conll、plain（不可改成大写）
    }

    cont = ''
    try:
        response = requests.get(url=url_get_base, params=args)  # get方法
        cont = response.text
    except():
        traceback.print_exc()  # 跟踪错误

    return cont


def word_seg():
    """分词功能，设置分析模式为ws分词模式
    :return: 分词结果文本
    """
    start_time = time.time()
    output = open("result/LTP语言云分词结果.txt", "w+")
    with open("files/待分词文本.txt") as f:
        for line in f:
            content = ltp_cloud(line, 'ws', 'plain')  # 传入文本、分析模式、结果格式
            output.write(content.replace("\n", " ") + "\n")  # 由于LTP会自动分句，所以将分开的句子再合为一行
    output.close()
    end_time = time.time()

    print("程序结束，耗时：%.2f秒" % (end_time - start_time))


if __name__ == "__main__":
    word_seg()
