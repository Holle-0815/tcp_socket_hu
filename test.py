import math
def equationroots():  
    try:
         a = int(input("Enter the coefficients of a: "))
         b = int(input("Enter the coefficients of b: "))
         c = int(input("Enter the coefficients of c: "))
    except ValueError:
         print("Not a number!")
    
    my = b * b - 4 * a * c  
    sqrt_val = math.sqrt(abs(my))
    quadratic = (-b + sqrt_val)/(2 * a) 
    return quadratic

quadratic = equationroots()
print("The equation root of the numbers is", quadratic)