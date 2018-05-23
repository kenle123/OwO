#Reads in the input.txt file and changes all r/l characters to w -> OwO
def readFile():

	#Reads in the file and converts to list since strings are immutable
	with open('input.txt') as f:
		read_data = f.read()
		text = list(read_data)

	#Goes through entire list and changes r/l to w
	for i in range(len(text)):
		if(text[i] == 'l' or text[i] == 'r'):
			text[i] = 'w'

	#Changes modified list to string type
	str = ''.join(text)
	f.close()

	return str

#Write the modified text to a file
def writeFile(str1):
	with open('output.txt', 'w') as f:
		f.write(str1)

def readFromUserInput():
	beforeText = input('Enter text to be OwO: ')
	text = list(beforeText)

	for i in range(len(text)):
		if(text[i] == 'l' or text[i] == 'r'):
			text[i] = 'w'

	#Changes modified list to string type
	str = ''.join(text)
	print(str)


#Main Function
def main():
	#readFromUserInput()
	updatedTxt = readFile()
	writeFile(updatedTxt)


if __name__ == "__main__":
	main()
