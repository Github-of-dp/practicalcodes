import pickle

def write():
    f = open("student.dat", "ab")
    r = int(input("Enter Roll Number: "))
    n = input("Enter Name: ")
    m = float(input("Enter Marks: "))
    pickle.dump([r, n, m], f)
    f.close()
    print("Record added!")

def display():
    f = open("student.dat", "rb")
    try:
        while True:
            r = pickle.load(f)
            print("Roll No:", r[0], "Name:", r[1], "Marks:", r[2])
    except EOFError:
        f.close()

def update():
    ru = int(input("Enter Roll Number to update: "))
    f = open("student.dat", "rb")
    r = []
    try:
        while True:
            r.append(pickle.load(f))
    except EOFError:
        f.close()
    
    f = open("student.dat", "wb")
    for i in r:
        if i[0] == ru:
            i[2] = float(input("Enter new marks: "))
        pickle.dump(i, f)
    f.close()
    print("Marks updated!")

while True:
    print("1. Write Data")
    print("2. Display Data")
    print("3. Update Marks")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        write()
    elif choice == 2:
        display()
    elif choice == 3:
        update()
    elif choice == 4:
        break