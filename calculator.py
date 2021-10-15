def calculator(x, y, op):
    result = 0
    if x.isdigit() and y.isdigit():
        if op == "+":
            result = int(x) + int(y)
        elif op == "-":
            result = int(x) - int(y)
        elif op == "*":
            result = int(x) * int(y) 
        elif op == "**":
            result = int(x) ** int(y) 
        elif op == "/":
            if y != 0:
                result = int(x) / int(y)
            else:
                return False
        elif op == "//":
            result = int(x) // int(y) 
        return result
    else:
        return False

def parse_input():
    raw = input()
    split1 = raw.split(" ")
    calculator(int(split1[2]), int(split1[4]), split1[3])