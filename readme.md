# 文本特征分析项目开发文档

这是一个用于提取文本特征的项目，底层使用了PaddleNLP开源框架

## 项目环境搭建

**首先进入项目的虚拟环境；**

**接着，执行下面语句，把项目加入虚拟环境的环境变量中:**

```shell
python addProjectEnv.py
```

**然后执行下面代码，安装项目依赖包：**

```shell
pip install -r requirements.txt
```

至此，开发环境已搭建完毕，详细的项目模块使用实例，可到文件夹目录下：`Text/test`下自行测试

**另外，你也可以选择手动安装核心库：**

[飞浆核心库](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/windows-pip.html)

因为无显卡，这里选取的是CPU版本，安装命令为：

```shell
python -m pip install paddlepaddle==2.3.0 -i https://mirror.baidu.com/pypi/simple
```

[飞浆NLP](https://github.com/PaddlePaddle/PaddleNLP/blob/develop/docs/get_started/installation.rst)

```shell
# 安装之前，请确认已安装完飞浆核心库
pip install --upgrade paddlenlp>=2.0.0rc -i https://pypi.org/simple
```

[FastApi](https://fastapi.tiangolo.com/zh/)

```shell
pip install fastapi[all]
```

[SqlAlchemy](https://www.sqlalchemy.org/)

```shell
pip install sqlalchemy
```

[LAC](https://github.com/baidu/lac)

```shell
pip install LAC --upgrade
```

[dotenv](https://pypi.org/project/python-dotenv/)

```shell
pip install python-dotenv
```

## 项目使用

输入以下命令，启动fastapi后台即可

```python
python main.py
```

## 指标详细信息

[详细信息](https://p-bf8j.tower.im/p/nnyl)

## 注意事项

- 安装完paddlepaddle使用时报错
  - ImportError: DLL load failed while importing core_avx: 找不到指定的模块。
  - 解决办法参考：[链接](https://aistudio.baidu.com/paddle/forum/topic/show/992594)
  - 下载安装重启后即可

- 在使用开放对话模型时候，有一个模块会引入jieba，导致控制台多了很多不必要的输出，如需取消这些输出提示，按照以下步骤即可
  - 飞浆的taskflow模块中 ```from .sentiment_analysis import SentaTask, SkepTask``` SkepTask中引入了```JiebaTokenizer```
  - 在```JiebaTokenizer```里面修改成以下代码即可
  
    ```python
    from .vocab import Vocab
    import logging

    import jieba
    # 去除 Building prefix dict from the default dictionary 的输出提示
    jieba.setLogLevel(logging.INFO)
    ```

- numpy库过高也会报一些不必要的警告信息
  - 在numpy的中写入

    ```python
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    ```
