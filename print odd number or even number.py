def print_number():

   start=int(input("Enter Start Number:"))
   end=int(input("Enter End Number:"))

   
   for start in range(start,end+1):
      if start % 2 == 0:
         print(f'{start}')

          
   for end in range(start,end+1):
      if end % 2 != 0:
         print (f'{start}')



print_number()
