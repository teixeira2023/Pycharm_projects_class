# class User:
#     def __init__(self, id, username):
#         self.id = id
#         self.username = username


# user_1 = User("001", "Alan")
# # user_1.id = "001"
# # user_1.username = "Alan"

# print(user_1.id)
# #
# user_2 = User("002","Janete")
# # # user_2.id = "002"
# # # user_2.username = "Janete"
# #
# print(user_2.id, user_2.username)


def calcular_imposto(valor, perc_ir):
    ir = valor * perc_ir
    iss = valor * 0.05
    csll = valor * 0.0375
    pis = valor * 0.03
    return ir + iss + csll + pis


print(calcular_imposto(8500, 0.275))


def calcularImposto(valor, *args):
    total_imposto = 0
    for item in args:
        total_imposto += valor * item
    return total_imposto


print(calcularImposto(1000, 0.275, 0.05, 0.0375, 0.03))

lista_imposto = {
    "perc_iss": 0.05,
    "perc_csll": 0.0375,
    "perc_ir": 0.275,
    "perc_pis": 0.03,
}


def calcular_imposto_tri(valor, **kwargs):
    total_imposto = 0
    if "perc_iss" in kwargs:
        total_imposto += valor * kwargs["perc_iss"]
    if "perc_csll" in kwargs:
        total_imposto += valor * kwargs["perc_csll"]
    if "perc_ir" in kwargs:
        total_imposto += valor * kwargs["perc_ir"]
    if "perc_pis" in kwargs:
        total_imposto += valor * kwargs["perc_pis"]
    return total_imposto


print(
    calcular_imposto_tri(
        1000, perc_iss=0.05, perc_csll=0.0375, perc_ir=0.275, perc_pis=0.03
    )
)
print(lista_imposto)
