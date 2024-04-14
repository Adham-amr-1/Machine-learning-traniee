from prettytable import PrettyTable
# -----------------------------------------------------------------------
# Structure For Books ( New Data Type To Deal With Book Data)
class book:
    books = 0
    def __init__(self, id, book_name, author_name, copies):
        self.id = id
        self.book_name = book_name
        self.author_name = author_name
        self.copies = copies 
        
        book.books+=1
    def __str__(self):
        return f"{self.copies} , {self.id} , {self.book_name} , {self.author_name}"
    def get_numberofbookexist(self):
        return book.books
# -----------------------------------------------------------------------
# Functions |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# -----------------------------------------------------------------------
# Printing Screen ( Done )
    def printscreen():
        print("")
        print("Welcome To The Library")
        print("------------------------------------")
        print("1 ) Add New Book")       
        print("2 ) Delete a Book")      
        print("3 ) Update a Book")      
        print("4 ) Check a Book")       
        print("5 ) Display Books") 
        print("6 ) Number of Books Exist In Library")   
        print("7 ) Exit from system") 
        print("------------------------------------") 
# -----------------------------------------------------------------------
#Add New Book ( Done ) ( Edit in case the book is exist )
    def add_book(id,library):
        bookN = input("Enter Book Name : ")
        AuthotN = input("Enter Author Name : ")
        while True :
            try: #Checking if input is integer or not
                copies = int(input("Enter Number Of Copies : "))
                break
            except:
                print("That's Not Number Of Copies ( Enter An Integer Number )")
        library.append(book(id,bookN,AuthotN,copies))
        print("")
        print("-----------------------")
        print("Book Added Successfully")
        print("-----------------------")
        print("")
# -----------------------------------------------------------------------
#Print All Books in Library ( Done )
    def view_all(library):
        table = PrettyTable()
        table.field_names = ["Copies", "ID", "Name", "Author"]

        for book in library:
            table.add_row([book.copies, book.id, book.book_name, book.author_name])
            table.add_row(["-" * 8, "-" * 4, "-" * 6, "-" * 8])
        table.title = "Library Books"
        print(table)
# -----------------------------------------------------------------------
    def save_to_excel(library):
        with open("library.xlsx", 'w') as file:
            file.write("Copies,ID,Name,Author\n")  # Write header
            for book in library:
                file.write(f"{book.copies:^10},{book.id:^5},{book.book_name:^20},{book.author_name:^15}\n")  # Use ^ for center alignment
# -----------------------------------------------------------------------
# Delete Specific Book ( Done )
    def delete_book(library): 
        while True:
            try : #Checking if input is integer
                delete = int(input("Enter The ID : "))
                break
            except:
                print("Invalid Input ( Enter Integer Number )")
        
        index = -1
        for book in library:
            index+=1
            if book.id == delete:
                break
        if index == len(library) + 1 or index == -1:
            print("Book does not exist")
        else:
            del library[index]
            print("Book Removed Successfully")
            print("-------------------------")
# -----------------------------------------------------------------------
# Exit Screen ( Done )
    def exit():
        print("--------------------")
        print("System Closing")
        print("!...GOOD BYE...!")
        print("--------------------")
# -----------------------------------------------------------------------
# Check If Exist or not ( Done )
    def checks(id,library):
        exist = False
        for book in library:
            if book.id == id:
                exist = True
                break
        if exist :
            return 1
        else:
            return 0
# -----------------------------------------------------------------------
#Check if exists ( Done )
    def check_book(id,library):
        exist = False
        index = 0
        copy = 0
        for book in library:
            if book.id == id:
                exist = True
                copy = book.copies
                break
            index+=1
        if exist :
            print("-------------------------------------------")
            print("Book exists")
            print(f"It Exist At the Roof Number {index+1} ")
            print(f"There's {copy} of this Book In our Library")
            print("-------------------------------------------")
        else:
            print("-------------------")
            print("Book does not exist")
            print("-------------------")      
# -----------------------------------------------------------------------
# Get Book Index ( Done )
    def index(id,library):
        index = -1
        for book in library:
            index+=1
            if book.id == id:
                break
        return index
# -----------------------------------------------------------------------
# Save list of books to file
    def save_to_file(library):
        with open("LibraryData.txt", 'w') as file:
            for book in library:
                file.write(str(book) + '\n')
# -----------------------------------------------------------------------
# Load list of books from file
    def load_from_file():
        class_instances = []
        try:
            with open("LibraryData.txt", 'r') as file:
                for line in file:
                    # Split the line by comma
                    parts = line.strip().split(',')
                    # Extract attributes from the split parts
                    copies = int(parts[0])
                    book_id = int(parts[1])
                    book_name = parts[2]
                    author_name = parts[3]
                    # Create a new instance using the extracted attributes
                    class_instances.append(book(book_id, book_name, author_name,copies))
            return class_instances
        except FileNotFoundError:
            return []
# -----------------------------------------------------------------------
# Update Specific Book ( Done )
    def update_book(place, library,Id = None):
        if id == None:
            while True :
                try: #Checking if input is integer or not
                    library[place].id = int(input("New Book ID : "))
                    break
                except:
                    print("That's Not ID ( Enter An Integer Number )")
        else:
            library[place].id = Id
        library[place].book_name = input("Enter New Book Name : ")
        library[place].author_name = input("Enter New Author Name : ")
        while True :
            try: #Checking if input is integer or not
                library[place].copies = int(input("Enter Number Of Copies : "))
                break
            except:
                print("That's Not Number Of Copeis ( Enter An Integer Number )")
        print("")
        print("Book Updated Successfully")
        print("-------------------------")
# -----------------------------------------------------------------------
