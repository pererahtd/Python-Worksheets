name = "Thimira\nDhananjaya"
school = "Kiriella Central Collage"
result = 22/7

print(name)
print(school)

print("The result of 22 divided by 7:", result)
print(type(result))

operation = "sum"
total = 8

# Using f-strings (The modern, clean way)
print(f"The {operation} is {total}")

print("Hello", name, "Welcome to NSBM!")

# --- Input Section ---
name1 = input("Enter your name: ")
print("Hello", name1, "Welcome to NSBM!")

# Fix: Convert input to integers so you can actually add them
no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))
add = no1 + no2
print(f"Answer: {add}")

# --- Birthday Section ---
bdyear_input = input("What is your birth year? ")
bdyear = int(bdyear_input)

# Fix: Use a comma or f-string to avoid the "TypeError"
print("Your birthday year type is:", type(bdyear))
print(f"Your birthday year is: {bdyear}")