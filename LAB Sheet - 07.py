"""
bill=0
for i in range (1,5):
    unit=int(input("Enter your unit = "))
    if unit>0:
        if unit<=100:
            bill=unit*10
        else:
            if unit<=100 and unit>=200:
                bill=(100*10)+(reamining*15)
            else:
                remaining=unit-60
                bill=(100*10)+(100*15)+(remaining*20)
        print(f"Display bill {bill}")
        """
"""
exam=0
exams=0
for i in range(1,11):
    attend=float(input("Enter your attendance = "))
    if attend>=75:
        print("Your are eligibility sit the exam")
        exam=exam+1
    else:
        print("Your are not eligibility sit the exam")
        exams=exams+1
    
    
print(f"Number of not eligibility students {exams}")
print(f"Number of eligibility students {exam}")"""

"""total_bill=0
item=0
while True:
    bill=float(input("Enter your price = "))
    if bill == 0:
     break
    total_bill=total_bill+bill
    item=item+1
print(f"Your total bill is {total_bill}")
print(f"Your purches iteam are {item}")
"""
"""
tot=0
sus=0
while True:
    draw=float(input("Enter your withdraw amount = "))
    if draw==-1:
        break
    if 50000<draw:
        print("Insuffcint Account balance")
    else:
        tot=50000-draw
        sus=sus+1
    print(f"Your total reamining balance is {tot}")
print(f"Number of seccesfull withdraw {sus}")"""



for i in range(1,9):
    mark=float(input("Enter your marks = "))
    


























        
