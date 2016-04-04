#Password Cracker test program
#Program written by Zach Hofmeister, ported to Python
#READ THE README BEFORE USING ANY OF MY CODE!!!

#imports the python function to get the local time
import time

#Below variable saves the password entered by the user. Only compared to a complete password to simulate brute-force cracking.
userPassword = raw_input("Enter a 4 digit password for the computer to guess. All letters/numbers/special characters are supported.") + ""

#The following variable contains an array of all the possible characters that can be present.
possibleCharacters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
'X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
'w','x','y','z','1','2','3','4','5','6','7','8','9','0',' ',',','.','?','!','/','\\','[',']','{','}',
'|','<','>',';',':','+','=','-','_','(',')','@','#','$','%','^','&','*','~','`']

#The default computer guess.
computerGuess = 'AAAA'

records when the function starts
starttime = time.time()

#Establishes that the computer has not correctly guessed the password, will be changed when password is discovered.
correctGuess = False

#The following variable keeps track of how many guesses it takes for the computer to crack the password.
totalGuesses = 0

#The following variable keeps track of what character is currently being tested.
i = [0,0,0,0,0,0,0,0,0,0]

#Function that compares the current guess to the user input. Notice that the password isn't guessed letter by letter, the whole 4 character guess is generated.
def checkPassword(passwordGuess):
	global userPassword
	if (passwordGuess == userPassword):
		global computerGuess
		global totalGuesses
		global starttime
		print "Your password is " + computerGuess + "."
		print "Took " + str(time.time() - starttime) + " seconds and " + str(totalGuesses) + " tries to guess your password."
	else:
		print "Guessing Again... " + str(totalGuesses) + " so far, currently " + str(computerGuess)

#Function that creates the current guess and compares it to the actual password.
def charGuess(charNumberDigit):
	global computerGuess
	global possibleCharacters
	global totalGuesses
	computerGuess = computerGuess[0:charNumberDigit - 1] + possibleCharacters[i[charNumberDigit - 1]] + computerGuess[charNumberDigit:]
	checkPassword(computerGuess)
	if (charNumberDigit != 4):
		i[charNumberDigit] = 0
	i[charNumberDigit - 1] += 1
	totalGuesses += 1

#The loop that tells the computer to try a guess
while (computerGuess != userPassword):
	while (i[3] <= 92 and computerGuess != userPassword):
		charGuess(4)
		while (i[2] <= 92 and i[3] == 92 and computerGuess != userPassword):
			charGuess(3)
			while (i[1] <= 92 and i[2] == 92 and computerGuess != userPassword):
				charGuess(2)
				while (i[0] <= 92 and i[1] == 92 and computerGuess != userPassword):
					charGuess(1)
