def util(n, fn = lambda x: x**2):

    #changes
    return [fn(i) for i in range(n)]

print(util(10))
