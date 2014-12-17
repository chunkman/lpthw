name = 'Zed A. Shaw'
age = 35
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
weight_in_kg = weight / 2.2046
height_in_cm = height / 0.39370

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# Tricky line comming up.
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
print "The weight in kilograms is %d." % weight_in_kg
print "The height in centimeters is %d." % height_in_cm
