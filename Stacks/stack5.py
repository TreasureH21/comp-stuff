from stacks import *


l = []


i = int(input("Enter decimal number to convert to binary : "))

n = i
l = []

while n != 0:
    d = n%2
    n = n//2
    l = push(l,d)
    
b = ''
while l:
    t = str(pop(l))
    b += t   
print(b)

