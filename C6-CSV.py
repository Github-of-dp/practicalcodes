import csv

def add():
    f = open("credentials.csv", "a", newline="")
    w = csv.writer(f)
    uid = input("Enter User ID: ")
    pwd = input("Enter Password: ")
    w.writerow([uid, pwd])
    f.close()
    print("User added!")

def display():
    f = open("credentials.csv", "r")
    r = csv.reader(f)
    for row in r:
        if row:
            print("User ID:", row[0], "Password:", row[1])
    f.close()

def search():
    sid = input("Enter User ID to search: ")
    f = open("credentials.csv", "r")
    r = csv.reader(f)
    for row in r:
        if row and row[0] == sid:
            print("Password is:", row[1])
            break
    f.close()

while True:
    print("1. Add User")
    print("2. Display Users")
    print("3. Search Password")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        add()
    elif choice == 2:
        display()
    elif choice == 3:
        search()
    elif choice == 4:
        break