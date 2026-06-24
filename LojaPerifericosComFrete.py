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
    Descolha = leitor(f"{escolha}.csv")
    for item in Descolha:
        print(item[f'{escolha}'], item['marca'], "/ R$", item['valor'])
        print("------------------------------")  

if escolha in ["mouse", "teclado", "mousepad", "microfone"]:
    escolhap2(escolha)
else:
    print("Não possuímos este produto.")

# Mostra Valor, e oende região

escolha3 = input("\nEscolha um de nossos produtos! : ").lower()


for item in leitor(f"{escolha}.csv"):
    if escolha3 == item[f'{escolha}'].lower() + " " + item['marca'].lower():
        print("O produto escolhido possui o valor de R$", item['valor'])
        valorcompra = float(item['valor'])
else:
    print("Não possuímos este produto.")

# Calculo frete
fretes = {
    "norte": 30,
    "nordeste": 20,
    "centro oeste" : 15,
    "sudeste" : 10,
    "sul" : 15,
}

regiao = input("Digite a região do destinatário : ").lower()

if regiao in ["norte", "nordeste", "centro oeste", "sudeste", "sul"]:
    taxaFrete = fretes[regiao]
    ValorTotal = valorcompra + taxaFrete
    print(f"\nO valor do produto é de R$ {valorcompra}  |  O valor do frete para sua região é de R$ {taxaFrete}  |  E o Valor total é de R$ {ValorTotal}")  
    print("\n======== FIM DO ATENDIMENtO ========")
else:
    print("Não atendemos esta região")
