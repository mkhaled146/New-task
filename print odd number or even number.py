def print_number():

   start=int(input("Enter Start Number:"))
   end=int(input("Enter End Number:"))

   for number in range(start,end+1):
      if number % 2 == 0:
         print (number,"Even Number")
   print("----------")
   for number in range(start,end+1):
      if number % 2 != 0:
         print (number,"Odd Number")

print_number()

