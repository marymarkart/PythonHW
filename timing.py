import time

def calculate_time(func):
    """
    Calculates the time spent executing a function

    Parameters
    ----------
    func:
        The function to be executed that were want the execution time of

    Returns
    -------
    wrapper

    Examples
    --------
    >>> calculate_time(time.sleep(2))
    2

    """
    def wrapper():
        """
        Wrapper within calculate_time decorator that executes the function
        and calculates the time spent executing a function

        Parameters
        ----------
        None

        Returns
        -------
        Nothing

        Examples
        --------
        >>> calculate_time(time.sleep(2))
        2
        """
        start_time = time.time()
        func()
        end_time = time.time()
        run = end_time - start_time
        print(f'Total time {run}')
    return wrapper
