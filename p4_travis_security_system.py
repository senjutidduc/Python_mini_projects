known_users= ["Alice","Bob","Claire","Dan","Emma","Fred","Georgia","Harry"]

print(known_users)
print("Number of known users: "+str(len(known_users)))

while True:
    print("Hi! My name is Travis!")
    name=input("What is your name?: ").strip().capitalize()
    
    if name in known_users:
        output="Hello {}!".format(name)
        print(output)
        remove=input("Would you like to be removed from the system(y/n)?: ").strip().lower()
        if remove == "y":
            known_users.remove(name)
            print(known_users)
        elif remove == "n":
            print("No problem! I didn't want you to leave anyway!")
    else:
        print(("Hmmm I don't think I have met you yet {}").format(name))
        add_me = input("Would you like to be added in the system(y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
            print(known_users)
        elif add_me == "n":
            print("No worries! See you around!")
