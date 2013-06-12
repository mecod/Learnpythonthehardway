# -- encoding: utf-8 --
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# a string is put inside a string
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y

# a string is put inside a string
print "I said: %r." % x
# a string is put inside a string
print "I also said: '%s'." %y

hilarious = False
# a string is put inside a string
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
