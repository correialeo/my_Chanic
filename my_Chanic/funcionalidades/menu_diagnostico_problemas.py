class MenuDiagnosticoProblemas:

    def __init__(self):
        self.historico_problemas = []
    def menu_problemas(self):
        # O "bot" da boas-vindas e oferece 2 opções para o cliente
        print('Bem-vindo à Mecanik AI')
        resposta = input('Digite 1 para diagnosticar seu problema\nDigite 2 para voltar ao menu principal')

        # caso cliente queira diagnosticar o bot solicita que o usuário descreva o problema
        if resposta == '1':
            problema = input('Conte-me mais sobre o problema que você está enfrentando. Ficarei feliz em ajudar :)')
            self.historico_problemas.append(problema)

            # depois do cliente descrever o problema, "bot" simula uma árvore de decisões e dá uma solução
            problema2 = input('O carro está quente ou vazando água?')

            print("Tente colocar água no tanque d'água e veja se resolve. Caso não, retorne aqui novamente! :)")

        # caso cliente responda 2, retorna ao menu principal
        elif resposta =='2':
            return

        # caso não seja uma resposta esperada, o programa printa uma mensagem de invalidez e repete as opções ao usuário
        else:
            print('Opção inválida. Tente novamente.\n')
            self.menu_problemas()

    def historico_de_problemas(self):
        if not self.historico_problemas:
            print('Você ainda não apresentou nenhum problema para nossos serviços.')
            return

        print("HISTÓRICO DE PROBLEMAS")
        for i, problema in enumerate(self.historico_problemas):
             print(f"{i + 1}: {problema}")

        escolha_problema = input('Digite o número do problema que deseja visualizar')

        try:
            escolha_problema = int(escolha_problema) -1
            if 0 <= escolha_problema <= len(self.historico_problemas):
                problema_escolhido = self.historico_problemas[escolha_problema]
                print(f"Detalhes do problema:\n{problema_escolhido}" )
            else:
                print("Problema inexistente.")
        except ValueError:
            print("Opção inválida.")
            return