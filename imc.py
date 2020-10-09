jornada Faixa PReta bylearn.... 

def numero_quadrado(numero):
    quadrado = numero * numero

    return quadrado

def calcular_imc(peso, altura):
    altura_quadrada = numero_quadrado(altura)
    meu_imc = peso / altura_quadrada

    return meu_imc

peso = float(input('Difgite o seu Peso: '))
altura = float(input('Digite a sua altura: '))
imc = calcular_imc(peso, altura)

def classificar_imc(meu_imc):
  if imc < 18.5:
    print('Sua classificação é: Magreza')
  elif imc >= 18.5 and imc < 25:
    print('Sua classificação é: Normal')
  elif imc >= 25 and imc < 30:
    print('Sua classificação é: Sobrepeso')
  elif imc >= 30 and imc < 40:
    print('Sua classificação é: Obesidade')
  else:
    print('Sua classificação é: Obesidade Grave')

print('Seu IMC é:', imc)

classificar_imc(imc)