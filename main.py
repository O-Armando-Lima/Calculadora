import math

def somar ( a , b ):
    return a + b

def diminuir ( a, b ):
    return a - b

def multiplicar ( a, b ):
    return a * b

def dividir ( a, b ):
    return a / b

while True:

    print("====================\n")
    print("    Calculadora\n")
    print("====================\n")

    print("Escolha uma opção:\n")

    print("1. Somar\n")
    print("2. Subtrair\n")
    print("3. Multiplicar\n")
    print("4. Dividir\n")
    print("5. Potência\n")
    print("6. Fatorial\n")
    print("7. Raiz Quadrada\n")
    print("8. Logaritmo\n")
    print("9. Trigonometria\n")
    print("10. Sair\n")

    try:
        opcao = int(input("Digite qual opção você quer? "))

        if opcao < 1 or opcao > 10:
             print("Digite uma entrada válida. Tente novamente.\n")
             continue
    except ValueError:
        print("Digite uma opção numérica válida.\n")
        continue

    if opcao >= 1 and opcao < 5:
        try:
            num1 = float(input("\nDigite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Digite números válidos.\n")
            continue

        if not math.isfinite(num1) or not math.isfinite(num2):
            print("Por favor, insira números válidos.\n")
            continue
        
        match opcao:
                    case 1:
                        print(f"A soma entre esses dois números é {somar( num1, num2 )}.\n")
                    case 2:
                        print(f"A subtração entre esses dois número é {diminuir( num1, num2 )}.\n")
                    case 3:
                        print(f"O produto entre esses dois números é {multiplicar( num1, num2 )}.\n")
                    case 4:
                        if num2 == 0:
                             print("Não se pode dividir por 0. Tente novamente.\n")
                             continue
                        print(f"A divisão entre esses dois número é {dividir( num1, num2 )}.\n")

    elif opcao == 5:
        try:
            num1 = float(input("Digite a base: "))
            num2 = float(input("Digite o expoente: "))
        except ValueError:
            print("Entrada inválida.")
            continue

        if not math.isfinite(num1) or not math.isfinite(num2):
            print("Digite números finitos.")
            continue

        try:
            resultado = math.pow(num1, num2)

        except ValueError:
            print("Não é possível calcular essa potência nos números reais.\n")

        except OverflowError:
            print("O resultado dessa potência é grande demais.\n")

        else:
            print(f"O resultado dessa potência é {resultado}.\n")
        
    elif opcao == 6:
        try:
            num = int(input("Você quer calcular o fatorial de qual número? "))
            if num < 0:
                    print("Entrada inválida. Tente de novo.\n")
                    continue
        except ValueError:
                print("Entrada inválida. Tente novamente.\n")
                continue
        else:
            print(f"O fatorial deste número é {math.factorial( num )}.\n")

    elif opcao == 7:
            try:
                num = float (input ("Você quer a raiz quadrada de qual número? ") )
                if num < 0:
                     print("Entrada inválida. Tente de novo.\n")
                     continue
            except ValueError:
                 print("Sua entrada não é válida. Tente de novo. \n")
                 continue
            else:
                if not math.isfinite(num):
                    print("Entrada inválida. Tente novamente.\n")
                    continue
                else:
                    print(f"A raiz quadrada desse número é {math.sqrt( num )}.\n")

    elif opcao == 8:
        try:
            valor = float(input("Você quer calcular o log de qual número? "))
            base = float(input("Em qual base? "))
        except ValueError:
            print("Você teve uma entrada inválida. Tente novamente.\n")
            continue
        else:
            if valor <= 0 or base == 1 or base <= 0 or ( not math.isfinite(valor) or not math.isfinite(base)):
                print("Entrada inválida para logaritmo.\n")
                continue  
            else:
                print(f"O log de {valor} na base {base} é {math.log( valor, base )}") 

    elif opcao == 9:
        while True:
            print("\nEscolhas possíveis:\n")
            print("1. Seno\n")
            print("2. Cosseno\n")
            print("3. Tangente\n")
            print("4. Sair\n")

            try:
                escolha = int(input("Qual razão trigonométrica você quer? "))
            except ValueError:
                print("Entrada inválida. Tente novamente.\n")
                continue
            else:
                 try:
                      if escolha < 1 or escolha > 3:
                        print("Opção inválida.")
                        continue
                      graus = float(input("Você quer essa razão trigonométrica para qual grau? "))
                 except (ValueError, OverflowError):
                      print("Valor impróprio. Por favor, coloque um valor válido.\n")
                 else:
                    if not math.isfinite(graus):
                        print("Ângulo inválido.")
                        continue
                    graus = graus % 360
                    radiano = math.radians(graus)

                    match escolha:
                        case 1:
                            if graus % 360 == 0:
                                print("O seno desse grau é de 0.\n")
                                break
                            else:
                                print(f"O seno desse grau é {math.sin( radiano ):.2f}.\n")
                                break
                        case 2:
                            if graus == 90 or graus == 270:
                                print("O cosseno desse grau é de 0.\n")
                                break
                            else:
                                print(f"O cosseno desse grau é {math.cos( radiano ):.2f}.\n")
                                break
                        case 3:
                            if graus == 0 or graus == 180 or graus == 360:
                                print("A tangente desse grau é de 0.\n")
                                break
                            elif math.isclose(math.cos(radiano), 0, abs_tol=1e-12):
                                print("A tangente não está definida, tente de novo,\n")
                                continue
                            else:
                                print(f"A tangente desse grau é {math.tan( radiano ):.2f}.\n")
                                break
                        case 4:
                            print("Obrigado por utilizar a calculadora, volte sempre.\n")
                            break

    elif opcao == 10:
        print("\nObrigado por usar a calculadora, até a próxima!\n")
        break

    try:
        decisao = input("Deseja fazer mais alguma operação? (s/n) ")
    except (EOFError, KeyboardInterrupt):
         print("Você forneceu uma entrada inválida, tente de novo.\n")
         continue
    else:         
        if decisao == 'n' or decisao == 'N':
            print("\nObrigado por usar a calculadora, até a próxima!")
            break
        elif decisao == 's' or decisao == 'S':
            continue
        else:
             print("Você digitou uma entrada inválida. Tente de novo.\n")
             continue