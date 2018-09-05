# coding=utf-8
import unittest,time
import HTMLTestRunner
import sys,os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 构造测试集
suite = unittest.TestSuite()
# 定义测试文件查找目录
dir = sys.path[1]+"\\testCase"
# 定义discover方法的参数
discover = unittest.defaultTestLoader.discover(dir,
                                               pattern='test_reg.py',  # 匹配测试文件
                                               top_level_dir=None)
#方法筛选出来的用例，循环添加到测试套件中
for test_suite in discover:
    suite.addTests(test_suite)

now=time.strftime("%Y%m%d_%H%M")
filename =sys.path[1]+ "\\Result\\reports\\"+now+".html" # 测试报告存放路径
fp = open(filename, 'wb')  # r只读   wb:读写
# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,  # 指定测试报告文件
                                       title="测试报告",  # 报告标题
                                       description="用例执行情况")  # 报告副标题

#定义发送邮件
def send_mail(report_file):
    # 邮件服务器
    mail_host = 'smtp.gmail.com'
    # 端口
    mail_port = 25
    # 发件人地址
    mail_user = 'delf@networkws.com'
    # 发件人密码
    mail_pwd = 'lxyjhhxpwsxcztbn'
    # 邮件标题
    mail_subjet ="测试报告"+now
    # 收件人地址list
    # mail_to = ['delf@networkws.com','hiro@infinitesys.my','muse@networkws.com','demong@networkws.com','scki@networkws.com']
    mail_to = ['delf@networkws.com']
    # 读取测试报告内容
    with open(report_file, 'r', encoding='UTF-8') as f:
        content = f.read()

    msg = MIMEMultipart('mixed')
    # 添加邮件内容
    msg_html = MIMEText("冒烟测试报告", 'html', 'utf-8')
    msg.attach(msg_html)

    # 添加附件
    msg_attachment = MIMEText(content, 'html', 'utf-8')
    msg_attachment["Content-Disposition"] = 'attachment; filename="{0}"'.format(report_file)
    msg.attach(msg_attachment)

    msg['Subject'] = mail_subjet
    msg['From'] = mail_user
    msg['To'] = ';'.join(mail_to)

    try:
        smtp = smtplib.SMTP(mail_host, mail_port)
        smtp.starttls()
        # 登陆
        print(smtp.login(mail_user, mail_pwd))
        # 发送邮件
        smtp.sendmail(mail_user, mail_to, msg.as_string())
        # 退出
        smtp.quit()
    except Exception as e:
        print("Exceptioin ", e)

#查找测试报告目录，找到最新生成的测试报告文件
def send_Report():
    # 报告目录
    report_dir =sys.path[1]+ '\\Result\\reports'
    list =os.listdir(report_dir)[-1]
    file=report_dir+"\\"+list
    '''
    lists=os.listdir(result_dir)
    # 重新按时间对目录下的文件进行排列
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
    # print('最新的文件为： ' + lists[-1])
    file = os.path.join(result_dir, lists[-1])
    print("file:",file)
    '''
    send_mail(file)

if __name__ == '__main__':
    # 执行用例
    runner.run(suite)
    fp.close()
    send_Report()