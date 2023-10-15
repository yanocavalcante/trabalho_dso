class TelaNotas:

    def mostra_tipo_notas(self):
        print('NOTAS')
        print('1 - Saída        2 - Entrada        3 - Retornar')
        op = int(input())
        return op

    def listagem_produtos(self):
        produtos = []
        print('PRODUTOS')
        while True:
            nome = input('Nome:')
            qnt = int(input('Quantidade:'))
            produto = {'nome': nome, 'qnt': qnt}
            produtos.append(produto)
            print('1 - Adicionar Produto        2 - Finalizar')
            act = int(input())
            if act == 2:
                break
        return produtos

    def input_notaSaida(self):
        print('NOTA DE SAÍDA')
        cliente = input('Cliente:')
        produtos = self.listagem_produtos()
        return cliente, produtos

    def input_notaEntrada(self):
        print('NOTA DE ENTRADA')
        fornecedor = input('Fornecedor:')
        produtos = self.listagem_produtos()
        return fornecedor, produtos
        