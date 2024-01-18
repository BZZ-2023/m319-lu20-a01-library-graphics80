from datetime import datetime
from math import inf
from rental import Rental


def init_books():
    """
    inits the books dictionary
    :return:
    """
    books = {
        'LOTR 1': [],
        'LOTR 2': [],
        'LOTR 3': []
    }
    return books


def read_rental():
    """
    gets the rental details from customer
    :return:
    """
    start_date = read_date('Enter rental date (dd.mm.yyyy): ')
    num_days = read_int('Enter number of rental days: ')
    end_date = read_date('Enter return date (dd.mm.yyyy): ')
    rental = Rental(start_date,end_date,num_days)
    return rental


def add_rental(books):
    """
    adds a new rental
    :param books:
    :return:
    """
    while True:
        book_name = input('Enter the book')

        if book_name in books:
            rental = read_rental()
            books[book_name].append(rental)
            choice = input('Do you want to enter another booking (y/n)')
            if choice != 'y':
                break
        else:
            print('Book not found')


def show_balance(books):
    """
    Prints the balance
    :param books:
    :return:
    """
    for book, rentals in books.items():
        print(f'Statement for {book}')

        total = 0
        for rental in rentals:
            #print(f'  - {datetime.strftime(rental.rental_date,"%d.%m.%Y")}: CHF {rental.cost}')
            print(f'  - {rental.rental_date.strftime("%d.%m.%Y")}: CHF {rental.cost}')
            total += rental.cost
        print(f'Total: CHF {total}')


def read_int(text_to_display, lower_bound = float(-inf), upper_bound = float(inf)):
    '''
    Read an int from the user within bounds
    '''
    while True:
        try:
            num = int(input(text_to_display))
        except ValueError:
            print("Please, enter a whole number!")
            continue
        else:
            if num < lower_bound:
                print("Please, enter a number greater than or equal to", lower_bound)
                continue
            if num > upper_bound:
                print("Please, enter a number less than or equal to", upper_bound)
                continue
            return num

def read_date(prompt):
    """
    Reads a date from console format dd.mm.yyyy
    :param prompt: Text to show the user
    :return:
    """
    while True:
        s = input(prompt)
        try:
            dt = datetime.strptime(s, '%d.%m.%Y')
            return dt
        except ValueError:
            print("Please enter a valid date.")



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
