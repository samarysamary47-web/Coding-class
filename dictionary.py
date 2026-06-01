countrydict = {
    "England":"London",
    "Russia":"Moscow",
    "Spain":"Madrid"
}
print(countrydict.keys())
while True:
    print("\nMini Dictionary App")

    print("1. Add/Update a country")

    print("2. Retrieve a country's capital")

    print("3. Delete")

    print("4. View all countries")

    print("5. Exit")

    option = input("What number do you pick?(1-5)")
    if option == "1":
        country = input("What country?")
        capital = (input("What is the capital city?"))
        countrydict[country] = capital
    elif option == "2":
        country = input("What country?")
        if country in countrydict.keys():
            countrydict[country] = input("What capital?")
        else:
          print("{} wasn't found in the dictionary.".format(country))
    elif option == "3":
        delete = input("What  country do you want to delete?")
        del countrydict[delete]
        print("{} has been deleted".format(delete))
    elif option == "4":
        print(countrydict)
    elif option == "5":
        print("Thank you for using this app!")
        break
    else:
        print("Please pick a number from 1-5.")