first_line = str(input()).split(" ")
n = int(first_line[0])
t = int(first_line[1])
second_line = str(input).split(" ")
books = str(input()).split(" ")
books = [int(book) for book in books]

max_book = 0
start_book = 0
read_time = 0

for end_book in range(n):
    read_time+=books[end_book]
    while read_time > t:
        read_time -=books[start_book]
        start_book+=1
    max_book = max(max_book,end_book-start_book+1)

print(max_book)