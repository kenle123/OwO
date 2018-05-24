#Reads in the input.txt file
def readFile():

	#Reads in the file
	with open('input.txt') as f:
		read_data = f.read()
	f.close()
	return read_data

#Write the modified text to a file
def writeFile(str):
	with open('output.txt', 'w') as f:
		f.write(str)
	f.close()

#Read in user input and prints to console the OwO version
def readFromUserInput():
	userInput = input('Enter text to be OwO: ')
	return userInput

#Converts a string into a list and changes all r/l to w -> OwO
def convertToOwO(beforeText):
	text = list(beforeText)

	for i in range(len(text)):
		if(text[i] == 'l' or text[i] == 'r'):
			text[i] = 'w'

	#Changes modified list back to string
	str = ''.join(text)

	return str

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

		menuChoice = int(input("Enter your choice(1,2, or 3): "))

		if(menuChoice == 1):
			BaseTxt = readFile()
			OwOTextRead = convertToOwO(BaseTxt)
			writeFile(OwOTextRead)

			print("Successfully Wrote to File")

		elif(menuChoice == 2):
			UserInput = readFromUserInput()
			OwOTextInput = convertToOwO(UserInput)
			printOwO(OwOTextInput)

		else:
			flag = False

if __name__ == "__main__":
	main()
