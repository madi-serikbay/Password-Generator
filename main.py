#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# for n in range(1, nr_letters + nr_symbols + nr_numbers + 1):
#   if n <= nr_letters:
#     password += letters[random.randint(0, len(letters) - 1)]
#   elif n <= nr_letters + nr_symbols:
#     password += symbols[random.randint(0, len(symbols) - 1)]
#   else:
#     password += numbers[random.randint(0, len(numbers) - 1)]
# print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
count_l = 0
count_s = 0
count_n = 0
password = ""
for n in range(1, nr_letters + nr_symbols + nr_numbers + 1):
  x = random.randint(1, 3)
  if x == 1:
    if count_l < nr_letters:
      password += letters[random.randint(0, len(letters) - 1)]
      count_l += 1
    else:
      x = random.randint(1, 2)
      if x == 1:
        if count_s < nr_symbols:
          password += symbols[random.randint(0, len(symbols) - 1)]
          count_s += 1
        else:
          password += numbers[random.randint(0, len(numbers) - 1)]
          count_n += 1
      elif x == 2:
        if count_n < nr_numbers:
          password += numbers[random.randint(0, len(numbers) - 1)]
          count_n += 1
  elif x == 2:
    if count_s < nr_symbols:
      password += symbols[random.randint(0, len(symbols) - 1)]
      count_s += 1
    else:
      x = random.randint(1, 2)
      if x == 1:
        if count_l < nr_letters:
          password += letters[random.randint(0, len(letters) - 1)]
          count_l += 1
        else:
          password += numbers[random.randint(0, len(numbers) - 1)]
          count_n += 1
      elif x == 2:
        if count_n < nr_numbers:
          password += numbers[random.randint(0, len(numbers) - 1)]
          count_n += 1
        else:
          password += letters[random.randint(0, len(letters) - 1)]
          count_l += 1
  elif x == 3:
    if count_n < nr_numbers:
      password += numbers[random.randint(0, len(numbers) - 1)]
      count_n += 1
    else:
      x = random.randint(1, 2)
      if x == 1:
        if count_l < nr_letters:
          password += letters[random.randint(0, len(letters) - 1)]
          count_l += 1
        else:
          password += symbols[random.randint(0, len(symbols) - 1)]
          count_s += 1
      elif x == 2:
        if count_s < nr_symbols:
          password += symbols[random.randint(0, len(symbols) - 1)]
          count_s += 1
        else:
          password += letters[random.randint(0, len(letters) - 1)]
          count_l += 1
print(password)
count_l = 0
count_s = 0
count_n = 0
for n in password:
  if n in letters:
    count_l += 1
  elif n in symbols:
    count_s += 1
  else:
    count_n += 1
print(f"{count_l} letters, {count_s} symbols, {count_n} numbers.")
        
        
      
      
 