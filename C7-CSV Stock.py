import csv

def create():
    f = open("stock.csv", "w", newline="")
    w = csv.writer(f)
    w.writerow(["ItemNo", "ItemName", "Quantity"])
    n = int(input("How many records: "))
    for i in range(n):
        ino = int(input("Enter Item Number: "))
        iname = input("Enter Item Name: ")
        qty = int(input("Enter Quantity: "))
        w.writerow([ino, iname, qty])
    f.close()
    print("Records added!")

def display():
    f = open("stock.csv", "r")
    r = csv.reader(f)
    for row in r:
        if row:
            print("Item No:", row[0], "Item Name:", row[1], "Quantity:", row[2])
    f.close()

def reorder():
    f = open("stock.csv", "r")
    r = csv.reader(f)
    data = list(r)
    f.close()
    
    for row in data[1:]:
        if row and int(row[2]) < 50:
            print("Reorder Item:", row[0], row[1], row[2])

while True:
    print("1. Add Records")
    print("2. Display Records")
    print("3. Re-order Items")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        create()
    elif choice == 2:
        display()
    elif choice == 3:
        reorder()
    elif choice == 4:
        break