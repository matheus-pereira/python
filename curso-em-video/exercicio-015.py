dias = int(input('Digite a quantidade de dias: '))
km = float(input('Digite a quantidade de km percorridos: '))
total = dias * 60 + km * 0.15
print('Total a pagar: {:.2f}'.format(total))
