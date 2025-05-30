glicose = int(input("qual a quantidade de glicose no sangue em mg/dl: "))

if glicose <= 75:
    print("a glicose esta baixa")

elif glicose <= 100:
    print("a glicose esta normal")

elif glicose <= 140:
    print("a glicose esta elevada")

else:
    print("voce tem diabetes")