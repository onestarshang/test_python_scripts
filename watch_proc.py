#coding = utf-8
import sys, os, time
import subprocess

cmd = "python child.py"
print time.time()
sub2 = subprocess.Popen(cmd, shell=True)

while 1:
    ret1 = subprocess.Popen.poll(sub2)
    if ret1 == 0:
        print sub2.pid,'end'
        break
    elif ret1 is None:
        print  'running'
        time.sleep(10)
    else:
        print ret1
        print sub2.pid,'termination'
        break
print time.time()
