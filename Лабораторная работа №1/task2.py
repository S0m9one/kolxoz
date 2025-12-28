


weight_of_symbol = 4
symbols = 25
strings = 50
pages = 100
capacity = 1.44 * 1024 ** 2

weight_of_book = weight_of_symbol * symbols * strings * pages
count_of_books = round(capacity / weight_of_book)



# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", count_of_books)