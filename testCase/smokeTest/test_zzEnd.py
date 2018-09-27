#coding=utf-8
from mylog import *
import unittest
class EndCase(unittest.TestCase):
    """
    所有用例执行完成标识
    """
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_endCase(self):

        logger.info("--------------------------------------------------------------")
        logger.info("-----------------------所有用例运行完成-----------------------")
        logger.info("--------------------------------------------------------------")