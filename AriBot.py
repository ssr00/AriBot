from time import sleep
from random import choice

user_profile = {}


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
        gender = question_renderer("What's your gender? Type 'male' or 'female'.")
        user_profile['gender'] = gender
        if gender != 'male' and gender != 'female':
            continue
        else:
            break
    return gender


def get_name():
    while True:
        name = question_renderer("What's your name?")
        name = name.lower().capitalize()
        if name == '':
            continue
        elif name.isdigit():
            typing(1)
            print("Please don't type numbers.")
        else:
            user_profile['name'] = name
            list = ["I like your name.", "I always wanted to have that name.", "My friend has the same name."]
            typing(1)
            print(choice(list))
            break


def get_age():
    while True:
        try:
            age = int(question_renderer("How old are you, {}?".format(user_profile['name'])))
        except ValueError:
            typing(1)
            print("Please, just type numbers.")
        else:
            if int(age) <= 25:
                typing(2)
                list = ["You're still young.", "Being young is very good.", "Enjoy your youth."]
                print(choice(list))
            elif int(age) > 25:
                typing(1)
                list = ["You're getting old already.", "I hope you have enjoyed your teenage years.", "More bills to pay than friends."]
                print(choice(list))
            break


def get_hobby():
    while True:
        hobby = question_renderer('What is your hobby?')
        if hobby == "":
            continue
        else:
            typing(1)
            list = ["I've always wanted to learn that.", "I tried to do it once but I did not like it.", "I like that too!"]
            print(choice(list))
            break


def get_city():
    while True:
        city = question_renderer("What city do you live, {}?".format(user_profile['name']))
        if city == '':
            typing(1)
            print("Please type the name of your city.")
            continue
        else:
            user_profile['city'] = city
            city_opinion = question_renderer("Do you like to live there?\nType 'yes' or 'no': ", type_count=3)
            if city_opinion.lower() == 'yes':
                typing(1)
                list = ["My friends live there and they like this city very much.", "Home sweet home.", "I really want to go there."]
                print(choice(list))
                break
            elif city_opinion.lower() == 'no':
                typing(1)
                list = ["It's never too late to change!", "A lot of people do not really like this city.", "There are much better places out there."]
                print(choice(list))
                break


def get_relationship():
    if user_profile['gender'] == 'male':
        while True:
            relationship = question_renderer("So {}, are you dating, married or single?".format(user_profile['name']))
            if relationship.lower() == 'dating':
                girlfriend = question_renderer("What's her name?")
                typing(1)
                list = ["I will pray for you, ", "You're a lucky woman, ", "Not everything is perfect, "]
                print(choice(list) + girlfriend.lower().capitalize() + ".")
                break
            elif relationship.lower() == 'single':
                typing(1)
                list = ["Try to be cool sometimes with people too.", "Best thing in life.", "One day you find someone, you're so cool."]
                print(choice(list))
                break
            elif relationship.lower() == 'married':
                wife = question_renderer("What's her name?")
                typing(1)
                list = ["I will pray for you, ", "You're a lucky woman, ", "Not everything is perfect, "]
                print(choice(list) + wife.lower().capitalize() + ".")
                break
            else:
                continue

    elif user_profile['gender'] == 'female':
        while True:
            relationship = question_renderer("So, {}, are you dating, married or single?".format(user_profile['name']))
            if relationship.lower() == 'dating':
                boyfriend = question_renderer("What's his name?")
                typing(1)
                list = ["I will pray for you, ", "You're a lucky man, ", "Not everything is perfect, "]
                print(choice(list) + boyfriend.lower().capitalize() + ".")
                break
            elif relationship.lower() == 'single':
                typing(1)
                list = ["Try to be cool sometimes with people too.", "Best thing in life.", "One day you find someone, you're so cool."]
                print(choice(list))
                break
            elif relationship.lower() == 'married':
                typing(2)
                print("What's his name?")
                husband = input("~ ")
                typing(2)
                list = ["I will pray for you, ", "You're a lucky man, ", "Not everything is perfect, "]
                print(choice(list) + husband.lower().capitalize() + ".")
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
            list = [ "I love this name.", "My pet have the same name.", "I'll put that name on my new pet."]
            typing(2)
            print(choice(list))
            break
        elif pet.lower() == 'no':
            list = [ "You should have one.", "They make a lot of mess.", "Everyone should have one at least once."]
            typing(2)
            print(choice(list))
            break


def get_band():   
    while True:
        band = question_renderer("What band or artist are you listening to?")
        if band == '':
            continue
        else:
            typing(3)
            list = ["I like too, once I went to a show in New York and it was really good. I have all the albums.", "I do not like it very much.", "I listened these days and I liked it a lot."]
            print(choice(list))
            break


def get_movie():
    while True:
        filme = question_renderer("What's your favorite movie?")
        if filme == '':
            continue
        else:
            typing(3)
            list = ["I love this movie! There are some things that I would change, but in general it's amazing.", "It's not my favorite movie.", "I loved the end of the movie.","I've watched this movie 5 times."]
            print(choice(list))
            break


def get_opinion():
    typing(4)
    print("So {}, like I said, I'm still in alpha and I know I can be better.".format(user_profile['name']))
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
