dictionary = {}

while True:
    print("\nDictionary Management System")
    print("1. Add a Word")
    print("2. Search for Meaning")
    print("3. Display all words")
    print("4. Update Meaning")
    print("5. Delete a Word")
    print("6. Exit")

    Choice  = input("Enter your choice: ")

    if Choice == "1":
        word= input("enter the word: ").lower() #coverts the input into lower case
        meaning = input("Enter the meaning: ")
        dictionary[word] = meaning
        print("Word added Successfully")
    elif Choice == "2":
        word= input("enter the word: ").lower()
        if word in dictionary:
            print("Meaning:", dictionary[word])
        else:
            print("word not found in dictionary.")

    if Choice == "3":
         
         if dictionary:
            print("\n Words in the dictionary are :")
            for word in dictionary:
                print(word)
         else:
            print("No word found")
    if Choice == "4":
        word =input("Enter the word to change the meaning :")
        if word in dictionary:
            new_meaning = input("Enter the New Meaning :")
            dictionary[word]=new_meaning
            print("Meaning has changed succesfully")
        else:
            print("No meaning found for the word")
    if Choice=="5":
        word=input("Enter the word to delete :")
        if word in dictionary:
            del dictionary[word]
            print("Word has been delted Succesfully")
        else:
            print("Word has not been found")
    if Choice=="6":
        break
    else:
        print("invalid choice") #if the input is not from 1 to 6

    




                


