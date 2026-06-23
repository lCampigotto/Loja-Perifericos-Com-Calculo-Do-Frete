import csv

print("======== BEM VINDO ========\n"
    "\n>  Escolha um de nossos produtos\n")

def leitor(caminho):
    with open(caminho) as inventario:
        return list(csv.DictReader(inventario))
    
def lista_produtos(dados):
    for item in dados:
        print("------------------------------")
        print(item['produto'], item['marca'],"/ R$", item['valor'])

dados = leitor("inventario.csv")
lista_produtos(dados)

escolha = input("\nDigite o produto aqui! : ").lower()

if escolha in dados:
    if escolha == item['produto'] + item['marca']:
        print("R$", item['valor'])
    else:
        print("Sinto Muito. Não oferecemos esse produto na nossa loja. ")
else:
    print("Sinto Muito. Não oferecemos esse produto na nossa loja. ")

tnorte = 30
tnordeste = 20
tcentrooeste = 15
tsudeste = 10
tsul = 15
