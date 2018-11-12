#coding=utf-8
import os,sys

if __name__=='__main__':
    filename = sys.path[1] + '\\testCase\\smokeTest\\test_bet.py'
    n=1
    while 1:
        os.system('Python ' + filename)
        print('运行完成%d次' %n)
        n=n+1