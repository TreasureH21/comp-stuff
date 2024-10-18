import csv


# QUESTION 1 :

s = input()
l = []
l += [eval("["+s+"]")]
while s:
    l += [eval("["+s+"]")]
    s = input()


with open("dinero.csv","r", newline = "") as f:
    w = csv.writer(f)
    w.writerows(l)

with open("dinero.csv","r") as f:
    # QUESTION A : 

    r = csv.reader(f)
    yr = input("Enter Year : ")
    for i in r:
        if i:
            if yr == i[0]:
                print(i)
    
    # QUESTION B :
    for i in r:
        if i:
            if i[2][0:3] == "The":
                print(i[0],i[2])

# QUESTION C :
with open("dinero.csv" , "a") as f:
    w = csv.writer(f)
    l = [2015,61,"The Intern"]
    w.writerow(l)


# QUESTION 3 :
def add():
    with open("worldcup.csv" , "a") as f:
        w = csv.writer(f)
        tname = input("Enter Team name : ")
        wins = int(input("Enter Number of Wins : "))
        loss = int(input("Enter Number of losses : "))
        w.writerow([tname, wins, loss])
        print("Team Registered!")
        print()

def countr():
    with open("worldcup.csv" , "r") as f:
        r = csv.reader(f)
        c = 0
        for i in r:
            if i:
                if i[1] > i[2]:
                    c += 1  
    return c


while True:
    print("1. Register New Team")
    print("2. Count of teams with wins more than losses.")
    print("3. Exit")
    print()
    c = int(input("Enter Your Choice : "))
    print()
    if c == 1:
        add()
        continue
    elif c == 2:
        c = countr()
        print("The count of teams with wins more than losses is : ", c)
        print()
        continue
    elif c == 3:
        print("Exiting Program....")
        break
    else:
        print("Invalid Option Entered")