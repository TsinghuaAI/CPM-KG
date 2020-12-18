# CPM-KG


## 1 相关库

首先需要安装各种依赖，主要为PyTorch与Numpy。

## 2 图谱规模与模型

目前使用的图谱为Wikidata全局数据，整体的规模如下：

|  # 实体   | # 关系  | # 三元组 | # 维度 |
|  ----  | ----  | ---- | ---- |
| 84752481  | 1288 | 4,7759,8890 | 256 |

所采用的模型为Distmult。


## 3 数据下载

已有的图谱与表示下载链接如下：

- rel2id.txt (13K)   链接: https://pan.baidu.com/s/11AJpuO6fqigEmYmUkSBKuA  密码: sq03
- ent2id.txt (1.5G)   链接: https://pan.baidu.com/s/1QD8RuJrH12d98pgR0gcs0Q  密码: vnkc
- final_distmult_1000_compressed.tar.gz (10G) 链接: https://pan.baidu.com/s/1BjZ7oTuQ_Xjf3olJBeca8A  密码: hlbv

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
