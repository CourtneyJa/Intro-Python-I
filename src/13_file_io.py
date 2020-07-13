"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

f = open('foo.txt', 'r')
doc = f.read()
f.close()
print(doc)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

f2 = open('bar.txt', 'w')
f2.write("Test Line 1 \nTest Line 2 \nTest Line 3")
f2.close()

f2 = open('bar.txt', 'r')
f2_doc = f2.read()
f2.close()
print(f2_doc)