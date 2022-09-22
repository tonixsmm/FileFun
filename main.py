#FILES
#a file stores data on your file system
#"on disk"

#Goal: read the content of data.csv into our python program memory. Eventually, store the content in a 2D list

#3-part file processing format template
#1. open the file
#2. process the file (e.g. read or write or sth else)
#3. close the file

#let use the function for practice
from fileinput import filename


def load_line_from_file(filemame):
    #filename is a string representing a path to file we want to work on
    #1. abosolute path: start with a drive in general
    #example: /Users/tony/Documents/Python Coding/CPSC222/FileFun
    #2. relative path: don't start with a drive, relative to the current working directory
    #use "pwd" with terminal
    infile = open(filename, "r") #r is the file read mode
    lines = infile.readlines()
    infile.close()
    return lines

def clean_lines(lines):
    for i in range(len(lines)):
        #lines[i] is a string
        lines[i] = lines[i].strip()

file_lines = load_line_from_file("data.csv") #relative path: in the same directory
print(file_lines)
