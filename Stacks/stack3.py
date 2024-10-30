from stack1 import *
s = input("Enter a string: ")
l = []
t = 0
for i in s[::-1]:
    push(l,t,i)
print(l)