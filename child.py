#coding = utf-8
import sys, os, time

def run():
    count = 50
    while count > 0:
        print 'hehe'
        count -= 5
        time.sleep(5)
    print 'child is end'
        
run()
