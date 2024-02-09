import time
import webbrowser

def dar_dica_nome():
    print("Dica: O nome começa com a letra 'J', um 'H', dois 'N'...")

def dar_dica_conta():
    print("Dica: A operação escolhida deve ser maior que 0 e menor que 10")

def desafio_jhonny_five():
    while True:
        nome_correto = "Jhonny"
        resultado_esperado = 5

        nome_usuario = input("Digita o nome corretamente: ")

        if nome_usuario.lower() == nome_correto.lower():
            print("Nome correto! Agora vamos para o próximo desafio.")
            print("Tens 10 segundos para responder à próxima pergunta.")

            start_time = time.time()
            num1 = int(input("Digita o primeiro número: "))
            operador = input("Digita o operador matemático (+, -, *, /): ")
            num2 = int(input("Digita o segundo número: "))
            end_time = time.time()

            tempo_restante = 10 - (end_time - start_time)
            if tempo_restante <= 0:
                print("Tempo esgotado! Desafio incompleto.")
                continuar_jogo = input("Desejas jogar novamente? (S/N): ").upper()
                if continuar_jogo != "S":
                    break
                else:
                    continue

            if operador == "+":
                resultado = num1 + num2
            elif operador == "-":
                resultado = num1 - num2
            elif operador == "*":
                resultado = num1 * num2
            elif operador == "/":
                if num2 == 0:
                    print("Divisão por zero não é permitida.")
                    continue
                else:
                    resultado = num1 / num2
            else:
                print("Operador inválido.")
                continue

            if resultado == resultado_esperado:
                print("Parabéns! Descobris-te o Jhonny Five!")
            else:
                print("Resultado incorreto. Desafio incompleto.")
            break
        else:
            print("Nome incorreto.")
            if input("Desejas uma dica para o nome? (S/N): ").upper() == "S":
                dar_dica_nome()
            print("Desafio terminado.")
            continuar_jogo = input("Desejas jogar novamente? (S/N): ").upper()
            if continuar_jogo != "S":
                break

    conhecer_jhonny_five = input("Gostarias de conhecer o Jhonny Five? (S/N): ").upper()
    if conhecer_jhonny_five == "S":
        webbrowser.open("https://johnny-five.io/")

    conhecer_criador = input("Gostarias de conhecer o criador deste jogo? (S/N): ").upper()
    if conhecer_criador == "S":
        webbrowser.open("https://github.com/Alexffb32/jhoony_five")

    print("Obrigado por jogar! Até a próxima!")

desafio_jhonny_five()
