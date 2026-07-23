def add(a,b):
    return a+b
result=add(5,6)
print(result)


def myname(str):
    print(f"this is my name {str}")

myname("abinash")

def check_weather(temp):
    itshot="very hot"
    itsnothot="not hot"
    if temp>26:
        #print("its very very hot")#
        return itshot
    elif temp>25:
        #print("its very  hot")#
        return itsnothot

    
for i in range(0,5):
   print( check_weather(24+i))

def area(len,bre):
    return len*bre

room_area=area(14,16)
print(f"area of the room is {room_area} sqft")


def double(nu):
    return nu*2

if((double(3)+2)>10):
    print("big number")

