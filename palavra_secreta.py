
palavra_secreta = "paralelepipedo"
palavra_mascarada = ""
letras_acertadas = ""
qtd_tentativas = 0

while palavra_mascarada != palavra_secreta:
    tentativa = input("Informe uma letra: ")
    qtd_tentativas += 1

    if len(tentativa) > 1:
        print("Informe apenas uma letra.")
        continue

    if tentativa in palavra_secreta:
        letras_acertadas += tentativa

    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_mascarada += letra
        else:
            palavra_mascarada += "*"

            
    print("A palavra secreta é: ", palavra_mascarada)

    if palavra_mascarada == palavra_secreta:
        print("Parabens! Voce ganhou!")
        print("Quantidade de tentativas: ",qtd_tentativas)
        letras_acertadas = ""
        qtd_tentativas = 0
    else:
        print("Palavra Mascarada: ",palavra_mascarada)
        palavra_mascarada = ""

    

