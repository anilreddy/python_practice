# Names, Variables, Code, Functions

def print_two(*args):
	x, y = args
	print "x: %r, y: %r" %(x, y)

def print_two_again(x, y):
	print "x: %r, y: %r" %(x, y)

def print_one(x):
	print "x: %r" %x

def print_none():
	print "Nothing to print!."

print_two("Anil", "Reddy")
print_two_again(10, 20)
print_one("Tester")
print_none()
