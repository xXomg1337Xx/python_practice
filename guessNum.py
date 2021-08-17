# Guess the number game

import random
import time


def playAgain():
	while True:
				try:
					print("[-] Play again? (yes/no)")
					answer = input()
					if answer == "yes":
						print("[-] Here we go again")
						break ########### start from beginning
					elif answer == "no":
						print("[-] Goodbye")
						exit()
					else:
						print("[X] Please answer yes or no")
						continue
				except ValueError:
					print("[X] Error >>> Yes or no")




print("Hello, what is your name?")
name = input()

print("Hello {}, I'm thinking of a number between 1-10".format(name))

secretNum = random.randint(0,10)
i=0
while True:
	print("[-] Take a guess idiot")
	try:
		guess = int(input())
		if i > 5:
			print("[X] Out of time shitter \n[X] The number was {} lmaoo".format(secretNum))
			i=0
			secretNum = random.randint(0,10)
			playAgain()
			continue
		i+=1


		if guess == secretNum:
			print("[*] Wow {}... crazy, you did it in {} guesses".format(name,i))
			time.sleep(2)
			i=0
			secretNum = random.randint(0,10)
			playAgain()

		elif guess > secretNum:
			print("[X] Too high, {} guesses remaining".format(6-i))
		elif guess < secretNum:
			print("[X] Too low, {} guesses remaining".format(6-i))
	except ValueError:
		print("[X] Error >>> use numbers")
		i=i-1



print("You took {} guesses".format(i))



