import random
print("I am going to generate passwords for you")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

number = int(input("How many passwords do you want to generate:"))
length = int(input("How many characters do you want your password to have:"))

passwords_list = []

print("\n Choose your passwords from the list below:")
for pwd in range (number):
    passwords = ""
    for c in range (length):
        passwords += random.choice(chars)
    passwords_list.append(passwords)
print(passwords_list)