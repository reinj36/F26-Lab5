# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Reina James
# Date: 23/10/2026
# Purpose: Read a text file.
# Usage: ./lab5a.py

# TO DO 1: Create data2.txt.
# TO DO 2: Complete the functions below.

def read_file_lineByLine(file_name):
    # Takes file_name as a string, reads the file in a loop one line at a time and prints each line.
    with open("data2.txt", "r") as infile:

        #read first line and assign to line
        line = infile.read() #doing readline() adds an empty line after, but just read() doesn't

        #print each line of data2.txt
        while line != "":
            print(line)
            line = infile.read()

def read_file_list(file_name):
    # Takes a file_name as string, read file line by line and add the line in a list as a list element without new-line characters
    # Return the list.

    #create list
    lines = []

    with open("data2.txt", "r") as infile:
        #read first line
        infile = open("data2.txt", "r")
        line = infile.readline()

        #add each line of data2.txt to lines list
        while line != "":
            lines.append(line.rstrip("\n"))
            line = infile.readline()

        return lines

def main():
    file_name = 'data2.txt'
    read_file_lineByLine(file_name)
    print(read_file_list(file_name))

if __name__ == "__main__":
    main()
