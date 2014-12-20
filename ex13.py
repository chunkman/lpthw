from sys import argv

script, first, second, third = argv

#print "The script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third

name = raw_input("What is your name? ")
age = raw_input("What is your age? ")
gender = raw_input("What is your gender? ")
print "Hello, my name is %s and I'm a %s year old %s who likes %s, %s and %s." % (
        name, age, gender, first, second, third)
