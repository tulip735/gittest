# -*- coding:utf-8 -*-

# from time import ctime,sleep

# def tsfunc(func):
# 	def wrappedFunc():
# 		print '[%s] %s () called' %(ctime(),func.__name__)
# 		return func()
# 	return wrappedFunc
 
# @tsfunc
# def foo():
# 	pass
# foo()
# sleep(4)
# for i in range(2):
# 	sleep(1)
# 	foo()


#coding:utf-8
def testII(item,x=[]):
    print 'append before x id:%d'%(id(x))
    x.append(item)
def test(item,x=[]):
    print 'append before x id:%d'%(id(x))
    x.append(item)
    print 'append after x id:%d'%(id(x))
    return x
print test(1,[]) 
 #这里每次调用函数时，都试着给参数x 赋值，虽然每次都是相同的空序列[]，
 #但是每次x引用的对象已不是同的。
print test(2,[])
print test(3,[])


# def test(item,x=[]):#注意这里x 是局部的与函数外的x是不同的两个变量，并此x引用的
# # 是可变对象,

# # 并在函数定义时就定义此变量而不是在每次调用时再定义

#     print 'append before x id:%d'%(id(x))
#     x.append(item)
#     print 'append after x id:%d'%(id(x))
#     return x
# x= [1,2,3]
# print 'before x id:%d'%(id(x))
# print test(5)#注意这里函数参数 x，在调用时已绑定到可变对象序列上了。
# print test(6)#多次调用时，参数x不再具有赋值操作，始终操作为同一对象
# print 'after x id:%d'%(id(x))
# print '---------------result--------'
# print x

















