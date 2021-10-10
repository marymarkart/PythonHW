def calculator(x, y, op):
    result = 0
    if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        if op == "+":
            result = int(x) + int(y)
        elif op == "-":
            result = int(x) - int(y)
        elif op == "*":
            result = int(x) * int(y) 
        elif op == "**":
            result = int(x) ** int(y) 
        elif op == "/":
            result = int(x) / int(y)
        elif op == "//":
            result = int(x) // int(y) 
        return result
    else:
        return False

def parse_input():
    raw = input("Enter equation:")
    lis = []
    split1 = raw.split(" ")
    for i in split1:
        lis.append(i)
    print(calculator(int(lis[0]), int(lis[2]), lis[1]))
    


parse_input()