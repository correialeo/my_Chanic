class MenuDiagnosticoProblemas:
    def menu_problemas(self):
        # O "bot" da boas-vindas e oferece 2 opções para o cliente
        print('Bem-vindo à Mecanik AI')
        resposta = input('Digite 1 para diagnosticar seu problema\nDigite 2 para voltar ao menu principal')

        # caso cliente queira diagnosticar o bot solicita que o usuário descreva o problema
        if resposta == '1':
            problema = input('Conte-me mais sobre o problema que você está enfrentando. Ficarei feliz em ajudar :)')

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