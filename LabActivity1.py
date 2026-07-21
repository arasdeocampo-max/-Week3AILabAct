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



# 6. What happens if a student types "Yes" instead of "yes" for overdue books, or "Active" instead of "active" for status? 
# How should Aliah's code handle these input variations so the kiosk doesn't break? 
#-answer:Case-sensitive ang Python, kaya ang "Yes" o "Active" ay hindi magmamatch sa "yes" o "active". Pwedeng magkamali 
# ang kiosk at isiping walang overdue books ang student o invalid ang status niya.Para maiayos ito Gamitan ng .strip().lower() ang mga input(). 
# Tinatanggal nito ang extra spaces at ginagawang lowercase ang lahat ng letters para matapat sa conditions nang hindi nag-e-error.


#7.  The rules say overdue books block borrowing **"regardless of status"** — meaning even an active-status student with overdue books is
#  blocked. Why did Aliah write the overdue check as a priority condition, and what would go wrong if she checked status first instead?

#ANS: Unang requirement ito sa rule sa written output ito ang nagsisilbing harang ang may overdue books 
# regardless ng status para mabilis ma-reject ang ineligible.

#Anong problema kung inuna ang status: Pwedeng makalusot ang active student na may overdue, o kaya magpakita ang system ng maling error 
# message kaysa na sabihing isauli muna ang libro.

#8 What if a student has no overdue books, active status, but tries to borrow 0 books? 
# Should the kiosk treat this as valid input or an error? Modify your code to handle this edge case gracefully.

#ans: its an invalid input. Ang kiosk ay dapat magpakita ng error message na nagsasabing kailangan mag-request ng kahit isang libro para makapag-borrow.