- 2022/10/21 把BIES标注的数据拉取了过来【采用BIES的方式表述NER数据】
  - 因为这个数据方便处理完为该TC模型需要的数据格式。
  - ~~因此会把这个数据统一标注为BMES数据，到时候公司的这个数据可以删除。~~
  - ~~这部分标注完成的标准的的BMES数据已经迁移到nermodelbert项目中；只是这个项目还未处理。~~
 
### 2022/12/22 关于TC数据集准备以及模型训练的工作   
- 运行该代码，首先是数据处理: 数据清洗方式按照如下过程进行：readdatafrommatterial.py  是读取原始的material表中的数据；
 
- 【老方案数据标注】数据标注与标准的训练数据生成：
  - giikindataset\ad_material_data\clean_materialdata2ner.py 生成的数据是纯净的ad text数据，可以用来做NER标注；
  - 执行 splitnewnertagdata.py 脚本分割出来一些待标注的数据：生成待标注的数据：存储在：newdata2ner_oldtags giikinnerdata.txt文件中: BIES标注数据；
  - 执行 checkdatalabels.py 检查 giikinnerdata.txt 文件标注是否异常；
  - 标注后的数据统一维护在：newdata2ner_oldtags   alldata.txt 中；

- 标注的标签数据的转换与数据分割
  - convertstandardtagdata2nertraindata.py，这个脚本生成的数据，就是标准的NER标注可以参与训练的数据；通过该脚本后会生成如下数据：
    - mid_data\train.json（需要将该文件copy to raw_data\stack.json，执行splittraindata.py脚本，将stack.json进行数据切分以及将数据最终转换为TC要求的标准NER数据） 
    - mid_data\ner_ent2id.json
    - mid_data\labels.json 
    

### 新的数据标注方案
- 这个标注方案是为了进一步改善知识图谱的实体数据识别；
- 存储在newdata2ner_newtags waittotagdata.txt； 截至20221222；划分的是1000条数据进行标注


### 模型的训练和预测；