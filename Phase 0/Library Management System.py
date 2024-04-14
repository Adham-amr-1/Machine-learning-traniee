# Library of BookClass
from BookClass import book as bk
# Library Decleration 
library = bk.load_from_file()
# -----------------------------------------------------------------------
# Program Code
while True:
    #-----------------------------------------------------------
    #Print User Interface Screen
    bk.printscreen()
    #-----------------------------------------------------------
    while True:
        try : #Checking if input is integer
            choice = int(input("Enter Your Choice : "))
            break
        except:
            print("Invalid Input ( Enter Integer Number )")
    #-----------------------------------------------------------
    if choice == 1:# Adding New Book
    #-----------------------------------------------------------
        while True :
                try: #Checking if input is integer or not
                    id = int(input("Book ID : "))
                    break
                except:
                    print("That's Not ID ( Enter An Integer Number )")
        if bk.checks(id, library):
            print("Book Exist In library")
            case = input("Do You Want to Update It's Data ( Y / N ) ? : ")
            if case == 'Y' or case == 'y':
                place = bk.index(id, library)
                bk.update_book(place, library,id)
            elif case == 'N' or case == 'n':
                pass
            else:
                print("------------------------------")
                print("Not Exist Choice")
                print("Default : Back to Main Screen ")
                print("------------------------------")
        else:
            bk.add_book(id,library)
    #-----------------------------------------------------------
    elif choice == 2: # Delete specific book
    #-----------------------------------------------------------
        if len(library):
            bk.delete_book(library)
        else:
            print("")
            print("There's No Book Exist in Library to remove")
            print("------------------------------------------")
    #-----------------------------------------------------------
    elif choice == 3: # Update Specific Book
    #-----------------------------------------------------------
        if len(library):
            while True :
                try: #Checking if input is integer or not
                    id = int(input("Book ID : "))
                    break
                except:
                    print("That's Not ID ( Enter An Integer Number )")
            if bk.checks(id,library):
                place = bk.index(id,library)
                bk.update_book(place,library,id)
            else:
                print("")
                print("-------------------")
                print("Book does not exist")
                print("-------------------")
        else:
            print("")
            print("There's No Book Exist in Library to update it")
            print("---------------------------------------------")
    #-----------------------------------------------------------
    elif choice == 4: # Check If Book Exists
    #-----------------------------------------------------------
        if len(library):
            while True :
                try: #Checking if input is integer or not
                    id = int(input("Book ID : "))
                    break
                except:
                    print("That's Not ID ( Enter An Integer Number )")
            bk.check_book(id,library)
        else:
            print("")
            print("There's No Book Exist in Library")
            print("--------------------------------")
    #-----------------------------------------------------------
    elif choice == 5: # Printing All Library Books
    #-----------------------------------------------------------
        if len(library):
            bk.view_all(library)
        else:
            print("")
            print("There's No Book Exist in Library to Display")   
            print("-------------------------------------------")
    #-----------------------------------------------------------
    elif choice == 6: # Exit The System
    #-----------------------------------------------------------
        print("--------------------")
        print("Saving Data.....")
        bk.save_to_file(library)
        bk.save_to_excel(library)
        print("Saved Successfully")
        bk.exit()
        break
    #-----------------------------------------------------------
    else: #If Input Is More Than 6
        print("Invalid Choice")
# -----------------------------------------------------------------------