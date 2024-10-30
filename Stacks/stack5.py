def hire(l,t,e):
    l.append(e)
    t += 1
    return t
def fire(l,t):
    if not l:
        t = -1
        return ("No one to fire")
    else:
        t = len(l) - 1
        r = l.pop()
        return r,t   

l = []

while True:
    print("""[1] hire employee
[2] fire employee
[3] quit""")
    ch = int(input("Enter choice: "))
    if ch == 1:
        l1 = []
        emp_name = input("Enter employee and name: ")
        emp_sal = int(input("Enter salary of employee: "))
        l1 += [emp_name, emp_sal]
        a = hire(l,len(l),l1)
        print(f"updated stack: {l}, no of emplyees: {a}")
    elif ch == 2:
        fired_emp, n = (fire(l,len(l)))
        print(f"fired employee: {fired_emp}, no of employees left: {n}")
    else: 
        break

