# CPM-KG

本项目旨在提供大规模知识图谱的预训练表示，用于下游各类任务的知识强化。

## 1 图谱规模与模型

目前使用的图谱为Wikidata全局数据，整体的规模如下：

|  # 实体   | # 关系  | # 三元组 | # 维度 |
|  ----  | ----  | ---- | ---- |
| 84752481  | 1288 | 4,7759,8890 | 256 |

所采用的模型为Distmult。


## 2 数据下载

已有的图谱与表示下载请前往：https://cpm.baai.ac.cn/download.html

## 3 使用方法

#### 3.1 安装依赖

使用`pip install -r requirements.txt`来安装所需的依赖。

#### 3.2 使用

读取数据请参考`sample.py`文件，通过实体id和关系id可以获取其对应的表示（返回为`numpy.array`格式）。

## 4 未来工作

目前的版本为初步版本，该项目仍在更新当中，我们正在训练其他图谱与模型，未来也会逐步放出。

## 5 引用

```[latex]
@article{cpm-v1,
  title={CPM: A Large-scale Generative Chinese Pre-trained Language Model},
  author={Zhang, Zhengyan and Han, Xu, and Zhou, Hao, and Ke, Pei, and Gu, Yuxian and Ye, Deming and Qin, Yujia and Su, Yusheng and Ji, Haozhe and Guan, Jian and Qi, Fanchao and Wang, Xiaozhi and Zheng, Yanan and Zeng, Guoyang and Cao, Huanqi and Chen, Shengqi and Li, Daixuan and Sun, Zhenbo and Liu, Zhiyuan and Huang, Minlie and Han, Wentao and Tang, Jie and Li, Juanzi and Sun, Maosong},
  year={2020}
}
```
