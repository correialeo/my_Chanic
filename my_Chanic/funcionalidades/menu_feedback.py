class MenuFeedback:

    def menu_feedback(self):
        # exibe o menu de feedbacks e da as opções disponíveis para o usuário escolher
        print('----- MENU FEEDBACK -----')
        resposta = input('Digite 1 para dar feedback da última oficina que utilizou\nDigite 2 para dar feedback no aplicativo\nDigite 3 para sair')

        # caso seja 1, o programa pede a avaliação da oficina e agradece após a avaliação
        if resposta == '1':
            feedback = input('Você avalia a Oficina com 1, 2, 3, 4 ou 5 estrelas?')
            print('Maravilha! Muito obrigado pela contribuição.')

        # caso seja 2, o programa pede a avaliação do aplicativo e agradece após a avaliação
        elif resposta == '2':
            feedback = input('Você avalia a myChanic com 1, 2, 3, 4 ou 5 estrelas?')
            print('Obrigado pela avaliação! Estaremos sempre ao seu dispor.')

        # caso seja 3, o programa retorna ao menu principal
        elif resposta == '3':
            return

        # caso não seja uma resposta esperada, o programa printa uma mensagem de invalidez e repete as opções ao usuário
        else:
            print('Opção inválida. Tente novamente.\n')
            self.menu_feedback()