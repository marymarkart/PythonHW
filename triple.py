def tripler(to_triple):
    def wrapper():
        to_triple()
        to_triple()
        to_triple()
    return wrapper