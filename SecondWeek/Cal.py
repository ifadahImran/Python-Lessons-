def add (in1, in2):
    return in1+in2

def sub (in1, in2):
    return in1-in2

def mul (in1, in2):
    return in1*in2

def dev (in1, in2):
    return in1/in2

in1= float (input ("Enter your 1st value: "))
in2= float (input("Enter your 2nd value: "))

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

ope=int(input("Enter Operator(Addition, Subraction, Multiplication, Devision)"))

if ope ==1:
    print("Answer = ", add(in1, in2))

elif ope==2:
    print("Answer = ", sub(in1, in2))

elif ope==3:
    print("Answer = ", mul(in1, in2))

elif ope==2:
    print("Answer = ", dev(in1, in2))

else:
    print("Invalid Input")
