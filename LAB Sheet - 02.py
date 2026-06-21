a=int(input("enter room charge per day "))
b=int(input("number of days live "))
c=int(input("food charges "))
f=int(input("service cgarge is "))

d= a*b
total=d+c+f
sertotal = total /10%
g= sertotal + d

print(f"your subtotal is {d}")
print(f"your service chage {f}")
print(f"your final bill is {sertotal}")
