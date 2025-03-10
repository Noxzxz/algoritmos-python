velMed = int(input('Insira a velocidade media da viagem: '))
TempGast = int(input('Insira o tempo gasto na viagem em horas:'))

km = velMed*TempGast
Gas = km/10.5

print('Foram percorridos {} km e foi gasto {:.4f}L de gasolina'.format(km,Gas))