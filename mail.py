#coding=utf-8
import yagmail
n=1

 #链接邮箱服务器
yag = yagmail.SMTP( user="312071687@qq.com", password="njizfzirsugzbgch", host='smtp.qq.com')
#发送邮件 to：可传一个list    subject：主题        contents：正文           attachments：附件
yag.send('554112771@qq.com', '',"")
