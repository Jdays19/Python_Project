import random

def aboutMe():
    print("\nHola como estas! My name is Jocelyn and I enjoy to run and solve puzzles in my freetime.\nI mostly just lay in bed though, sigh.\n")
    menu() #returns back to menu.

def question1():
    ques = ["Favorite Holiday? Halloween","Favorite Food? Fettuccine Alfredo","Favorite Color? Lavender"]
    random.shuffle(ques)
    print()
    print(ques[random.randrange(0, len(ques))])
    menu() #could not figure out how to randomize dictionary

def guestBook():
    name1 = input("Enter your first name: ")
    name2 = input("\nEnter your last name: ")
    msg1= input("\nInclude a message: ")
    user = {"First Name":"","Last Name":"","Message":""} #created dictionary
    user.update({"First Name":name1,"Last Name":name2,"Message":msg1})
    print(user)
    menu()

def random1():
    Facts = ["Panda Express is trash, change my mind","Still waiting for GTA6 to be released...","Ketchup on scrambled eggs is a must","It is 1am and im tired"]
    random.shuffle(Facts)
    print()
    print(Facts[random.randrange(0, len(Facts))])
    menu()

def menu():
    print("\nEnter one of the following:\n")
    print("About: Learn more about me\nQ&A: Ask me a question\nGuestbook: Get added to my guestbook\nRandom: For something random!\nGoodbye: End the program.\n")
    choice=input("Enter your option: ")

    if choice == "about" or choice == "About":
        aboutMe()
    elif choice == "q&a" or choice == "Q&A":
        question1()
    elif choice == "guestbook" or choice == "Guestbook":
        guestBook()
    elif choice == "random" or choice == "Random":
        random1()
    elif choice == "goodbye" or choice == "Goodbye":
        print("\n See ya later!\n")
    else:
        print("\nPlease enter a valid option.") 
        menu()
menu()


    
 


