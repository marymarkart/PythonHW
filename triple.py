def tripler(to_triple):
    """
    Executes the parameter function 3 times

    Parameters
    ----------
    to_triple:
        The function to be executed 3 times

    Returns
    -------
    wrapper

    Examples
    --------
    if I have a method say_hi that prints "Hi!"
    >>> tripler(say_hi)
    Hi!
    Hi!
    Hi!

    """
    def wrapper():
        """
        Wrapper within tripler decorator that executes the function 3 times

        Parameters
        ----------
        None

        Returns
        -------
        Nothing

        Examples
        --------
        >>> tripler
        """
        to_triple()
        to_triple()
        to_triple()
    return wrapper