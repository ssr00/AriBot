from time import sleep
from random import choice

def talk():
	
	welcome()

	get_gender()

	get_name()

	get_age()

	get_hobby()

	get_city()

	get_relationship()

	get_pet()

	get_band()

	get_movie()

	get_opinion()

	finish()

def typing(x):

	sleep(2)
	print("\nTyping ...\n")
	sleep(x)

def welcome():

	asterisk = '*'
	print(asterisk*58)
	print("* Hi, my name is Ari!                                    *\n")
	print("* I'd like to talk with you a little.                    *\n")
	print("* I`m still in alpha so I`m not really very smart.       *")
	print(asterisk*58)

	input("\nPress ENTER to start ")

def get_gender():
	
	while True:

		typing(3)
		print("What's your gender? Type 'male' or 'female'.")
		global gender
		gender = input("~ ")

		if gender != 'male' and gender != 'female':
			continue

		else:
			break

	return gender


def get_name():

	while True:

		typing(2)
		print("What's your name?")
		global name
		name = str(input("~ "))
		name = name.lower().capitalize()

		if name == '':
			continue

		elif name.isdigit():
			typing(2)
			print("Please don't type numbers.")

		else: 
			list = [ "I like your name.", "I always wanted to have that name.", "My friend has the same name."
			]
			typing(2)
			print(choice(list))
			break

def get_age():
	
	while True:

		try:
			typing(2)
			print("How old are you, {}?".format(name))
			age = int(input("~ "))

		except ValueError:
			typing(2)
			print("Please, just type numbers.")

		else:
			if age <= 25:
				typing(2)
				list = ["You're still young.", "Being young is very good.", "Enjoy your youth."
				]
				print(choice(list))

			elif age > 25:
				typing(2)
				list = ["You're getting old already.", "I hope you have enjoyed your teenage years.", "More bills to pay than friends."
				]
				print(choice(list))
			break

def get_hobby():

	while True:

		typing(2)
		print("What is your hobby?")
		hobby = str(input("~ "))

		if hobby == "":
			continue

		else:
			typing(2)
			list = ["I've always wanted to learn that.", "I tried to do it once but I did not like it.", "I like that too!"
			]
			print(choice(list))
			break

def get_city():

	while True:

		typing(2)
		print("What city do you live, {}?".format(name))
		global city
		city = input("~ ")

		if city == '':
			typing(2)
			print("Please type the name of your city.")
			continue

		else:
			typing(3)
			city_opinion = input("Do you like to live there?\nType 'yes' or 'no': ")

			if city_opinion.lower() == 'yes':

				typing(2)
				list = ["My friends live there and they like this city very much.", "Home sweet home.", "I really want to go there."
				]
				print(choice(list))
				break

			elif city_opinion.lower() == 'no':

				typing(2)
				list = ["It's never too late to change!", "A lot of people do not really like this city.", "There are much better places out there."
				]
				print(choice(list))
				break

def get_relationship():
	
	if gender == 'male':
		while True:

			typing(2)
			print("So {}, are you dating, married or single?".format(name))
			relationship = input("~ ")

			if relationship.lower() == 'dating':

				typing(2)
				print("What's her name?")
				girlfriend = input("~ ")

				typing(2)
				list = ["I will pray for you, ", "You're a lucky woman, ", "Not everything is perfect, "
				]
				print(choice(list) + girlfriend.lower().capitalize() + ".")
				break

			elif relationship.lower() == 'single':

				typing(2)
				list = ["Try to be cool sometimes with people too.", "Best thing in life.", "One day you find someone, you're so cool."
				]
				print(choice(list))
				break

			elif relationship.lower() == 'married':

				typing(2)
				print("What's her name?")
				wife = input("~ ")

				typing(2)
				list = ["I will pray for you, ", "You're a lucky woman, ", "Not everything is perfect, "
				]
				print(choice(list) + wife.lower().capitalize() + ".")
				break

			else:
				continue

	elif gender == 'female':

		while True:

			typing(2)
			print("So, {}, are you dating, married or single?".format(name))
			relationship = input("~ ")

			if relationship.lower() == 'dating':

				typing(2)
				print("What's his name?")
				boyfriend = input("~ ")

				typing(2)
				list = ["I will pray for you, ", "You're a lucky man, ", "Not everything is perfect, "
				]
				print(choice(list) + boyfriend.lower().capitalize() + ".")
				break

			elif relationship.lower() == 'single':

				typing(2)
				list = ["Try to be cool sometimes with people too.", "Best thing in life.", "One day you find someone, you're so cool."
				]
				print(choice(list))
				break

			elif relationship.lower() == 'married':

				typing(2)
				print("What's his name?")
				husband = input("~ ")

				typing(2)
				list = ["I will pray for you, ", "You're a lucky man, ", "Not everything is perfect, "
				]
				print(choice(list) + husband.lower().capitalize() + ".")
				break

			else:
				typing(2)
				print("Please answer the question.")
				continue

def get_pet():

	while True:

		typing(2)
		print("Do you have pets?")
		pet = str(input("Type 'yes' or 'no': "))

		if pet == '':
			continue

		elif pet.lower() == 'yes':

			typing(2)
			print("What's his name?")
			name_pet = input("~ ")
			list = [ "I love this name.", "My pet have the same name.", "I'll put that name on my new pet."
			]
			typing(2)
			print(choice(list))
			break

		elif pet.lower() == 'no':

			list = [ "You should have one.", "They make a lot of mess.", "Everyone should have one at least once."
			]
			typing(2)
			print(choice(list))
			break

def get_band():
	
	while True:

		typing(2)
		print("What band or artist are you listening to?")

		band = input("~ ")

		if band == '':
			continue

		else:
			typing(3)
			list = ["I like too, once I went to a show in New York and it was really good. I have all the albums.", "I do not like it very much.", "I listened these days and I liked it a lot."
			]
			print(choice(list))
			break

def get_movie():
	
	while True:

		typing(2)
		print("What's your favorite movie?")
		filme = input("~ ")

		if filme == '':
			continue

		else:
			typing(3)
			list = ["I love this movie! There are some things that I would change, but in general it's amazing.", "It's not my favorite movie.", "I loved the end of the movie.", 	"I've watched this movie 5 times."
			]
			print(choice(list))
			break

def get_opinion():

	typing(4)
	print("So {}, like I said, I'm still in alpha and I know I can be better.".format(name))

	typing(3)
	print("I'd like to know what you're thinking about me.")

	typing(3)
	input("Type here some critic or complains: ")

	typing(4)
	print("Thank you so much, I hope to get better in my next version!")

def finish():

	typing(2)
	input("Press any key to finish ... ")

if __name__ == "__main__":
    talk()
