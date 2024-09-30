import random

def otp():
    otp = random.randint(1000,9999)
    return otp

def captcha():
    length = int(input("Enter length of captcha: "))
    while length <4:
        length = int(input("Re-enter captcha length (atleast 4): "))
    sc = ["!","#", "$", "%", "&", "*", "?", "@", "^", "_"]
    uc = chr(random.randint(65,90))
    lc = chr(random.randint(97,122))
    digits = (random.randint(0,9))

    l = []
    l += [uc,sc[random.randint(0,len(sc)-1)],lc,str(digits)]
    (random.shuffle(l))
    s = ''
    for i in l:
        s += i
    k = 4
    while k<=length:
        l = []
        l += [uc,sc[random.randint(0,len(sc)-1)],lc,str(digits)]
        (random.shuffle(l))
        s += l[0]
        k += 1

    return s

print(otp())
print(captcha())


    

