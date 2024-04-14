class MenuPagamentoServicos:
    def menu_pagamento(self):

        # exibe o menu de pagamentos e verifica se o usuário quer ou não pagar a conta agora
        print('Menu de Pagamentos')
        resposta = input('Olá, você possui contas em aberto. Deseja efetuar o pagamento agora? (S/N)')

        # estrutura condicional que verifica a resposta do usuário
        # caso sim, o programa retorna a função efetuar_pagamento, fazendo a simulação de pagamento
        if resposta.upper() == "S":
            forma_pgto = input('Deseja pagar com cartão ou pix?')
            return self.efetuar_pagamento()
        # caso nao, o programa printa uma mensagem aconselhando a pagar antes do vencimento e retorna ao menu principal
        elif resposta.upper() == "N":
            print('Certo. Aconselhamos a fazer o pagamento antes do vencimento da conta. Até logo! :)')
            return
        # caso não seja nenhuma das que esperamos, o programa printa que a opção é inválida
        # e volta ao menu de pagamento, perguntando novamente se o usuário quer pagar ou não
        else:
            print('Opção inválida. Tente novamente.\n')
            self.menu_pagamento()

    # função que simula um pagamento
    def efetuar_pagamento(self):
        print('Efetuando pagamento dos serviços...')