def create_f():
    content = "The UAE (United Arab Emirates) is a federation of seven emirates renowned for its modern architecture, luxury shopping, and thriving economy. Situated on the Arabian Peninsula, it has become a global hub for business, tourism, and innovation. Balancing rich cultural traditions with futuristic development, the UAE is a unique blend of past and future."
    f = open("uae.txt", "w")
    f.write(content)
    f.close()
    print("File created successfully!")

def display_f():
    f = open("uae.txt", "r")
    t = f.read()
    f.close()
    print(t)

def search_word():
    w = input("Enter word to search: ")
    f = open("uae.txt", "r")
    t = f.read().split()
    f.close()
    c = t.count(w)
    print("Word count:", c)

while True:
    print("1. Create file")
    print("2. Display file")
    print("3. Search word")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        create_f()
    elif choice == 2:
        display_f()
    elif choice == 3:
        search_word()
    elif choice == 4:
        break