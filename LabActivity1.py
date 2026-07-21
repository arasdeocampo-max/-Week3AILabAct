#Activity 1: Aliah's Interactive Library Kiosk

def check_borrowing(overdue_books, status):
    if overdue_books:
        return "Not allowed has overdue books"
    elif status == "suspended":
        return "Not allowed for suspended account"
    elif status == "active":
        return "Borrowing allowed"
    else:
        return "invalid status"


allowed_borrowers_count = 0

print("= Welcome to the Library Kiosk =\n")


while True:
    name = input("Enter your name (or type 'quit' to exit): ").strip()
    if name.lower() == "quit":
        break

    overdue_input = input("Do you have overdue books? (yes/no): ").strip().lower()
    overdue_books = overdue_input == "yes"

    status_input = input("Enter your account status (active/suspended): ").strip().lower()
    result = check_borrowing(overdue_books, status_input)

    if result == "Borrowing allowed":
        books_requested = int(input("How many books do you want to borrow?: "))
        if books_requested <= 0:
            print("Invalid input: You must request at least 1 book to borrow.\n")
            continue
        if books_requested > 3:
            print("Warning: Maximum limit is 3 books per student. Capping request to 3 books.")
            books_allowed = 3
        else:
            books_allowed = books_requested


        allowed_borrowers_count += 1
        print("Success! " + name + " is allowed to borrow " + str(books_allowed) + " book(s).\n")
    else:
        print(name + ": " + result + ".\n")

print("\n=== Library Kiosk Session Ended ===")
print("Total students successfully borrowed books: " + str(allowed_borrowers_count))