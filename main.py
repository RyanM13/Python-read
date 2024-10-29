import re
from rich import print

line = 0
infile = "alice-in-wonderland.txt"
fin = open(infile, encoding="utf8")
content = fin.read()


match = (re.findall('(\(.*?)\)', content))  
for word in match:
    print(word)