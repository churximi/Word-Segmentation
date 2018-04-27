#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：哈工大LTP学习（Mac环境）
时间：2017年08月25日09:22:59
"""

import os
from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
from pyltp import Parser

LTP_DATA_DIR = '/Users/simon/LTP_data'  # ltp模型目录的路径

# 分句
sents = SentenceSplitter.split('第一个句子，第二个句子？')  # 分句
print('\n'.join(sents))

# 分词
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型
segmentor = Segmentor()  # 初始化实例
# segmentor.load(cws_model_path)  # 加载模型
segmentor.load_with_lexicon(cws_model_path, 'files/用户词典2.txt')  # 添加用户词典
words = segmentor.segment("这是一个测试句子。")  # 分词
print(" ".join(words))
segmentor.release()  # 释放模型

# 词性标注（也支持外部词典）
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型
postagger = Postagger()  # 初始化实例
postagger.load(pos_model_path)  # 加载模型
words = ['元芳', '你', '怎么', '看']  # 分词结果
postags = list(postagger.postag(words))  # 词性标注
for w, p in zip(words, postags):
    print(w, p)
postagger.release()  # 释放模型

# 命名实体识别（能识别人名（Nh）、地名（Ns）、机构名（Ni））
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型
recognizer = NamedEntityRecognizer() # 初始化实例
recognizer.load(ner_model_path)  # 加载模型
words = ['元芳', '你', '怎么', '看']
postags = ['nh', 'r', 'r', 'v']
netags = recognizer.recognize(words, postags)  # 命名实体识别
print('\t'.join(netags))
recognizer.release()  # 释放模型

# 依存句法分析
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型
parser = Parser() # 初始化实例
parser.load(par_model_path)  # 加载模型
words = ['元芳', '你', '怎么', '看']
postags = ['nh', 'r', 'r', 'v']
arcs = parser.parse(words, postags)  # 句法分析
print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
parser.release()  # 释放模型


if __name__ == "__main__":
    pass
