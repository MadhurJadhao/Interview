# Write a Python program that returns a string that is n 
# (non-negative integer) copies of a given string.
#sol:-
"""def Lar_Str(text, n):
    result = " "
    for i in range(n):
        result = result + text
    return result
    
print(Lar_Str('abc', 2))
print(Lar_Str('.test', 3))"""
#######################################################################

# Python: How to check if a number is odd or even?
#sol:-

"""num = int(input("Enter a Number:- "))
mod = num % 2
if mod > 0:
    print("This Number Is An Odd Number....")
else:
    print("This Number is Even Number.....")"""
####################################################################

# Write a Python program that will accept the base and height of a triangle and compute its area.
#sol:-
"""b = int(input("Enter The Base :- "))
h = int(input("Enter A height:- "))
area = b*h/2
print("Area is:- ",area)"""
###################################################################################################################

# Write a Python program to find the least common multiple (LCM) of two positive integers.
# sol:-
"""def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y 
    
    while(True):
        if((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1
    return lcm
print(lcm(4, 6))
print(lcm(15, 17))   """  
########################################################################################################################

# Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
# sol:-

"""def sum_three(x ,y, z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z
    return sum

print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(8, 2, 8))    
    """
####################################################################################################################

# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
#sol:-
"""def sum(x, y):
    sum = x + y
    if sum in range (15, 20):
        return 20
    else:
        return sum

# print(sum(10, 5))
# print(sum(15, 2))
"""
##########################################################################################################################

# Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
#sol:-
"""def test_number5(x, y):
    if x == y or abs(x - y) or (x + y):
        return True
    else:
        return False


print(test_number5(7, 2))
print(test_number5(3, 2))
"""
##########################################################################################################################
# Write a Python program to add two objects if both objects are integers.
#sol:-
"""def add_number(x, y):
    if not(isinstance(x, int) and isinstance(y, int)):
        return "Inputs Must Be Interger..!"
    return x + y

print(add_number(10,20))
print(add_number('1',20))"""
##########################################################################################################################

# Write a Python program that displays your name, age, and address on three different lines.
#sol:-
"""def personal_details():
    name = 'kartik'
    age = 19
    address = 'pune'
    print("Name: {}\n Age: {}\n Address: {}".format(name,age,address))
    
    
personal_details()    """
##################################################################################################################









