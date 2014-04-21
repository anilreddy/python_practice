# Functions and Variables

def apples_and_bananas(apples, bananas):
	print "You have %d box of apples!" %apples
	print "You have %d bananas" %bananas
	print "We have lot of fruits!"
	print "Get a plate. \n"

print "We can just give the function numbers directly:"
apples_and_bananas(40, 30)

print "OR, we can use variables from our script:"
no_of_apples = 70
no_of_bananas = 10

apples_and_bananas(no_of_apples, no_of_bananas)

print "We can even do math inside too:"
apples_and_bananas(20 + 50, 70 + 90)

print "And we can combine the two, variables and math:"
apples_and_bananas(no_of_apples + 30, no_of_bananas + 40)
