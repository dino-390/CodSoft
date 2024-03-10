import random

uppercase = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
lowercase = uppercase.lower()
numbers = "0123456789"

upper, lower, num = True , True , True

create=""
if upper:
    create += uppercase
if lower:
    create += lowercase
if num:
    create += numbers
    
print("Random Password Generator")
length = int(input("Enter the length for your password: "))
amount = int(input("Enter the number of passwords to generate: "))

for i in range(amount):
    password = "".join(random.sample(create, length))
    print(password)
