print("Calculator")
num1 = int(input("Enter First Number"))
num2 = int(input("Enter Second Number"))

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

add = add(num1,num2);
sub = sub(num1,num2);
mul = mul(num1,num2);
div = div(num1,num2);

print("Additoion is ",add)
print("Subtraction is ",sub)
print("Multiplication is ",mul)
print("Division is ",div)