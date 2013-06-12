# -*- coding: utf-8 -*-
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
	

age = raw_input('你几岁了？')

height = raw_input('你身高几何？')

weight = raw_input('你有多重？')

print "你%r岁了, 身高%r 厘米， 体重 %r。" % (
    age, height, weight)