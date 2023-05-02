#Fazer um programa que pergunta ao usuário um valor em metros e imprime o correspondente em decímetros, centímetros e milímetros

metro = float(input("Digite a Metragem que deseja converter: "))
dcm =metro*10
cm = metro*100
mm = metro*1000

print(f"{metro} convertido em decimetro é: {dcm}dcm")
print(f"{metro} convertido em centimetro é: {cm}cm")
print(f"{metro} convertido em milimetro é: {mm}mm")