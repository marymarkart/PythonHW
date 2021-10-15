def calculator(x, y, op):
    """
    Perform the arithmetic operation "op" on x and y.

    Parameters
    ----------
    x : the first operand
    y : the second operand
    op : the arithmetic operation to be performed

    Returns
    -------
    int
        The result of the arithmetic operation, op, on x and y
    False
        A value is invalid

    Examples
    --------
    >>> calculator(4, 5, "+")
    9
    
    >>> calculator(12, 4.2, "*")
    50.400000000000006

    >>> calculator(10, 2, "**")
    100

    >>> calculator('hello', 2, "**")
    False

    """
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
    """
    Parses the user input for x, y, and op to be used in calculator(x, y, op)
    The user input is split into a list seperated by " "
    Values from the list are then used in calculator()

    Parameters
    ----------
    None

    Returns
    -------
    Nothing

    Examples
    --------
    >>> parse_input()
    >>> raw = input()
    "Enter equation: 10 + 11"
    >>> raw.split(" ")
    split1 = ["Enter", "equation:", "10", "+", "11"]
    >>> calculator("10", "11", "+") 

    """
    raw = input()
    split1 = raw.split(" ")
    calculator(split1[2], split1[4], split1[3])