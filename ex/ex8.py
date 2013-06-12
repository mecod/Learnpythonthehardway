# -*- encoding: utf-8 -*-
formatter = "%r %r %r %r"
print "%s" % "打印字符"
print "%s %s" %("我知道这件事", "清楚吧")

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("I had this thing", 
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight"
)
