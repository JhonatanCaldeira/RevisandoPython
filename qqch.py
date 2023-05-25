import sys

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1','3','4','5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['10','30','40','25'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['1','3','4','5'],
        'Resposta': '5'
    }
]

acerto = 0
for pergunta in perguntas:
    acertou = False
    escolha_int = None
    
    print('Pergunta: ', pergunta.get('Pergunta'))
    print('')

    for i, opcao in enumerate(pergunta.get('Opções')):
        print(f'{i}) {opcao}')

    print('')
    resposta = input('Escolha uma opção: ')


    qtd_opcoes = len(pergunta.get('Opções'))

    if resposta.isdigit():
        escolha_int = int(resposta)
    
    if escolha_int is not None:
        if escolha_int >= 0  and escolha_int < qtd_opcoes:
            if pergunta.get('Opções')[escolha_int] == pergunta.get('Resposta'):
                acertou = True

    if acertou:
        print('Acertou!')
        acerto += 1
    else:
        print('Errou')

print(f'Você acertou {acerto} de ', len(pergunta))