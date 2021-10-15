def multiply_list(list):
    """
    Multiply all numbers from a list.

    This function checks if the given input from the list is a number then
    multiplies all values in that list.

    Parameters
    ----------
    list: the list of values to be multiplied together

    Returns
    -------
    int
        The product of all values in the list.
    False
        The list contains an invalid item

    Examples
    --------
    >>> list = [1, 2, 3, 7]
    >>> multiply_list(list)
    42
    
    >>> list = [3, 2, 4, 89] 
    >>> multiply_list(list)
    2136

    >>> list = [3, "B", 4, 89] 
    >>> multiply_list(list)
    False
    """
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
