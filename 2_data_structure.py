# Task 1: Library System Enhancement

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]


new_book = ('More Than A Carpenter', 'Josh McDowell')
# new_book = ('1984', 'George Orwell') #Remove comment to see else statement print

title, author = new_book

if new_book not in library:
    library.append(new_book)
    print(f'{title} by {author} has been added to library')
else:
    print('This book already exists')
