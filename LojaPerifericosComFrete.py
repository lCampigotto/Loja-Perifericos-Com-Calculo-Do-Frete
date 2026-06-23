print("---- BEM VINDO ----")
print("")
print("Escolha um de nossos produtos! ")

produtos = ["Mouse", "Teclados", "Mousepads", "Microfones"]
print(produtos)
print("")
escolha = input("Digite o produto aqui! : ")
print("")

mmouse = ["Logitech", "Razer"]
mteclados = ["Corsair", "Redragon"]
mmousepads = ["SteelSeries", "Zowie"]
mmicrofones = ["HyperX", "Fifine"]

Logitech = 505.00
Razer = 999.99
Corsair = 1704.55
Redragon = 326.00
SteelSeries = 283.22
Zowie = 459.99
HyperX = 1413.00
Fifine = 353.93

if escolha in produtos:
    if escolha == "Mouse":
        print(mmouse)
        print("")
        marca = input("Digite aqui a marca desejada : ")
    elif escolha == "Teclados":
        print(mteclados)
        print("")
        marca = input("Digite aqui a marca desejada : ")
    elif escolha == "Mousepads":
        print(mmousepads)
        print("")
        marca = input("Digite aqui a marca desejada : ")
    elif escolha == "Microfones":
        print(mmicrofones)
        print("")
        marca = input("Digite aqui a marca desejada : ")
    else:
        print("Sinto Muito. Não oferecemos esse produto na nossa loja. ")
else:
    print("Sinto Muito. Não oferecemos esse produto na nossa loja. ")

print("--------------------------")
print("")
if marca in mmouse:
    print("Ótima escolha")
    if marca == "Logitech":
        print(f"Mouse Logitech: R$ {Logitech} à vista! Envio para todo o Brasil!")
    elif marca == "Razer":
        print(f"Mouse Razer: R$ {Razer} à vista! Envio para todo o Brasil!")
elif marca in mteclados:
    print("Ótima escolha")
    if marca == "Corsair":
        print(f"Teclado Corsair: R$ {Corsair} à vista! Envio para todo o Brasil!")
    elif marca == "Redragon":
        print(f"Teclado Redragon: R$ {Redragon} à vista! Envio para todo o Brasil!")
elif marca in mmousepads:
    print("Ótima escolha")
    if marca == "SteelSeries":
        print(f"Mousepad Steel Series: R$ {SteelSeries} à vista! Envio para todo o Brasil!")
    elif marca == "Zowie":
        print(f"Mousepad Zowie: R$ {Zowie} à vista! Envio para todo o Brasil!")
elif marca in mmicrofones:
    print("Ótima escolha")
    if marca == "HyperX":
        print(f"Microfone HyperX: R$ {HyperX} à vista! Envio para todo o Brasil!")
    elif marca == "Fifine":
        print(f"Microfone Fifine: R$ {Fifine} à vista! Envio para todo o Brasil!")
    print("")
else:
    print("Desculpe, não temos essa marca no nosso catálogo!")

tnorte = 25
tnordeste = 20
tcentrooeste = 15
tsudeste = 10
tsul = 15

regiao = input("Digite sua região para calculo do frete : ")
if regiao == "Norte":
    if marca == "Logitech":
        pmarca = Logitech
    elif marca == "Razer":
        pmarca = Razer
    elif marca == "Corsair":
        pmarca = Corsair
    elif marca == "Redragon":
        pmarca = Redragon
    elif marca == "SteelSeries":
        pmarca = SteelSeries
    elif marca == "Zowie":
        pmarca = Zowie
    elif marca == "HyperX":
        pmarca = HyperX
    elif marca == "Fifine":
        pmarca = Fifine
    preço = pmarca + tnorte + (pmarca * 0.05)
    print(f"Valor do Item : {pmarca} / Valor total com o frete : {preço}")
elif regiao == "Nordeste":
    if marca == "Logitech":
        pmarca = Logitech
    elif marca == "Razer":
        pmarca = Razer
    elif marca == "Corsair":
        pmarca = Corsair
    elif marca == "Redragon":
        pmarca = Redragon
    elif marca == "SteelSeries":
        pmarca = SteelSeries
    elif marca == "Zowie":
        pmarca = Zowie
    elif marca == "HyperX":
        pmarca = HyperX
    elif marca == "Fifine":
        pmarca = Fifine
    preço = pmarca + tnordeste + (pmarca * 0.05)
    print(f"Valor do Item : {pmarca} / Valor total com o frete : {preço}")
elif regiao == "Centro-Oeste":
    if marca == "Logitech":
        pmarca = Logitech
    elif marca == "Razer":
        pmarca = Razer
    elif marca == "Corsair":
        pmarca = Corsair
    elif marca == "Redragon":
        pmarca = Redragon
    elif marca == "SteelSeries":
        pmarca = SteelSeries
    elif marca == "Zowie":
        pmarca = Zowie
    elif marca == "HyperX":
        pmarca = HyperX
    elif marca == "Fifine":
        pmarca = Fifine
    preço = pmarca + tcentrooeste + (pmarca * 0.05)
    print(f"Valor do Item : {pmarca} / Valor total com o frete : {preço}")
elif regiao == "Sudeste":
    if marca == "Logitech":
        pmarca = Logitech
    elif marca == "Razer":
        pmarca = Razer
    elif marca == "Corsair":
        pmarca = Corsair
    elif marca == "Redragon":
        pmarca = Redragon
    elif marca == "SteelSeries":
        pmarca = SteelSeries
    elif marca == "Zowie":
        pmarca = Zowie
    elif marca == "HyperX":
        pmarca = HyperX
    elif marca == "Fifine":
        pmarca = Fifine
    preço = pmarca + tsudeste + ( pmarca* 0.05)
    print(f"Valor do Item : {pmarca} / Valor total com o frete : {preço}")
elif regiao == "Sul":
    if marca == "Logitech":
        pmarca = Logitech
    elif marca == "Razer":
        pmarca = Razer
    elif marca == "Corsair":
        pmarca = Corsair
    elif marca == "Redragon":
        pmarca = Redragon
    elif marca == "SteelSeries":
        pmarca = SteelSeries
    elif marca == "Zowie":
        pmarca = Zowie
    elif marca == "HyperX":
        pmarca = HyperX
    elif marca == "Fifine":
        pmarca = Fifine
    preço = pmarca + tsul + (pmarca * 0.05)
    print(f"Valor do Item : {pmarca} / Valor total com o frete : {preço}")
else:
    print("Não atendemos esta região.")

