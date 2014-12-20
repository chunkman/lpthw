from sys import argv

script, first, second, third = argv

name = raw_input("What is your name? ")
age = raw_input("What is your age? ")
gender = raw_input("What is your gender? ")
print "Hello, my name is %s and I'm a %s year old %s who likes %s, %s and %s." % (
        name, age, gender, first, second, third)
print "This is just a test branch. You should not see this."
