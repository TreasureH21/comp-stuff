import random

def otp():
    otp = random.randint(1000,9999)
    return otp



def captcha():
    def rcs(x): # rcs for random character selector
        return (x[random.randint(0,len(x)-1)])
    
    length = int(input("Enter length of captcha: "))
    while length <4:
        length = int(input("Re-enter captcha length (atleast 4): "))
    sc = "!#$%&*?@^_"
    uc = "QWERTYUIOPASDFGHJKLZXCVBNM"
    lc = "qwertyuiopasdfghjklzxcvbnm"
    digits = "1234567890"

    l = []
    l += [rcs(sc)] + [rcs(uc)] + [rcs(lc)] + [rcs(digits)]
    (random.shuffle(l))
    s = ''
    for i in l:
        s += i
    k = 4
    total = sc + uc + lc + digits
    while k<=length:
        s += rcs(total)
        k += 1

    return s
