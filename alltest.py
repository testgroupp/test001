# coding=utf-8
import unittest,time
import HTMLTestRunner

# 构造测试集
suite = unittest.TestSuite()
# 定义测试文件查找目录
dir = "E:\\test001\\testCase"
# 定义discover方法的参数
discover = unittest.defaultTestLoader.discover(dir,
                                               pattern='test*.py',  # 匹配测试文件
                                               top_level_dir=None)
#方法筛选出来的用例，循环添加到测试套件中
for test_suite in discover:
    suite.addTests(test_suite)

now=time.strftime("%Y%m%d_%H%M%S")
filename = "E:\\test001\\Result\\reports\\"+now+".html"  # 定义测试报告存放路径
fp = open(filename, 'wb')  # r只读   wb:读写
# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,  # 指定测试报告文件
                                       title="测试报告",  # 报告标题
                                       description="用例执行情况")  # 报告副标题
if __name__ == '__main__':
    # 执行测试
    runner.run(suite)
    fp.close()  # 关闭报告