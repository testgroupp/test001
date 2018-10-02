#coding=utf-8
import os,sys
import multiprocessing

def runtest(filename):

    print ("开始运行脚本:")
    os.chdir(sys.path[1])
    os.system('Python '+ filename)  # 执行脚本
    print ("运行完成退出")

list={"alltest.py","alltest1.py"}
thread=[]

#创建线程
for file in list:
    t=multiprocessing.Process(target=runtest,args=(file,))
    thread.append(t)

if __name__=='__main__':
    for i in thread:
        i.start()
    for i in thread:
        i.join()