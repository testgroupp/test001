import logging
import sys,time

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# 创建handler，写入日志文件
now=time.strftime("%Y%m%d_%H%M%S")
fh = logging.FileHandler(sys.path[1]+'\\Result\\logs\\'+ now +'.log')
fh.setLevel(logging.INFO)
# 创建handler，输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# 定义handler的输出格式
formatter = logging.Formatter('【%(asctime)s】【%(levelname)s】【%(message)s】')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 添加handler到handler
logger.addHandler(fh)
logger.addHandler(ch)