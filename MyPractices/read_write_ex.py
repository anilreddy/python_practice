# Reading and Writing Files

from sys import argv

script, filename = argv

print "We are going to erase %r file" %filename
print "If you Don't want that, hit CTRL + C"
print "If you do want that, hit ENTER"

raw_input('?')

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
#target.write("\n")

print "Finally we close it!"

target.close()
