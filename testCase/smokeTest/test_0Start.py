#coding=utf-8
from mylog import *
import unittest
class BeginCase(unittest.TestCase):
    """
    开始执行用例
    """
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_begintCase(self):
        logger.info("--------------------------------------------------------------")
        logger.info("-------------------------开始执行用例-------------------------")
        logger.info("--------------------------------------------------------------")