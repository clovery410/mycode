from sys import argv  # from module sys import argv

script, filename = argv  # assign argument variables to script and filename

txt = open(filename) # open a file, and set that returned file to variable txt

print "Here's your file %r:" % filename  # print a string with the filename you get from the argument
print txt.read()  # read the file and print it
txt.close()

print "Type the filename again:"  # print a string
file_again = raw_input("> ")  # use raw_input function to get input from user's typing, and assign the input to variable file_again, it should be a filename here

txt_again = open(file_again)  # open this file and set it to variable txt_again

print txt_again.read()  # read this file and print it
txt_again.close()
