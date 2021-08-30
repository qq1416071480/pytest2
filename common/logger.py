import logging
import os
import time
# dirname:返回文件路径  realpath:返回文件真实路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 日志文件路径
LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

class Logger():
    def __init__(self):
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))
        # 记录器
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 创建屏幕并设置默认等级
        self.consoleHandler = logging.StreamHandler()
        self.consoleHandler.setLevel(logging.INFO)
        # 创建文件并设置默认等级
        self.fileHandler = logging.FileHandler(self.logname, mode='a', encoding='utf-8')
        self.fileHandler.setLevel(logging.INFO)
        # 设置formatter格式
        self.formatter = logging.Formatter("%(asctime)s|%(levelname)s|%(filename)s|%(lineno)s|%(message)s")
        # 给处理器设置格式
        self.consoleHandler.setFormatter(self.formatter)
        self.fileHandler.setFormatter(self.formatter)
        # 记录器要设置处理器
        self.logger.addHandler(self.consoleHandler)
        self.logger.addHandler(self.fileHandler)
        # 定义一个过滤器
        # self.flt = logging.Filter('log')
        # 关联过滤器
        # self.logger.addFilter(flt)
        # self.fileHandler.addFilter(flt)


Logger = Logger().logger

# 测试代码
# if __name__ == '__main__':
#     Logger.info('测试开始')
#     try:
#         int(a)
#     except Exception as e:
#         Logger.exception(e)
#     Logger.info('测试结束')

