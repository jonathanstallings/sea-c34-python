import io

# Question 1: can I use this for my bot text?
# f = io.open('bletchley.txt', encoding='utf-8')
# my_data = f.read()
# f.close()
# print my_data

# nope, I get an error 'UnicodeDecodeError: 'utf8' codec can't decode
# byte 0xe9 in position 39020: invalid continuation byte'

# f = io.open('bletchley.txt')
# my_data = f.read()
# f.close()
# print my_data

# nope, that doesn't work either.


f = io.open('bletchley.txt', 'rb')
secret_data = f.read()
f.close()
print secret_data

# that works! and this reads everything as a string, so if I put:

print secret_data[0]

# it will print the zero-th character, not word.

# Question 2: can I open the file, print a line, and then re-write the file
# with that line deleted? (I need this for a twitter bot...)

f = io.open('bletchley.txt', 'rb')
secret_data = f.readlines()
f.close()
print secret_data[0]
numlines = len(secret_data)
print type(secret_data)
# this code above prints one line at a time... a good start. let's see if we
# can now write everything else to a new file, effectively deleting that line

outfile = io.open('bletchley.txt', 'w')
for i in secret_data[1:]:
    outfile.write(unicode(i))

# it works!
