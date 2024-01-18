def init_books():
    pass


def read_rental():
    pass


def add_rental(books):
    print('Here is the book rental part')


def show_balance(books):
    print('Print the book balance here')


def read_int(prompt, minimum, maximum):
    return int(input(prompt))  # Placeholder to let main run. Delete when doing the aassignment


def read_date(prompt):
    return None


def main():
    books = init_books()
    while True:
        print('\nLibrary Management System')
        print('1. Add Rental')
        print('2. Show Balances')
        print('3. Exit')
        choice = read_int('Enter your choice (1/2/3): ', 1, 3)

        if choice == 1:
            add_rental(books)
        elif choice == 2:
            show_balance(books)
        elif choice == 3:
            break


if __name__ == '__main__':
    main()
