import requests
response= requests.get("https://api.github.com")
print(response.status_code)
print("hello world")

total=10*10
power=10**2

String = "My name is Abinash"
longstring = """ 
My name is abinash.
I want to be a software developer 
"""
print(longstring)

first_name="Abinash"
last_name="Das"
full_name=first_name+" "+last_name
long_dash="-"*15 # this will print - 15 times#
print(full_name)
print(long_dash)

len(long_dash)+len(full_name)

is_true=True
age=18
can_vote=age>=17

age=16
has_license=True
drunk=True
can_drive=age>=18 and has_license and not drunk
print(can_drive)

score=10
score=10+5
score+=5

name="john"
string=f"Hi There, my name is {name}!"

name="Abinash is my name"
name.lower()
name.upper()
name.title()


temparature=28
humidity=70

if(temparature>30):
    print("its very hot!")
elif temparature > 25:
    print("its hot")
else:
    print("its not hot")

if temparature>20 and humidity>50:
    print("its hot and humid")
humidity=45
if temparature > 20:
    if humidity>50:
        print("its hot and humid")
    else:
        print("its hot but not humid")



for i in range(5):
    print("hello world")

letter="testing"
for i in letter:
    print(i)


for i in range(1,6):
    print(i)

for i in range(1,10,2):
    print(i)

age=25
has_license=False


#List#
my_list=["Alice",25,age,True,has_license]
my_list[0]
has_license=my_list[-1]
print(my_list[0:2])
my_list[0]="Abinash"
my_list
my_list.append("alice")
my_list.remove(my_list[-1])
my_list.insert(1,"Alice")

#dictionary#

person={
    "name":"Alice",
    "age":25,
    "City":"Newyork"
}

person["age"]=4
person["License"]=True

#Tuples#
empty=()
point=(3,5)
colours=("red","green","blue")
colours[0]="blue"  #not allowed. tuples are immutable#


#set#
empty_set=set()

numbers={1,2,3,4,5}
fruits=set(["apple","banana"])


scores=[60,70,80,90]
unique_scores=set(scores)