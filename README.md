# CPM-KG


This is an efficient implementation for large-scale knowledge representation learning (KRL) on **Wikidata** dataset. It currently implements **DistMult** method based Pytorch framework.
Statistics are as follows.
|  # Entities   | # Relations  | # Triplets | # dimensions |
|  ----  | ----  | ---- | ---- |
| 84752481  | 1288 | 4,7759,8890 | 256 |

Pretrained knowledge emebddings are provided as follows. They are trained 1000 iterations using eight V100 GPUs. 

- rel2id.txt (13K)   链接: https://pan.baidu.com/s/11AJpuO6fqigEmYmUkSBKuA  密码: sq03
- ent2id.txt (1.5G)   链接: https://pan.baidu.com/s/1QD8RuJrH12d98pgR0gcs0Q  密码: vnkc
- final_distmult_1000_compressed.tar.gz (10G) 链接: https://pan.baidu.com/s/1BjZ7oTuQ_Xjf3olJBeca8A  密码: hlbv
