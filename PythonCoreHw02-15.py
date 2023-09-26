result = None
operand = None
operator = None
wait_for_number = True
while True :
    entry = input(">>>")
    
    if entry == '=' :
        print(result)
        break
    
    if wait_for_number :
        try:
            operand = int(entry)
            wait_for_number = False
        except ValueError:
            print("Not a number. Try again")
            continue
    else:
        if entry in ("+", "-", "/", "*"):
            operator = entry
            wait_for_number = True
        else:
            print("Not \'+\' or \'-\' or \'*\' or \'*\'. Try again")
            continue
    
    if not result:
        result = operand
        operand = None
        continue
    
    if operand and operator:
        if operator == "+":
            result += operand
        if operator == "-":
            result -= operand
        if operator == "*":
            result *= operand
        if operator == "/":
            result /= operand
        operand = None
        operator = None
