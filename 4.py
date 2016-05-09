import urllib.request
import re

counter = 1
nothingNum = 12345
numList = []

# Function for parsing pages until something strange is found
def parsePages():
	global counter, nothingNum, numList
	while True:
		page = urllib.request.urlopen("http://www.pythonchallenge.com"
			"/pc/def/linkedlist.php?nothing=" + str(nothingNum))
		pageContent = page.read().decode()
		counter += 1
		print(pageContent)
		
		if re.match(r"and the next nothing is", pageContent):
			nothingNum = int(pageContent.rsplit(' ', 1)[1])
			numList.append(nothingNum)
		else:
			break


# Parsing first pages
parsePages()
print("Yes, we have to keep parsing pages...")


# Keep parsing
nothingNum = 94485
parsePages()
print("Dividing by two and going on...")


# Dividing nothingNum by 2 as requested
nothingNum /= 2
parsePages()
print("There is a mistake in following numbers")
print("Requesting next page and then replacing number with 63579")


# Requesting next page and setting nothingNum to 63579
page = urllib.request.urlopen("http://www.pythonchallenge.com"
		"/pc/def/linkedlist.php?nothing=" + str(nothingNum))
counter += 1
nothingNum = 63579
parsePages()

print()
print("Parsed pages: " + str(counter))
