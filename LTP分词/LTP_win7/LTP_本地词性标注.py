#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：LTP本地词性标注pos_cmdline，输入文本需要已分好词（有空白符间隔）；每行一句（不能自动分句）。
时间：2016年4月13日 20:22:39
"""

import os

project_path = r"D:\BookReviews\WordSegmentor\LTP"  # 项目文件夹目录

model_exe = "pos_cmdline"  # 词性标注模块

threads_num = " --threads " + str(3)  # 更改线程数
input_path = " --input " + r"D:\BookReviews\WordSegmentor\file\input.txt"  # 输入文件
pos_lexicon = " --postagger-lexicon " + r"D:\BookReviews\WordSegmentor\file\pos_lexicon.txt"  # 词典
output_path = r"D:\BookReviews\WordSegmentor\file\output_pos.txt"  # 输出文件

command = "cd " + project_path + " & " + model_exe + threads_num + input_path + " > " + output_path
os.system(command)
