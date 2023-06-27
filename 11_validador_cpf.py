

def calcula_digito_verificador(cpf, digito_a_verificar='segundo'):
    cpf_nove_digitos, cpf_dois_digitos = cpf.split('-')
    cpf_nove_digitos = cpf_nove_digitos.replace('.', '')

    if (digito_a_verificar != 'primeiro'):
        primeiro_digito = calcula_digito_verificador(cpf, 'primeiro')
        contador_regressivo = 11
        cpf_a_validar = cpf_nove_digitos + str(primeiro_digito)
        digito_verificador = cpf_dois_digitos[1]
    else:
        contador_regressivo = 10
        cpf_a_validar = cpf_nove_digitos
        digito_verificador = cpf_dois_digitos[0]

    soma_cpf = 0
    for digito in cpf_a_validar:
        soma_cpf += int(digito) * contador_regressivo
        contador_regressivo -= 1

    digito_calculado = digito_verificador if (soma_cpf * 10) % 11 <= 9 else '0'

    print('Func: ', digito_calculado)
    return digito_calculado


cpf = '161.352.630-05'
cpf = '338.905.070-18'

calcula_digito_verificador(cpf, 'segundo')


###############################################################
