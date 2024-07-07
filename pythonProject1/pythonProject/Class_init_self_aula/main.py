class ControleRemoto:
    def __init__(self, cor, altura, largura, profundidade, volume):
        self.cor = cor
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade
        self.volume = volume

    def change_channel(self, channel):
        valid_channels = {"+", "-"}
        if channel in valid_channels:
            print(f"{'Increase' if channel == '+' else 'Decrease'} channel")
        else:
            print("Invalid channel")

    # metodos de controle remoto:
    # - mudar de canal
    # - mudar_volume
    # - aumentar_volume
    # - diminuir_volume
    # - ligar_desligar


# def passar_canal(self, canal):
#     if canal =="+":
#         print("aumentar canal")
#     elif canal =="-":
#         print("diminuir canal")
#     else:
#         print("canal invalido")



controle_remoto = ControleRemoto('preto', "10cm", "2cm", "3cm", 4)
controle_remoto_2 = ControleRemoto('prata', "11cm", "3cm", "3cm", 10)
print(controle_remoto.volume)
controle_remoto.change_channel('+')
print(controle_remoto_2.volume)
controle_remoto_2.change_channel('-')



