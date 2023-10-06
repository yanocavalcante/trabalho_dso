from views.telaprincipal import TelaPrincipal


class CtrlPrincipal:
    def __init__(self):
        self.__ctrlnotas = CtrlNotas()

    def mostra_tela_principal(self):
        tela = TelaPrincipal()
        op = tela.opcoes_do_sistema()
        self.processa_input(op)

    def mostra_tela_notas(self):
        pass

    def mostra_tela_cadastros(self):
        pass

    def mostra_tela_financeiro(self):
        pass

    def processa_input(self,op):
        if op == 1:
            self.mostra_tela_notas()
        elif op == 2:
            self.mostra_tela_cadastros()
        elif op == 3:
            self.mostra_tela_financeiro()