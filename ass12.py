f = open("Poem.txt","r")
l = f.readlines()
l = l[::-1]
f.close()
f = open("reversePoem.txt", "w")
for i in range(len(l)):
    if i == 0:
        f.write(l[i]+"\n")
    else:
        f.write(l[i])





fmain = open("fileNames.txt","r")
l = fmain.readlines()
for i in l:
    ffile = open(i[:-1] , "r" )
    lf = ffile.readlines()
    w = 0
    d = 0
    lines = len(lf)
    for j in lf:
        w += len(j.split())
        for k in j:
            if ord(k) in range(48,58):
                d += 1
    
    print(i[:-1])
    print("No of words are :",w)
    print("Number of digits are :",d)
    print("Number of lines are :",lines)
    print()






username = input("Enter a username : ")


f = open("users.txt", "r")
u = True
l = f.readlines()
for i in l:
    stored_username, _ = i.split(" ")
    if stored_username == username:
        print("Username already exists")
        u = False
        break

if u:
    pwd = input("Enter Password : ")
    f.close()
    f = open("users.txt", "a")
    f.write(username + " " + pwd + "\n")
