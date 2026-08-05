books = []

while True:
    print("\n1.Add 2.Issue 3.Return 4.Search 5.Display 6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        books.append(input("Book name: "))

    elif ch == 2:
        b = input("Book to issue: ")
        if b in books:
            books.remove(b)
            print("Issued")
        else:
            print("Not found")

    elif ch == 3:
        books.append(input("Book to return: "))
        print("Returned")

    elif ch == 4:
        b = input("Search book: ")
        if b in books:
            print("Available")
        else:
            print("Not available")

    elif ch == 5:
        print("Books:", books)

    elif ch == 6:
        break

    else:
        print("Invalid choice")