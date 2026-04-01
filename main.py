while True:
    num1 = int(input("\nDigite Primeiro Número: "))
    num2 = int(input("Digite Segundo Número: "))

    print("\nEscolha a Operação:")
    print("1- Soma")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")

    opcao = int(input("Opção: "))

    if opcao == 1:
        print(f'Resultado da Soma: {num1 + num2}')
    elif opcao == 2:
        print(f"Resultado da Subtração: {num1 - num2}")
    elif opcao == 3:
        print(f"Resultado da Multiplicação: {num1 * num2}")
    elif opcao == 4:
        if num2 == 0:
            print("Erro: Não é possível dividir por zero!")
        else:
            print(f"Resultado da Divisão: {num1 / num2}")
    else:
        print("Opção Inválida")

    
    continuar = input("\nDeseja continuar? (s/n): ")
    if continuar == 'n':
        print("Encerrando a calculadora. Até logo!")
        break 