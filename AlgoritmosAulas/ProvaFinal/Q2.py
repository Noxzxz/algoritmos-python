#variavel sete como controlador
sete = 2

sens1 = [0]*sete
sens2 = [0]*sete

def Entrada(a):
    return int(input("Insira a precipitação da {} semana:".format(a+1)))



print("Sensor 1\n----------------------")
for i in range(0,sete):
    sens1[i] = Entrada(i)
print("Sensor 2\n----------------------")
for i in range(0,sete):
    sens2[i] = Entrada(i)
    
def mediaDia(a,b):
    # a -> sensor1 b -> sensor2
    ListaMedia = []
    for i in range(0,sete):
        ListaMedia.append((a[i]+b[i])/2)
    return ListaMedia

def MediaSemana(a):
    # a -> listaMedia
    ValorSemana=0
    for i in range(0,sete):
        ValorSemana+=a[i]
    ValorSemana = ValorSemana/sete
    return ValorSemana

def totAcumulado(a):
    # a -> ValorSemana
    if(ValorSemana<=100):
        txtAlert = "Sem alerta"
    if(ValorSemana>=101 and ValorSemana<=200):
        txtAlert = "Alerta amarelo"
    if(ValorSemana>=201 and ValorSemana<=300):
        txtAlert = "Alerta laranja"
    if(ValorSemana>300):
        txtAlert = "Alerta vermelho"
    return print(txtAlert)

ListaMedia = mediaDia(sens1,sens2)
print("Media diaria\n--------------------")
for i in range(0,sete):
    print("{}° dia -->{:.0f}".format(i+1,ListaMedia[i]))

ValorSemana = MediaSemana(ListaMedia)
totAcumulado(ValorSemana)

