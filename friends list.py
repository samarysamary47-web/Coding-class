print("Welcome to your friends list!")
friends = set()

while True:
    print("1. Add a friend")
    print("2. delete a friend")
    print("3. view friends")
    print("4. Exit")
    option = int(input("Enter your option (1 - 4) "))
    if option == 1:
        add = str(input("Enter the friend's name "))
        friends.add(add)
        print("{} has been added".format(add))
    elif option == 2:
        add = str(input("Enter the friend's name "))
        friends.discard(add)
        print("{} has been deleted".format(add))
    elif option == 3:
        print("your friends are:")
        for i in friends:
            print(i)
    elif option == 4:
        print("Thank you for using the friends list!")
        break
    else:
        print("please pick a number from 1 - 4")
        continue