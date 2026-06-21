"""bag=int(input("Enter baggage weight = "))
if bag<= 20:
    print("Free of Charge ")
elif bag<= 21 and bag <= 30:
    bags=bag-20
    bags=bags*200
    print(f"Your price is {bags} ")
else:
    print("Not allowed ")"""

"""salary=float(input("Enter your salary = "))
if salary >=10000:
    bonus=(salary/100)*115
elif salary> 50000 and salary <= 99999:
    bonus=(salary/100)*110
else:
    bonus=(salary/100)*105
print(f"Your salary and bonus = {bonus} ")"""


"""count=0
tot=0
while count<=10:
    tot=tot+count
    count=count+1
print(f"Answer is {tot}")
"""

"""mark=0
count=0
avg=0
tot=0
while count<=10:
    
    mark=float(input("Enter your mark = "))
    tot=tot+tot
    count=count+1
    tot=tot+mark
avg=tot/10

if avg>=50:
    print(f"Your are pass ")
else:
    print(f"Your are fail " )
print(f"your average {avg}")"""
"""tot=0
while True:
    num=float(input("Enter your number "))
    if num == -1:
        break
    tot=tot+num
    print(tot)"""

word=input("Enter your word ")
count=0

i=0
while i<len(word):
    if word [i].lower() in "aeiou":
        count+=1
    i+=1
print(f"Your word have vovels {word}")

 
 
    



