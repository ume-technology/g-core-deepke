# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:UmeAI
@File:splitnewnertagdata.py
@Time:2022/12/13 22:43
@Read: 切分新的NER待标注数据; 完成标注后书移动到 alltageddata文件夹中
"""
import pickle

with open('ad_material_data_clean_2ner_clean_with_interest_words.pick', 'rb') as f:
    oricleandata = pickle.load(f)

with open('../newdata2ner_newtags/waittotagdata.txt', 'w+', encoding='utf-8') as f:
    for i in oricleandata[:1000]:
        for _ in list(i):
            f.write(_ + '\t\n')
        f.write('\n')
