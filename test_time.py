# -*- coding: cp936 -*-
import time
t = time.time()#tΪʱ���
t = t-3600
lt = time.localtime(t)  #ltΪʱ��Ԫ��
mt = time.mktime(lt)  #mtΪʱ�������ת��
gt1 = time.strftime('%Y-%m-%d',lt)
gt2 = time.strftime('%H:%M:%S',lt)
#print time.strftime("%H:%M:%S")
#print gt2
#�����ǰʱ��
def nowtime(num,j=1,c=10):
    i = 0
    #���һ��ʱ��
    if num==1:
        global gt1,gt2
        print gt1
        print gt2
    #������ʱ�䣬����ʹ����Զ���Ĭ��1s��10��
    if num==2:
        print gt1
        while 1:
            i+=1
            t = time.time()
            lt = time.localtime(t)
            gt1 = time.strftime('%Y-%m-%d',lt)
            gt2 = time.strftime('%H:%M:%S',lt)
            print gt2
            if i==c:
                break
            time.sleep(j)
def deftime():
    at = time.asctime(lt)  #ʱ��Ԫ��ת��ΪĬ��ʱ����ʾ��ʽ 'Sat Jun 28 19:07:56 2014'
    st = time.strptime(at) #��ת��

def test_clock():
    print time.clock()
    time.sleep(1)
    print time.clock()  #�ӵ�һ�ε��õ���ǰ��ʱ���
    time.sleep(2)
    print time.clock()  #�ӵ�һ�ε��õ���ǰ��ʱ���
    time.sleep(3)
    print time.clock()  #�ӵ�һ�ε��õ���ǰ��ʱ���
    return

def call_time(func):
    '''װ����������ִ��ʱ��'''
    def _deco(*args, **kwargs):
        start = time.clock()
        result = func(*args, **kwargs)
        print '%s() : %s' % (func.__name__, time.clock())
        return result
    return _deco

def get_timestamp():
    s = "2016-04-07 00:00:00"
    t = time.strptime(s, "%Y-%m-%d %H:%M:%S")
    print time.mktime(t)
    return 


if __name__ == "__main__":
    #test_clock()
    get_timestamp()
    pass
    
    
