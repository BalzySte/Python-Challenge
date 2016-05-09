import re
import urllib.request

# text found in source saved in file 3.txt

f = open("3.txt")
infile = f.read()

occurr = re.findall(r"[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]", infile)

print(occurr)

for string in occurr:
	print(string[4], end='')   	
print()
