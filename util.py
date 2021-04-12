def util(n, fn = lambda x: x**3):

    '''
    calculates power for number up to n
    args:
        power: power for numbers to raise, default power is 3
        n: highest number in list of numbers to raise, no default
    '''
    return [fn(i) for i in range(n)]

print(util(10))
