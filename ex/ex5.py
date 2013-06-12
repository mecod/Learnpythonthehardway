# -- coding: utf-8 --
my_name = 'Zed A. Shaw'
my_age = 30 # 差几天
my_height = 168 # 厘米
my_weight = 68 # 公斤
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'
test = """hello,\nworld"""

print "Let's talk about %s." % my_name
print "He's %d cms tall." % my_height
print "He's %d kilos heavy." % my_weight
print "Have a test.%s" %test
print "Have a test.%r" %test
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# 改正错误语句
print "If I add %d, %d, and %d I get %d." %(
    my_age, my_height, my_weight, my_age + my_height + my_weight)
