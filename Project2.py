def get_number(number):
    while True:
        Operand = input("number "+ str(number) + ":")
        try:
            return float(Operand)
        except:
            print("invalid Number. Try Again.")

        
Operand = get_number(1)
Operand2 = get_number(2)
Sign = input( "sign : ")

result = 0
if Sign == "+":
     result = float(Operand) + float(Operand2)
elif Sign == '-':
        result = float(Operand) - float(Operand2)
elif Sign == '/':
    if float(Operand2) != 0:
         result = float(Operand) / float(Operand2) 
    else:
            print("Division by Error")
elif Sign == '*':
    result =float(Operand) * float(Operand2)
else:
     print("Invalid sign.")
     

print(result)


