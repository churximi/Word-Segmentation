#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：LTP本地词性标注par_cmdline，输入文本每行一句，且已经分词和词性标注。
时间：2017年3月30日 18:16:15
"""

import os

project_path = r"D:\BookReviews\WordSegmentor\LTP"  # 项目文件夹目录

model_exe = "par_cmdline"  # 句法分析模块

threads_num = " --threads " + str(3)  # 更改线程数
input_path = " --input " + r"D:\BookReviews\WordSegmentor\file\output_pos.txt"  # 输入文件
output_path = r"D:\BookReviews\WordSegmentor\file\output_par.txt"  # 输出文件

command = "cd " + project_path + " & " + model_exe + threads_num + input_path + " > " + output_path
os.system(command)
