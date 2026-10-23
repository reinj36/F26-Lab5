# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Reina James
# Date: 23/10/2026
# Purpose: Process File data.
# Usage: ./lab5c.py

# TO DO 1: Run the code provided in readme.md file.

with open("rhyme.txt", "w") as dataFile :
  dataFile.write("I made myself a snowball\nAs perfect as could be.\nI thought I'd keep it as a pet\nAnd let it sleep with me.")

# TO DO 2: Open rhyme.txt file.
# TO DO 3: Print the output as directed in readme.md file.

with open("rhyme.txt", "r") as infile:

  #read first line
  line = infile.readline()

  while line != "":

    #strip white spaces and . from each line
    line =line.strip()
    line = line.strip(".")

    #print line and number of words in line
    print(line, " --- ", len(line.split()), " words")

    #read next line
    line = infile.readline()


