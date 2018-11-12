#coding=utf-8
from mylog import *
import unittest
from config.config_alltest import  *

class BeginCase(unittest.TestCase):
    """
    开始执行用例
    """
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_begintCase(self):
        plt=None
        if 'm' and 'c' in platform.lower():
            plt='摩臣'
        elif 'm' and 'd' in platform.lower():
            plt='摩登'
        else:
            logger.info('-------------------平台名输入错误！！！--------------------------')

        logger.info("-------------------------开始执行用例:【%s】-------------------------" %plt)
