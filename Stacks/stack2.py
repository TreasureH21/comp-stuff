from stack1 import *

l = []
t = 0
e1 = int(input("Enter 1st element: "))
e2 = int(input("Enter 2nd element: "))
t = push(l,t,e1)
t = push(l,t,e2)
p,tt = pop(l,t)
print(f"popped element: {p}, top = {tt}")