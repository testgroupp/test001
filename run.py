#coding=utf-8
import os,sys,time
import threading

def change_config():
    f = open(sys.path[1]+'\\config\\'+'config_alltest.py', 'r+',encoding='utf-8')
    sk = 0
    for line in f.readlines():
        if 'mc' in line:
            line_new = line.replace('mc', 'md')
            f.seek(sk - 1, 0)
            f.write('\n' + line_new)
            break
        else:
            sk = sk + len(line)
    f.close()

def undo_config():
    f = open(sys.path[1]+'\\config\\'+'config_alltest.py', 'r+',encoding='utf-8')
    sk = 0
    for line in f.readlines():
        if 'md' in line:
            line_new = line.replace('md', 'mc')
            f.seek(sk - 1, 0)
            f.write('\n' + line_new)
            break
        else:
            sk = sk + len(line)
    f.close()


def runtest(filename):
    os.system('Python '+ filename)

if __name__=='__main__':
    # runtest('alltest.py')
    # change_config()
    # runtest('alltest.py')
    # undo_config()
    pro=[]
    p1=threading.Thread(target=runtest,args=('alltest.py',))
    pro.append(p1)
    p2=threading.Thread(target=runtest,args=('alltest.py',))
    pro.append(p2)

    for p in pro:
        p.start()
        change_config()
        time.sleep(3)
    for p in pro:
        p.join()
    undo_config()