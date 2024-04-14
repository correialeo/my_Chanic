class MenuFeedback:
    def menu_feedback(self):
        # exibe o menu de feedbacks e da as opções disponíveis para o usuário escolher
        print('----- MENU FEEDBACK -----')
        resposta = input(
            'Digite 1 para dar feedback da última oficina que utilizou\nDigite 2 para dar feedback no aplicativo\nDigite 3 para sair')

        # inicializa um dicionário para facilitar a leitura do código
        feedback_msg = {
            '1': {
                '1': 'Puxa, que pena. Espero que tenha uma melhor próxima experiência.',
                '2': 'Puxa que pena. Obrigado pelo feedback.',
                '3': 'Obrigado pelo seu feedback!',
                '4': 'Ficamos felizes! Obrigado pelo seu feedback!',
                '5': 'Que maravilha! Obrigado pelo feedback.',
                'default': 'Opção inválida.'
            },
            '2': 'Em breve você poderá avaliar pelo aplicativo!',
            '3': 'Saindo do menu. Até logo!'
        }

        # se resposta fornecida coincidir com algum item do dicionário, é válido
        if resposta in feedback_msg:

            # se resposta for 1, programa pergunta a avaliação
            if resposta == '1':
                feedback = input('Você avalia a Oficina com 1, 2, 3, 4 ou 5 estrelas?')

                # verifica se a avaliação fornecida está presente como uma chave no dicionário e printa a mensagem
                # padrão que está associada a resposta no dicionário
                if feedback in feedback_msg[resposta]:
                    print(feedback_msg[resposta][feedback])

                # se o feedback não existir no dicionário, ele imprime o item padrão definido default
                else:
                    print(feedback_msg[resposta]['default'])

            # se resposta nao for igual a 1, usuário selecionou outra opção e programa printa a rsposta associada
            else:
                print(feedback_msg[resposta])

        # se não houver uma associação no dicionário, programa printa erro
        else:
            print('Opção inválida. Tente novamente.')