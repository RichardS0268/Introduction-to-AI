+ MPDH
    >注：
    >1. '0_data/0_all.csv'和'1_data/1_all.csv'为bin中程序里模型训练要加载的数据
    >2. 如要运行run_0.py，run_1.py，可在Process/log中查看各进程运行进度，在进程结束后log文件及中间产生的csv文件自动删除
    >3. 最大进程数不要开得太大，不然可能死机
  + run_0.py 
    + 多进程计算转移矩阵
  + run_1.py 
    + 多进程计算发射矩阵
  + run.ipynb 
    + 开发时写，如运行上面两个程序出错，可通过此文件调试
+ data_handler.ipynb:
  + 数据预处理文件
+ pinyin_normal.txt, sentences_normal.txt
  + 预处理后的数据文件

+ 数据获取：
    1. files.zip

    `wget https://cloud.tsinghua.edu.cn/f/1f6e33ed073e42cbb758/?dl=1 -O ./src/files.zip`

    `unzip ./src/files.zip`

    + pinyin_normal.txt
    + sentences.txt
    + sentences_normal.txt
    + sentences_raw.txt
    + 拼音汉字表.txt
    + 一二级汉字表.txt

    2. 语料库.zip

    `wget https://cloud.tsinghua.edu.cn/f/ad2a884a89204c1eaa15/?dl=1 -O ./src/语料库.zip`

    `unzip ./src/语料库.zip`

    注意：语料库中的txt文件都是gbk编码
