def isEmpty(s):
    return len(s) == 0

def Push(s):
    bno = int(input("Enter Book Number: "))
    bname = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    s.append([bno, bname, author])
    print("Book pushed successfully!")

def Pop(s):
    if isEmpty(s):
        print("Underflow! Stack is empty.")
    else:
        item = s.pop()
        print("Popped Book:", item)

def Display(s):
    if isEmpty(s):
        print("Stack is empty.")
    else:
        for i in range(len(s) - 1, -1, -1):
            print("Book No:", s[i][0], "Name:", s[i][1], "Author:", s[i][2])

stack = []
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        Push(stack)
    elif choice == 2:
        Pop(stack)
    elif choice == 3:
        Display(stack)
    elif choice == 4:
        break