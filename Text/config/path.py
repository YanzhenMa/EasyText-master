import os
# from pathlib import Path

# 源码目录
SOURCE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 数据目录
DATA_DIR = os.path.join(SOURCE_DIR, 'data')
# 数据库链接地址
DB_ENGINE = 'sqlite:///{}?check_same_thread=False'.format(
    os.path.join(DATA_DIR, 'data.db'))


if __name__ == '__main__':

    print(SOURCE_DIR)

