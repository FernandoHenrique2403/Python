#Desenvolva um programa em Python que receba o valor do raio de uma circunferência e calcule a área. Fórmula: (pi x r²) considerando o PI como uma constante 3,1415
raio = float(input("Digite o raio da circunferencia em cm "))
pi = 3.1415

def circulo(a,b):
    area = b*(a**2)
    print(f"A área é {area}cm²")

circulo(raio,pi)