def soma(x, y):
    """Soma x e y

    >>> soma(10, 20)
    30

    >>> soma(-10, 20)
    10

    >>> soma(1.5, 2,5)
    4
    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x + y

def subtrai(x, y):
    """Subtrai x e y

    >>> subtrai(10, 5)
    5

    >>> subtrai(30, 15)
    15
    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x - y


if name == '__main__':
    import doctest
    doctest.testmod(verbose=True)
