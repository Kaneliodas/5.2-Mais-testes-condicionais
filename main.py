string1 =  input("Ponha uma palavra: ")
string2 =  input("Ponha uma palavra: ")
num = float(input("Ponha algum número: "))
num2 = float(input("Ponha outro número: "))
lista = ["banana","uva","cereja","laranja","limão"]
a = input("Diga uma fruta: ")
if string1 == string2:
    print("Teste de igualdade entre strings deu: ", string1 == string2)
else:
    print("Teste de diferença entre strings deu: ", string1 != string2)
    
if string1.lower == string2.lower:
    print("Teste lower() de igualdade deu:", string1.lower() == string2.lower()) 
else:
    print("Teste lower() com não igualdade (False):", string1.lower() != string2.lower())


if num == num2:
    print("São iguais.")
elif num2 > num:
    print(f"{num2} é maior ou igual que {num}")
elif num > num2:
    print(f"{num} é maior ou igual que {num2}")

if num == num2 or num2 ==num:
    print("Eles são iguais.")
elif num != num2 and num2 != num:
    print("Eles são diferentes.")
    
if a in lista:
    print("Seu pedido sairá em breve.")
else:
    print("Seu pedido não sairá.")
