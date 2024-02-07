print ("hello world")
var = 10
print (var)

#! loop
numbers = [1,2,3,4,5]

for number in numbers:
    print (number)


age = 18
if age>21:
    print("adult")
else:
    print("kid")
    
    
    #! var
    x = 1
    y = 2
    sum = x + y
    print (sum)
    
    #! def=define(a function)
def great(name):
        return "hello"+name
    
result= great("adrian")
print(result)


def power(base, exponent=2):
    return base**exponent
result=power(2)
result2=power(3,3)

print(result)
print(result2)

def multiply(number1,number2):
    multiplyResult=number1*number2
    return multiplyResult

product = multiply(12,12)
print(product)
