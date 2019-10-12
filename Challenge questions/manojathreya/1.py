#@author:Manoj Athreya A

#write a program to print occurance count of all the characters of a string.

str="Good Morning"
d=dict()
count=0
for char in str:
    if char in d:
        d[char]=d[char]+1
    else:
        d[char]=1
print(d)

#OUTPUT: {'G': 1, 'o': 3, 'd': 1, ' ': 1, 'M': 1, 'r': 1, 'n': 2, 'i': 1, 'g': 1}

