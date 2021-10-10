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
    raw = input()
    lis = []
    split1 = raw.split(" ")
    calculator(int(split1[2]), int(split1[4]), split1[3])