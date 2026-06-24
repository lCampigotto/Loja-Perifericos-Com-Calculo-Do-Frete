import csv
import os

print("========= BEM VINDO =========\n"
    "\n>  Escolha um de nossos produtos\n")

def leitor(caminho):
    pasta = os.path.dirname(__file__)
    caminho_completo = os.path.join(pasta, caminho)
    with open(caminho_completo) as inventario:
        return list(csv.DictReader(inventario))

def lista_produtos(par1): # LISTA DE PRODUTOS
    print("------------------------------")
    for item in par1:
        print(item['produto'], item['marca'])
        print("------------------------------")


dados = leitor("inventario.csv")
lista_produtos(dados)

escolha = input("\nEscolha um de nossos produtos! : ").lower()

# ESCOLHA NUMERO DOIS 

def escolhap2(escolha):
    print("------------------------------")
    if escolha in ["mouse", "teclado", "mousepad", "microfone"]:
        Descolha = leitor(f"{escolha}.csv")
        for item in Descolha:
            print(item[f'{escolha}'], item['marca'], "/ R$", item['valor'])
            print("------------------------------")
     

if escolha in ["mouse", "teclado", "mousepad", "microfone"]:
    escolhap2(escolha)
else:
    # busca produto específico ex: "mouse logitech"
    for item in dados:
        if escolha == item['produto'].lower() + " " + item['marca'].lower():
            print("O valor do produto escolhido é de R$", item['valor'])
            break
    else:
        print("Não possuímos este produto.")

# FRETE

escolha3 = input("\nEscolha um de nossos produtos! : ").lower()

for item in leitor(f"{escolha}.csv"):
    if escolha3 == item[f'{escolha}'] + " " + item['marca']:
        print(item['valor'])
 













tnorte = 30
tnordeste = 20
tcentrooeste = 15
tsudeste = 10
tsul = 15
