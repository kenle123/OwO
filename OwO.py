#Reads in the input.txt file
def readFile():
	with open('input.txt') as f:
		read_data = f.read()
	f.close()
	return read_data

#Write the modified text to output.txt
def writeFile(str):
	with open('output.txt', 'w') as f:
		f.write(str)
	f.close()

#Read in user input and prints to console the OwO version
def readFromUserInput():
	userInput = input('Enter text to be OwO: ')
	return userInput

#Converts string parameter into a list and changes all r/l to w -> OwO
def convertToOwO(beforeText):
	text = list(beforeText)

	for i in range(len(text)):
		if(text[i] == 'l' or text[i] == 'r'):
			text[i] = 'w'

		if(text[i] == 'L' or text[i] == 'R'):
			text[i] = 'W'

	#Changes modified list back to string
	OwoText = ''.join(text)

	return OwoText

#Prints resulting OwO
def printOwO(string):
	print(string)

#Main Function
def main():
	flag = True

	while(flag):
		print()
		print("-----------------------------------");
		print("|    Welcome to the OwO Machine   |");
		print("|                                 |");
		print("|   1. Read From File and Write   |");
		print("|   2. Read From User Input       |");
		print("|   3. Exit                       |");
		print("-----------------------------------");

		#Get user input for their menu choice
		menuChoice = int(input("Enter your choice(1,2, or 3): "))

		#User decides to read/write to a file
		if(menuChoice == 1):
			baseTxt = readFile()
			OwOTextRead = convertToOwO(baseTxt)
			writeFile(OwOTextRead)

			print("Successfully Wrote to File")

		#User decides to use user input
		elif(menuChoice == 2):
			userInput = readFromUserInput()
			OwOTextInput = convertToOwO(userInput)
			printOwO(OwOTextInput)

		#User exits program
		else:
			flag = False

if __name__ == "__main__":
	main()
