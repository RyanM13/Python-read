# Ryan Mathews
# CMPS 4143 Cont-Prog
# Tina Johnson
# 10/30/2024
# This program takes a the text file alice-in-wonderland.txt and finds all the parenthesis in it. 
# It than sorts it in alphabetical order and than counts each word in each line as well as prints it. 


# Used for regular expresions 
import re
# Makes output more readable and look better, can comment out if not installed.
from rich import print  

# Storing it in a varible for readability 
infile = "alice-in-wonderland.txt"
line = 0

# Opening the file, also using utf8 because of some weird characters in the file
fin = open(infile, encoding="utf8")

# Reading the file into the variable content 
content = fin.read()

# Grabing the lines that are in parenthesis
match = (re.findall('\((.*?)\)', content))  

# Sorting the match in alphabetical order, using lower for precedence 
match = sorted(match, key=lambda word: word.lower())

# Looping through match to print and than split that line to grab word count
for i in range(len(match)):
    print(match[i], len(match[i].split()))
    line+= 1

# Does whitespace count?
print(line)
# Closing file, I was curious as to why we actually have to close the file in python so I looked it up and found this forum: 
# https://stackoverflow.com/questions/25070854/why-should-i-close-files-in-python. I thought it was pretty interesting what othe people thought.
fin.close()




