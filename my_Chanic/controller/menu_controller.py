# imports necessários para a classe funcionar como o esperado
from my_Chanic.funcionalidades.menu_diagnostico_problemas import MenuDiagnosticoProblemas
from my_Chanic.funcionalidades.menu_pagamento_servicos import MenuPagamentoServicos
from my_Chanic.funcionalidades.menu_feedback import MenuFeedback

def main_menu():
    # inicializa as classes importadas para permitir a utilização
    menu_diagnostico = MenuDiagnosticoProblemas()
    menu_pagamento = MenuPagamentoServicos()
    menu_feedback = MenuFeedback()

    # inicializa um loop para o menu ficar rodando até o cliente desejar sair
    executar = True
    while executar:
        # programa printa menu principal e da as opções ao cliente
        print('----- MENU PRINCIPAL -----')
        resposta = input('DIGITE 1 PARA DIAGNÓSTICOS\nDIGITE 2 PARA PAGAMENTOS\nDIGITE 3 PARA DAR FEEDBACKS\nDIGITE 4 PARA SAIR')

        # caso 1, abre o menu de diagnósticos
        if resposta == '1':
            menu_diagnostico.menu_problemas()

        # caso 2, abre o menu de pagamentos
        elif resposta == '2':
            menu_pagamento.menu_pagamento()

        # caso 3, abre o menu de feedbacks
        elif resposta == '3':
            menu_feedback.menu_feedback()

        # caso 4, ele sai do programa, colocando a condição do while como falsa
        elif resposta == '4':
            executar = False

        # caso não seja nenhum, o programa printa opção inválida e retorna para o menu principal
        else:
            print('Opção inválida. Tente novamente.\n')
            return main_menu()