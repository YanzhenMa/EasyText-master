'''日志模块'''
import time
import logging

from Text.config.path import LOGS_DIR

# 初始化log
log = logging.getLogger('EasyText')
# 配置日志级别,默认为warning级别
log.setLevel(logging.INFO)

# 创建一个格式化对象
formatter = logging.Formatter(fmt=" %(name)s %(asctime)s [line:%(lineno)d]%(filename)s %(levelname)s - %(message)s",
                              datefmt="%Y-%m-%d %H:%M:%S")

# 配置日志输出到控制台
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
# 设置输出格式
console.setFormatter(formatter)
log.addHandler(console)

# 配置日志输出到文件
# 详细输出内容
log_file_name = time.strftime("%Y-%m-%d.log", time.localtime())
logs_path = LOGS_DIR / log_file_name
file_logging = logging.FileHandler(logs_path, encoding='utf-8')
file_logging.setLevel(logging.INFO)
file_logging.setFormatter(formatter)
log.addHandler(file_logging)


log.info(u"*".center(60, "*"))
if __name__ == "__main__":
    '''测试日志功能
    '''
    log.debug("debug")
    log.info("info")
    log.warning("warning")
    log.error("error")
    log.critical("critical message")
