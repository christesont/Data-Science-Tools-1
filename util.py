def util(n, power =2):

    '''
    calculates power for number up to n
    args:
        power: power for numbers to raise, default power is 2
        n: highest number in list of numbers to raise, no default
    '''
    return [i**power for i in range(n)]

print(util(10))
