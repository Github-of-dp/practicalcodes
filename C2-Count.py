v=c=l=u=o=0

f = open("aboutuae.txt", "r")
t = f.read()
f.close()

for ch in t:
    if ch.isalpha():
        if ch.islower():
            l = l + 1
        elif ch.isupper():
            u = u + 1
        elif ch in "aeiouAEIOU":
            v = v + 1
        else:
            c = c + 1
    else:
        o = o + 1

print("Total Vowels:", v)
print("Total Consonants:", c)
print("Total Lowercase Characters:", l)
print("Total Uppercase Characters:", u)
print("Characters other than letters:", o)