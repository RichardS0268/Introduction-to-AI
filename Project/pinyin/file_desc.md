#### bin
该目录下的三个文件功能（模型，算法）完全相同，应对不同的使用场景
> 注：请确保运行以下三个程序时src文件夹已下载，否则训练过程中会出错
+ IM_shell.py:
  + 直接在命令行中输入`python IM_shell.py`运行，之后通过命令行输入全拼，程序将返回相应结果，若要终止程序，可向命令行输入'exit'
+ IM_test.py:
  + 用于文件输入输出，运行方式：`python IM_test.py input_path output_path`（两个参数分别为测例文件的路径及输出结果文件保存的路径）
+ IM.ipynb：
  + 开发时所写
  + 如果在运行上面两个文件出现路径方面的错误(本地调试时均可正常运行)，可通过此文件进行调试

#### data
+ input.txt: 
  + 实验验提供的测例
+ my_output:
  + 模型输出结果
+ std_output.txt：
  + 测例标准输出

#### src
+ MPDH
    >注：
    >1. '0_data/0_all.csv'和'1_data/1_all.csv'为bin中程序里模型训练要加载的数据
    >2. 如要运行run_0.py，run_1.py，可在Process/log中查看各进程运行进度，在进程结束后log文件及中间产生的csv文件自动删除
    >3. 最大进程数不要开得太大，不然可能死机
  + run_0.py 
    + 多线程计算转移矩阵
  + run_1.py 
    + 多线程计算发射矩阵
  + run.ipynb 
    + 开发时写，如运行上面两个程序出错，可通过此文件调试
+ data_handler.ipynb:
  + 数据预处理文件
+ pinyin_normal.txt, sentences_normal.txt
  + 预处理后的数据文件
  
#### z_others
+ 