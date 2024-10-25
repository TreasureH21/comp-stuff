def push(l,t,e):
    l.append(e)
    t += 1
    return t
def pop(l,t):
    if t == -1:
        print("stack is empty, cannot pop stack")
    t = 0
    r = l.pop()
    print(f"popped element is {r}")
    return r,t   
