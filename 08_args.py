def multiplicacao(*args):
    total = 1
    for i in args:
        total *= i

    return total

def verifica_par_ou_impar(num):
    if (num%2 == 0):
        return 'par'
    else:
        return 'impar'

total = multiplicacao(1,5,7,9,3,6,3,7)
print(f'Total: {total}')

print(verifica_par_ou_impar(total))