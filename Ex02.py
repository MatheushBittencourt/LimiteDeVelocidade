velocidade = int(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade<=80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h \n '
          'Você deve pagar uma multa de R${}.00'.format(multa))

