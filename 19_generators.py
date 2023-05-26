def generator(n=0, maximun=10):
    while True:
        yield n

        n += 1

        if n >= maximun:
            return 'end'
    
lista = (n for n in range(10000))
print('Generator by comprehension')
print(next(lista))
print(next(lista))
print(next(lista))
print()

gen = generator(n=0,maximun=5)
print('Generator by method')
print(next(gen))
print(next(gen))
print(next(gen))