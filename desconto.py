preco = float(input("qual o preço do produto: "))
setor = str(input("qual o setor do produto A, B ou C: "))
cor = str(input("qual a cor da etiqueta azul, branca, verde ou preta: "))
total = float


if setor == "A":
    if cor == "azul":
        total = preco - (preco * 0.06)
        print(f"o total com desconto é R${total} ")
    elif cor == "branca":
        total = preco - (preco * 0.07)
        print(f"o total com desconto é R${total} ")
    elif cor == "verde":
        total = preco - (preco * 0.08)
        print(f"o total com desconto é R${total} ")
    elif cor == "preta":
        total = preco - (preco * 0.09)
        print(f"o total com desconto é R${total} ")
    
elif setor == "B":
    if cor == "azul":
        total = preco - (preco * 0.063)
        print(f"o total com desconto é R${total} ")
    elif cor == "branca":
        total = preco - (preco * 0.074)
        print(f"o total com desconto é R${total} ")
    elif cor == "verde":
        total = preco - (preco * 0.082)
        print(f"o total com desconto é R${total} ")
    elif cor == "preta":
        total = preco - (preco * 0.091)
        print(f"o total com desconto é R${total} ")

elif setor == "C":
    if cor == "azul":
        total = preco - (preco * 0.056)
        print(f"o total com desconto é R${total} ")
    elif cor == "branca":
        total = preco - (preco * 0.067)
        print(f"o total com desconto é R${total} ")
    elif cor == "verde":
        total = preco - (preco * 0.078)
        print(f"o total com desconto é R${total} ")
    elif cor == "preta":
        total = preco - (preco * 0.109)
        print(f"o total com desconto é R${total} ")