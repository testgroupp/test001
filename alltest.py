# coding=utf-8
import unittest,time
import HTMLTestRunner
import sys,os
import smtplib #邮件模块
from email.mime.text import MIMEText  #邮件内容
from email.mime.multipart import MIMEMultipart  #附件
from config import config_mail
from config import config_report

now=time.strftime("%Y%m%d_%H%M")

def runTestsToReport():
    # 构造测试集
    suite = unittest.TestSuite()
    # 定义测试文件查找目录
    dir = sys.path[1]+"\\testCase"
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(dir,
                                                   pattern='test_*.py',  # 匹配测试文件
                                                   top_level_dir=None)
    #方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        suite.addTests(test_suite)

    filename =sys.path[1]+ "\\Result\\reports\\"+now+".html" # 测试报告存放路径
    fp = open(filename, 'wb')  # r只读   wb:读写
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,  # 指定测试报告文件
                                           title=config_report.title,  # 报告标题
                                           description="用例执行情况")  # 报告副标题
    # 执行用例
    runner.run(suite)
    fp.close()

#发送邮件
def send_mail(report_file):
    # 第三方服务器设置
    sender =config_mail.sender
    password = config_mail.password
    receiver=config_mail.receiver

    msg = MIMEMultipart()  # 创建一个带附件的邮件实例
    msg['Subject'] =config_mail.Subject + "冒烟测试报告" + now
    msg['From'] = sender
    msg['To'] = ";".join(receiver)
    # 邮件正文内容
    content='<h1><font color="red">报告详情见附件(下载查阅效果更佳)</font><h1/>'
    msg.attach(MIMEText(content, 'html', 'utf-8'))

    # 构造附件1
    att = MIMEText(open(report_file, 'rb').read(), 'py', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename="{}"'.format("report"+now+".html")  # filename:自定义邮件名字
    msg.attach(att)
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com")  # 连接邮件服务器
        server.login(sender, password)  # 登录
        server.sendmail(sender, receiver, msg.as_string())  # 发送
        server.quit()
    except smtplib.SMTPException as e:
        print("邮件未发送：", e)

#找到最新生成的测试报告文件,并发送
def send_Report():
    # 报告目录
    report_dir =sys.path[1]+ '\\Result\\reports'
    list =os.listdir(report_dir)[-1]
    file=report_dir+"\\"+list
    send_mail(file)

if __name__ == '__main__':
    runTestsToReport()
    send_Report()