print("Welcome to Volta.")

name = input("What is your name? ")

print("Hi " + name + ". It's nice to meet you.")
print("I haven't seen you before. Is this your first time coming to Volta?")

choice = input("1) Yes. It's My first time. 2) No, I have been many times before: ")

if choice == "1":
	print("Oh. A tourist! You are going to have a lot of fun!")
elif choice == "2":
	print("Ok. A return visitor. I wonder why I have never seen you before")
else:
	print("Sorry. I do not understand")
	print("Game over. Want to play again?")