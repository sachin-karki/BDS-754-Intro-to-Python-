# Sachin Karki
# Purpose: Assignment 3, Using while loop to count integer from 0 to 99 

print ("Numbers from 0 to 99:")
numbers = 0
while numbers <= 99: #Prints 0 to 99
  if numbers % 5 == 0: #Checks if the number is divsible by 5
    print(numbers, end = '*\n') 
    numbers=numbers+1
  else:
    print(numbers)
    numbers=numbers+1