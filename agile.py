n=int(input("enter the number of books:"))
books=[]
for i in range(n):
    books.append(input("enter the book name: "))
print("Book")
for i in range(n):
    print(books[i],end="\n")
print("Thank you")