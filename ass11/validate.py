import random

def otp():
    otp = random.randint(1000,9999)
    return otp

def captcha():
    length = int(input("Enter length of captcha: "))
    while length <= 4:
        length = int(input("Re-enter captcha length (atleast 4): "))
    
    sc = ["!","#", "$", "%", "&", "*", "?", "@", "^", "_","/",]
    uc = [chr(i) for i in range(65,91)]
    lc = [chr(i) for i in range (97,123)]
    digits = [str(i)for i in range(0,10)]

    s = ''
    t = [sc[random.randint(0,len(sc)-1)]]
    t += [uc[random.randint(0,len(uc)-1)]]
    t += [lc[random.randint(0,len(lc)-1)]]
    t += [digits[random.randint(0,len(digits)-1)]]

    random.shuffle(t)
    for i in t:
        s += i
    
    l = sc + uc + lc + digits

    k = 4
    while k<=length:
        (random.shuffle(l))
        s += l[0]
        k += 1

    return s

