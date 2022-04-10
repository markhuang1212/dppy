import csv

def read_book_csv(num_of_books = 100) -> list[list[int]]:
    file = open("Books.csv")
    reader = csv.reader(file)
    books: list[int] = []

    line = next(reader)
    curr_book = [int(float(line[2]))]
    curr_book_id = line[0]

    while True:
        if len(books) == num_of_books:
            return books

        line = next(reader)
        if len(line) == 0:
            return books
        
        if line[0] != curr_book_id:
            books.append(curr_book)
            curr_book = []
            curr_book_id = line[0]

        curr_book.append(int(float(line[2])))

books = read_book_csv(10000)
