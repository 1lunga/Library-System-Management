#Task1A: Calling Functions

books=[]
members=[]

def add_books(book_id, tittle, auhtor, status):
    books.append({"book_id": book_id,"tittle": tittle,"author": auhtor, "status": status})

def add_members(member_id, name):
    members.append({"member_id": member_id,"name": name,"borrowed_books": ""})

add_books(2024001, "Python Progarmming", "Jacob Zuma", "Available")

add_members(1, "Anelisa Maleka")

print("Books:", books)
print("\nMemebrs:", members)

#########################
#Task1B: Calling Functions without using parameters and arguments

books=[]
members=[]

def add_books():
    books.append({"book_id": "book_id","tittle": "tittle","author": "auhtor","status":"status"})

def add_members():
    members.append({"member_id": "member_id","name": "name","borrowed_books": ""})

add_books()

add_members()

print("\nBooks:", books)
print("\nMemebrs:", members)

########################
#Task1C: Track Without using Functions

add_books = ({"book_id": "book_id","tittle": "tittle","author": "auhtor","status":"status"})
books.append(add_books)

add_members = ({"member_id": "member_id","name": "name","borrowed_books": ""})
members.append(add_members)

print("\nBooks:", books)
print("\nMemebrs:", members)

########################
#Task1D: Using DataFrames instead of lists

import pandas as pd

add_books = ({"book_id": ["book_id"],"tittle": ["tittle"],"author": ["auhtor"],"status":["status"]})
books.append(add_books)
df = pd.DataFrame(add_books)

add_members = ({"member_id": ["member_id"],"name": ["name"],"borrowed_books": [""]})
members.append(add_members)
df = pd.DataFrame(add_members)

print("\nBooks:", books)
print("\nMemebrs:", members)


