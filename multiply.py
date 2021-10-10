def multiply_list(list):
    product = 1
    for x in list:
        if isinstance(x, int):
            product*=x
        elif isinstance(x, float):
            product*=x
        else:
            return False
    else:
        return product
    
y = [1, 2, 3, 7]

z = multiply_list(y)
print(z)

a = [3, 2, 4, 8.9]
b = multiply_list(a)
print(b)
f = [3, "d", 6]
g = multiply_list(f)
print(g)