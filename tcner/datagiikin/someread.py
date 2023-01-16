# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:UmeAI
@File:someread.py
@Time:2022/12/13 15:17
@Read: 
"""
import jieba
import pickle

with open('./bigfiles/readdatafrommatterial.pick', 'rb') as source:
    source = pickle.load(source)

with open('./bigfiles/ad_material_data_clean_2ner_clean.pick', 'rb') as onlycleantext:
    onlycleantext = pickle.load(onlycleantext)

with open('./bigfiles/ad_material_data_clean_2ner_clean_with_interest_words.pick', 'rb') as f:
    data = pickle.load(f)
# a = '转运招财水晶手链。紫水晶足银手链转运招财超夯下杀入组再得入组精美款可选，总有一款适合你哦。占星学命运坠饰手链护身符爱情珠宝能量护身符运气风水香水'
# for i in jieba.cut(a):
#     print(i)
