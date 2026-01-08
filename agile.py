n=int(input("enter the number of books:"))
books=[]
author=[]
for i in range(n):
    books.append(input("enter the book name: "))
    author.append(input("enter the author name: "))
print("Book",'   ',"Author")
for i in range(n):
    print(books[i],"  ",author[i],end="\n")
print("Thank you")