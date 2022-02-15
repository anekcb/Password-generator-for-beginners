#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=""
for i in range(0,nr_letters):
  a=random.choice(letters)
  password=password+a
password2=""
for i in range(0,nr_symbols):
  a=random.choice(symbols)
  password2=password2+a
password3=""
for i in range(0,nr_numbers):
  a=random.choice(numbers)
  password3=password3+a
b=password+password2+password3
print (f"ordered password is {b}")
li=[]
c=''
for j in range (0,len(b)):
  c=b[j]
  li.append(c)
random.shuffle(li)
t=""
for j in li:
  t+=j
print(f"your shuffled password is {t}",end="")
