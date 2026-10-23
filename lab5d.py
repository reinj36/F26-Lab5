# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Reina James
# Date: 23/10/2026
# Purpose: Process File data.
# Usage: ./lab5d.py

# TO DO 1: Copy the files pythonStatements.txt and machineCode.txt in folder.
# TO DO 2: Follow the instructions from the readme.me file to create the exact output.

#open files
code = open("machineCode.txt", "r")
statements = open("pythonStatements.txt", "r")
outfile = open("output.txt", "w")

#read first line of both scripts
codeLine = code.readline()
statementLine = statements.readline()

while codeLine != "" and statementLine != "":

    statementLine = statementLine.lstrip()
    statementLine = statementLine.strip("#\n")

    outfile.write(statementLine + "\t" + codeLine)

    codeLine = code.readline()
    statementLine = statements.readline()


#close files
code.close()
statements.close()
outfile.close()

#Not sure how to remove the comments using strip()?