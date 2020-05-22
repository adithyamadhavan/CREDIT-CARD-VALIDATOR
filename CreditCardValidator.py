#Credit Card Validator
cardtype = input("Enter the Credit Name \n 1. Mastercard \n 2. Visa \n 3.American Express \n 4. Discoverer : ")

sc = input("Enter the credit card number:")
#LUHN ALGORITHM

# -> STEP 1
output = [int(x) if x.isdigit() else x  
          for z in sc for x in str(z)]
print(output)

#PART 1 OF LUHN ALGORITHM
part1  = output[::2]
print(part1)

# -> Step 2
part2 = output[1::2]
print(part2)

# -> Step 3
part_2 = [i*2 for i in part2]
print(part_2)

# PART 2 OF LUHN ALGORITHM

# --> Step 1
lst = []
for k in part_2:
    if k<10:
        lst.append(k)
        

print(lst)

# --> Step 2
lst1 = []
for num in part_2:
    if num >= 10:
        lst1.append(num)
        
        
print(lst1)

# --> Step 3
a = []
for number in lst1:
    if number >= 10:
        rem = number%10
        s = rem +1
        a.append(s)
        
        
        
print(a)

# Adding Part 1 and Part 2 in List
secondhalf = lst
secondhalf.extend(a)
print(secondhalf)
part1.extend(secondhalf)
print(part1)

# Check For CreditSum of Credit Card Digits
creditsum = sum(part1)
su = 0
if creditsum%10 == 0:
    su += 1
    print("Credit Card Number is valid")
else:
    print("Credit Card Number is Invalid")
    print(creditsum)
#
# Checking it applies to all conditions of Credit Card
#  
if cardtype == 'Mastercard' and sc[0] == '5' and su == 1 :
    print("Credit Card Number is Valid")
    
elif cardtype == 'Visa' and sc[0] == '4' and su == 1:
    print("Credit Card Number is Valid ")
    
elif cardtype == 'American Express' and sc[0] == '3' and su == 1:
    print("Credit Card Number is Valid ")

elif cardtype == 'Discoverer' and sc[0] == '6' and su == 1:
    print("Credit Card Number is Valid ")
    
else:
    print("Credit Card Number is Invalid")
