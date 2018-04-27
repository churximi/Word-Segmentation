#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：LTP本地分词cws_cmdline，输入文本需要每行一句。（不能自动分句）
输入：将要分词的txt文本放在WordSegmentor\file文件夹，文件名为input.txt
输出：file文件夹下的output.txt文件
时间：2017年1月14日 15:49:30
"""

import os

project_path = r"/Users/simon/myprojects/ana2/分词/LTP"  # LTP项目文件夹目录

model_exe = "cws_cmdline"  # 分词模块，相当于ltp_test的last_stage=ws，但是输出格式不同

threads_num = " --threads " + str(3)  # 更改线程数
input_path = " --input " + r"D:\BookReviews\WordSegmentor\file\input.txt"  # 输入文件
seg_lexicon = " --segmentor-lexicon " + r"D:\BookReviews\WordSegmentor\file\userdic.txt"  # 分词用户词典
output_path = r"D:\BookReviews\WordSegmentor\file\output.txt"  # 输出文件

command = "cd " + project_path + " & " + model_exe + \
          threads_num + input_path + seg_lexicon + " > " + output_path
os.system(command)

if __name__ == "__main__":
    pass
