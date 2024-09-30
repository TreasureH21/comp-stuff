from datetime import *

ist = datetime.now()
print(ist)
syd = ist + timedelta(hours =5, minutes = 30)
nyc = ist - timedelta(hours =9, minutes = 30)
jhn = ist - timedelta(hours =3, minutes = 30)

print(ist.hour,':',ist.minute)
print(syd.hour,':',syd.minute)
print(nyc.hour,':',nyc.minute)
print(jhn.hour,':',jhn.minute)
