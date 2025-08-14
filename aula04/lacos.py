# sistema de calculo de indice de massa (IMC)
'''
-Crie um sistema que calcule o indice de massa corporal do usuario, mostre o valor do IMC na tela,
e retorne se o usuario esta no peso ideal ou se precisa emagrecer ou engordar mais. Utilize a tabela do IMC para definir os valores.
'''
# tabela de classificação 
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 24.9: Peso normal
# Entre 25 e 29.9: Sobrepeso
# Acima de 30: Obesidade

# calculo IMC
# IMC = peso / (altura *altura) 
print(40*'-','CALCULADORA DE IMC',40*'-')
nome = input("Digite seu nome: ")
peso = float(input('Digite seu peso: ').replace(',', '.'))
altura = float(input('Digite sua altura: ').replace(',', '.'))
IMC = peso / (altura * altura)
print(f'seu IMC é:{IMC:.2f}')

if IMC <= 18.5:
  print('abaixo do normal') 
elif IMC <= 24.9:
  print('normal')
elif IMC <=29.9:
  print('soberano')
elif IMC <= 34.9:
  print('obesidade grau 1')
elif IMC <= 39.9:
  print('obesidade grau 2')
else:
  print('obesidade grau 3')

  '''
  problema 2: um elevador de carga possui capacidade para 200kg. 
  Crie um programa que recaba do usuario seu peso e o peso da carga e verifica se a carga está autorizada a usar elevador ou não.s
  '''
  peso_usuario = float(input("informe seu peso:").replace(",","."))
  peso_carga = float(input("informe seu peso").replace(",","."))
  peso_total = (peso_usuario+peso_carga)
  if peso_total >200:
    print("peso excedente, você não está autorizado a usar o elevador")
  else:
   print("você está autorizado a subir")

while True:
          print(40*'-','Sistema console 2° DS',40*'-')
          print('1 - Calculadore IMC')
          print('2 - Maioridade')
          print('3 - Calculadora')
          print('4 - Dados pessoais')
          print ('5 - Sair')

          opcao = input('Digite uma opcao:')
          if opcao == '1':
               pass
          elif opcao == '2':
               pass
          elif opcao == '3':
               ...
          elif opcao == '4':
               ...
          elif opcao == '5':
               linhas = 6
               i = 1

               while i<= linhas:
                    espacos = linhas - i
                    estrelas = 2 * j - j

                    print("" * espacos + "" * estrelas )
                    j + 1

          elif opcao == "6":
              print("saindo do sistema!")
              break
          else:
              print("opcao invalida!")
    
 

while true:
    print("calculadora")
    print("1 - soma")
    print("2 - divisao")
    print("3 - subtracao")
    print("4 - multiplicacao")
    print("5 - sair")

    opcao_calculo = input('escolha uma operaçao matematica')
    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o segundo numero:"))