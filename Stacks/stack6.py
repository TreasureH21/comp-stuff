from stacks import *



# QUESTION 6

"""

6.	Write a menu driven program to accept and store a list of names who come to the canteen for meals. Perform the following operations by implementing a stack. Take care of the boundary conditions. 
 
1.	Issue a token (ask for name, generate a token number, and add to the stack [<token>, <name>])
2.	Issue meal (accept ‘n’ remove ‘n’ students from the stack. Display their names)
3.	Exit
         Sample list: [ [1,”Josh”],[ 2,”Rohan”]]


"""


l = []
while True:
    print("1. Issue a token")
    print("2. Issue meals to n students")
    print("3. Exit")
    print()
    c = (input("Enter your choice : "))
    if c == "1":
        n = input("Enter name : ")
        l = push(l, (  len(l), n ))
        print("Token given to student",n)
    elif c == "2":
        n = int(input("Enter the number of meals given out : "))
        r = 0
        while r < n:
            t = pop(l)
            if t:
                print("Meal issued to", t[1])
            else:
                print("No more students to give meals to")
                break
        
    elif c == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid Option entered. Try again")
    
    print()