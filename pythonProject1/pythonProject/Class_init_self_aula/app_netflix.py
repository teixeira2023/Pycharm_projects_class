# criar uma classe para Clientes da Netflix

class Cliente:
    def __init__(self, nome, email, plano, assinatura):
        self.nome = nome
        self.email = email
        self.plano = plano
        self.assinatura = assinatura
        self.lista_de_planos = ['Basic', 'Premium', 'Gold']
        if plano in self.lista_de_planos:
            self.plano = plano
        else:
            invalid_plan_message = f'Invalid plan. Please try again. Available plans are: {self.lista_de_planos}'
            raise Exception(invalid_plan_message)

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_de_planos:
            self.plano = novo_plano
        else:
            invalid_plan_message = f'Invalid plan. Please try again. Available plans are: {self.lista_de_planos}'
            raise Exception(invalid_plan_message)

    def ver_filmes(self,filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Cliente aprovado para ver o filme: {filme}')
        elif self.plano == 'Gold':
            print(f'Cliente aprovado para ver o filme: {filme}')
        elif self.plano == 'Basic' and plano_filme != 'Basic':
            print(f'Filme: {filme} está indisponível para o plano {self.plano}')
        elif self.plano == 'Premium' and plano_filme == 'Gold':
            print(f'Filme: {filme} está indisponível para o plano {self.plano}')
        else:
            print('Plano indisponível')

cliente = Cliente('Vitor', 'vitor@email', 'Basic', '2022-09-01')
# print(cliente.nome)
# print(cliente.plano)
# print(cliente.assinatura)
# print(cliente.lista_de_planos)
cliente2 = Cliente('Biruleibe', 'xuxu@email', 'Basic', '2015-12-01')
print(cliente2.nome)
print(cliente2.plano)
print(cliente2.assinatura)
print(cliente2.lista_de_planos)

cliente2.mudar_plano('Premium')
print(f'cliente2: {cliente2.nome} Novo plano: {cliente2.plano}') # print(cliente2.nome)
print(cliente2.plano)
cliente2.ver_filmes('Casa de papel', 'Gold')
cliente2.mudar_plano('Gold')
print(f'cliente2: {cliente2.nome} Novo plano: {cliente2.plano}') # print(cliente2.plano)
cliente2.ver_filmes('Casa de papel', 'Gold')