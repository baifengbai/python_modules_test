#coding:utf8
'''
状态模式测试
'''
import time
from state import curr, switch, stateful, State, behavior

@stateful
class People(object):
    class Workday(State):
        default = True
        @behavior
        def day(self):
            print 'work hard.'

    class Weekend(State):
        @behavior
        def day(self):
            print 'play harder!'



people = People()
while 1:
    for i in xrange(1,8):
        if i == 6:
            switch(people, People.Weekend)
        if i == 1:
            switch(people, People.Workday)
        people.day()
        time.sleep(1)