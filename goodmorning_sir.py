import time
name=input("Enter your name : ")
timestamp= time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
print(timestamp)

if hour>=0 and hour<12:
    print(f"Good Morning {name} !")
elif hour>=12 and hour<16:
    print(f"Good Afternoon {name} !")
elif hour>=16 and hour<20:
    print(f"Good Evening {name} !")
elif hour>=20 and hour<0:
    print(f"Good Night {name} !")
