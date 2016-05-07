from string import ascii_letters

# Text found in page source is in file 2.txt
f = open("2.txt")
text = f.read()

output = ""

for char in text:
	if char in ascii_letters:
		output += char
	
print(output)
