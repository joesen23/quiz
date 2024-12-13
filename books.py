def display_menu():
    print("Book Inventory System")
    print("Press [1] To Add Book")
    print("Press [2] To Add Multiple Books")
    print("Press [3] To View All Books")
    print("Press [4] To Delete Book")
    print("Press [5] To Update Book")
    print("Press [6] To Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            add_multiple_books()
        elif choice == '3':
            view_books()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            update_book()
        elif choice == '6':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

def add_book():
    try:
        with open("books.txt", "a") as myfile:
           
            with open("books.txt", "r") as f:
                existing_books = f.readlines()
            book_id = len(existing_books) + 1  

            title = input("Enter new book title: ")
            author = input("Enter book author: ")
            price = float(input("Enter book price: "))
            year_published = int(input("Enter year published: "))
            age = calculate_book_age(year_published)

            myfile.write(f"{book_id}|{title}|{author}|{price:.2f}|{year_published}|{age}\n")
            print(f"Book '{title}' added with ID {book_id} successfully.")
    except IOError as e:
        print(f"Error while accessing the file: {e}")

def add_multiple_books():
    try:
        num_books = int(input("Enter number of books to add: "))
        for _ in range(num_books):
            add_book()
    except ValueError:
        print("Please enter a valid number for the number of books.")

def view_books():
    try:
        with open("books.txt", "r") as myfile:
            lines = myfile.readlines()
            if lines:
                print("\n--- List of Books ---")
                for line in lines:  
                    book_id, title, author, price, year_published, age = line.strip().split('|')
                    print(f"ID: {book_id}, Title: {title}, Author: {author}, Price: ${float(price):.2f}, Year Published: {year_published}, Age: {age} years")
            else:
                print("No books available.")
    except FileNotFoundError:
        print("No books file found!")
    except IOError as e:
        print(f"Error while accessing the file: {e}")

def delete_book():
    try:
        book_id = int(input("Enter the ID of the book you want to delete: "))
        with open("books.txt", "r") as myfile:
            lines = myfile.readlines()
            if book_id > len(lines) or book_id <= 0:
                print("Invalid ID. Book not found.")
                return
            updated_lines = []
            for line in lines:
                current_id = int(line.split('|')[0])
                if current_id == book_id:
                    title, author, price, year_published, age = line.strip().split('|')
                    print(f"Deleting Book: Title: {title}, Author: {author}, Price: ${float(price):.2f}, Year Published: {year_published}, Age: {age} years")
                    continue
                updated_lines.append(line)

        with open("books.txt", "w") as myfile:
            myfile.writelines(updated_lines)

        print(f"Book with ID {book_id} deleted successfully!")
    except ValueError:
        print("Please enter a valid book ID.")
    except FileNotFoundError:
        print("No books file found!")
    except IOError as e:
        print(f"Error while accessing the file: {e}")

def update_book():
    try:
        book_id = int(input("Enter the ID of the book you want to update: "))
        with open("books.txt", "r") as myfile:
            lines = myfile.readlines()
            book_found = False
            for index, line in enumerate(lines):
                current_id, title, author, price, year_published, age = line.strip().split('|')
                if int(current_id) == book_id:
                    book_found = True
                    print(f"Current details of the book (ID: {book_id}):")
                    print(f"Title: {title}, Author: {author}, Price: ${float(price):.2f}, Year Published: {year_published}, Age: {age} years")

                    new_title = input(f"Enter new title (current: {title}): ") or title
                    new_author = input(f"Enter new author (current: {author}): ") or author
                    new_price = input(f"Enter new price (current: ${float(price):.2f}): ") or price
                    new_year_published = input(f"Enter new year published (current: {year_published}): ") or year_published
                    new_age = calculate_book_age(int(new_year_published))

                    updated_line = f"{book_id}|{new_title}|{new_author}|{new_price}|{new_year_published}|{new_age}\n"
                    lines[index] = updated_line
                    break

            if not book_found:
                print("Book with the given ID not found.")

        with open("books.txt", "w") as myfile:
            myfile.writelines(lines)

        print(f"Book with ID {book_id} updated successfully!")

    except ValueError:
        print("Please enter a valid book ID or number.")
    except FileNotFoundError:
        print("No books file found!")
    except IOError as e:
        print(f"Error while accessing the file: {e}")

def calculate_book_age(year_published):
    from datetime import date
    current_year = date.today().year
    age = current_year - year_published
    return age

if __name__ == "__main__":
    main()