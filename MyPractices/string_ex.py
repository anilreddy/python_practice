
# Strings in Python Programming Language

# Basic Print Statements

print "Hello World!"
print('I am new to Python!')
print "Hey! This is 'Anil'."



# More Basic Print Statements

print "I will now count my Chickens:"
print "Hens", 32 + 50 / 5
print "Roosters", 100 - 50 * 5 / 2
print "Now I will count Eggs:"
print 5 + 6 - 3 * 7 % 3
print "Is it True that 3 + 2 < 5 - 10 ?"
print 3 + 2 < 5 - 10
print "What is 9 + 4 ?", 9 + 4
print "Is it greater ?", 5 > -2
print "Is that greater or equal ?", 5 >= -2
print "Is less or equal ?", 5 <= -2



# Variables & Names

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_in_a_car = passengers / cars_driven

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "car pool today"
print "We need to put about", average_passengers_in_a_car, "in each car"



# More Variables & printing

my_name = 'Anil Reddy'
my_age = 25
my_height = 72
my_weight = 160
my_eyes = 'Brown'
my_hair = my_eyes
my_teeth = 'White'

print "Let's talk about %s" %my_name
print "He's %d inches tall" %my_age
print "He's %d pounds heavy" %my_weight
print "Actually its not too heavy!"
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "He's teeth %s color" %my_teeth


# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight)



# Strings & Text

x = "There are %d types of people." %10
binary = 'binary'
do_not = "don't"
y = "Those who knows %s and those who %s" %(binary, do_not)

print x
print y

print "I said: %r." %x
print "I also said: '%s'." %y

fun = False
joke = "Ins't that joke so funny?! %r"

print joke % fun

a = "This is the left side of...."
b = "A string with a right side."

print a + b

# Printing, Printing

formatter = "%r, %r, %r, %r"

print formatter %("Anil", "Sunil", "Naveen", "Reddy")
print formatter %(10, 20, 30, 40)
print formatter %(True, False, True, False)
print formatter %(formatter, formatter, formatter, formatter)
print formatter %(
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said good night.")

# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-qoutes.
We'll be able to type as much as we like.
Even 10 lines.
""" 

bad_dog = "\tI'm bad in."
persian_dog = "I'm split\non a line."
blackslash_dog = "I'm \\ a \\ dog."

fat_dog = """
I'll do a list.
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print bad_dog
print persian_dog
print blackslash_dog
print fat_dog
