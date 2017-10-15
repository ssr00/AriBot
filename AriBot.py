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


def typing(type_sleep, type_wait=2):
    sleep(type_wait)
    print("\nTyping ...\n")
    sleep(type_sleep)


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
        global gender
        gender = question_renderer("What's your gender? Type 'male' or 'female'.")
        # print("What's your gender? Type 'male' or 'female'.")
        if gender != 'male' and gender != 'female':
            continue
        else:
            break
    return gender


def get_name():
    while True:
        global name
        name = question_renderer("What's your name?")
        name = name.lower().capitalize()
        if name == '':
            continue
        elif name.isdigit():
            typing(1)
            print("Please don't type numbers.")
        else:
            typing(1)
            print(choice(("I like your name.", "I always wanted to have that name.", "My friend has the same name.")))
            break


def get_age():
    while True:
        try:
            age = int(question_renderer("How old are you, {}?".format(name)))
        except ValueError:
            typing(1)
            print("Please, just type numbers.")
        else:
            if int(age) <= 25:
                typing(2)
                print(choice(("You're still young.", "Being young is very good.", "Enjoy your youth.")))
            elif int(age) > 25:
                typing(1)
                print(choice(("You're getting old already.", "I hope you have enjoyed your teenage years.", "More bills to pay than friends.")))
            break


def get_hobby():
    while True:
        hobby = question_renderer('What is your hobby?')
        if hobby == "":
            continue
        else:
            typing(1)
            print(choice(("I've always wanted to learn that.", "I tried to do it once but I did not like it.", "I like that too!")))
            break


def get_city():
    while True:
        global city
        city = question_renderer("What city do you live, {}?".format(name))
        if city == '':
            typing(1)
            print("Please type the name of your city.")
            continue
        else:
            city_opinion = question_renderer("Do you like to live there?\nType 'yes' or 'no': ", type_count=3)
            if city_opinion.lower() == 'yes':
                typing(1)
                print(choice(("My friends live there and they like this city very much.", "Home sweet home.", "I really want to go there.")))
                break
            elif city_opinion.lower() == 'no':
                typing(1)
                print(choice(("It's never too late to change!", "A lot of people do not really like this city.", "There are much better places out there.")))
                break


def get_relationship():
    if gender == 'male':
        while True:
            relationship = question_renderer("So {}, are you dating, married or single?".format(name))
            if relationship.lower() == 'dating':
                girlfriend = question_renderer("What's her name?")
                typing(1)
                print(choice(("I will pray for you, ", "You're a lucky woman, ", "Not everything is perfect, ")) + girlfriend.lower().capitalize() + ".")
                break
            elif relationship.lower() == 'single':
                typing(1)
                print(choice(("Try to be cool sometimes with people too.", "Best thing in life.", "One day you find someone, you're so cool.")))
                break
            elif relationship.lower() == 'married':
                wife = question_renderer("What's her name?")
                typing(1)
                print(choice(("I will pray for you, ", "You're a lucky woman, ", "Not everything is perfect, ")) + wife.lower().capitalize() + ".")
                break
            else:
                continue

    elif gender == 'female':
        while True:
            relationship = question_renderer("So, {}, are you dating, married or single?".format(name))
            if relationship.lower() == 'dating':
                boyfriend = question_renderer("What's his name?")
                typing(1)
                print(choice(("I will pray for you, ", "You're a lucky man, ", "Not everything is perfect, ")) + boyfriend.lower().capitalize() + ".")
                break
            elif relationship.lower() == 'single':
                typing(1)
                print(choice(("Try to be cool sometimes with people too.", "Best thing in life.", "One day you find someone, you're so cool.")))
                break
            elif relationship.lower() == 'married':
                typing(2)
                print("What's his name?")
                husband = input("~ ")
                typing(2)
                print(choice(("I will pray for you, ", "You're a lucky man, ", "Not everything is perfect, ")) + husband.lower().capitalize() + ".")
                break
            else:
                typing(2)
                print("Please answer the question.")
                continue


def get_pet():
    while True:
        pet = question_renderer('Do you have pets?')
        if pet == '':
            continue
        elif pet.lower() == 'yes':
            pet_name = question_renderer("What's his name?")
            typing(2)
            print(choice(("I love this name.", "My pet have the same name.", "I'll put that name on my new pet.")))
            break
        elif pet.lower() == 'no':
            typing(2)
            print(choice(("You should have one.", "They make a lot of mess.", "Everyone should have one at least once.")))
            break


def get_band():   
    while True:
        band = question_renderer("What band or artist are you listening to?")
        if band == '':
            continue
        else:
            typing(3)
            print(choice(("I like too, once I went to a show in New York and it was really good. I have all the albums.", "I do not like it very much.", "I listened these days and I liked it a lot.")))
            break


def get_movie():
    while True:
        filme = question_renderer("What's your favorite movie?")
        if filme == '':
            continue
        else:
            typing(3)
            print(choice(("I love this movie! There are some things that I would change, but in general it's amazing.", "It's not my favorite movie.", "I loved the end of the movie.","I've watched this movie 5 times.")))
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


def question_renderer(question, user_input='~ ', type_count=2):
    while True:
        typing(type_count)
        print(question)
        answer = input(user_input)
        return answer

if __name__ == "__main__":
    talk()
