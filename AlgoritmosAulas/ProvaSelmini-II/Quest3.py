i=1
Votos = []
contVotos = 0
while (i != 0):
    i = int(input("Qual o melhor Sistema Operacional para uso em servidores?\nAs possíveis respostas são:\n1. Windows Server\n2. Unix\n3. Linux\n4. Netware\n5. MacOS\n6. Outro\n"))
    Votos.append(i)
    contVotos+=1
    
WS, UX, LX, NW, MAC, Ot = 0,0,0,0,0,0
for i in range(len(Votos)):
    if(Votos[i] == 1):
        WS+=1
    elif(Votos[i] == 2):
        UX+=1
    elif(Votos[i] == 3):
        LX+=1
    elif(Votos[i] == 4):
        NW+=1
    elif(Votos[i] == 5):
        MAC+=1
    elif(Votos[i] == 6):
        Ot+=1
    
maior="Windows Server"
maiorN= WS
if(UX>WS or UX>LX or UX>NW or UX> MAC or UX>Ot):
    maior="Unix"
    maiorN= UX
elif(LX>WS or LX>UX or LX>NW or LX> MAC or LX>Ot):
    maior="Linux"
    maiorN= LX
elif(NW>WS or NW>UX or NW>LX or NW> MAC or NW>Ot):
    maior="Netware"
    maiorN= NW
elif(MAC>WS or MAC>UX or MAC>LX or MAC> NW or MAC>Ot):
    maior="MacOs"
    maiorN= MAC
elif(Ot>WS or Ot>UX or Ot>LX or Ot> NW or Ot>MAC):
    maior="Outros"
    maiorN= Ot
    

    
print("Sistema Operacional Votos %\n------------------- ----- ------\nWindows Server {} {:.0f}%\nUnix {} {:.0f}%\nLinux {} {:.0f}%\nNetware {} {:.0f}%\nMac OS {} {:.0f}%\nOutro {} {:.0f}%\n------------------- -----\nTotal {}".format(WS,(WS/contVotos)*100,UX,(UX/contVotos)*100,LX,(LX/contVotos)*100,NW,(NW/contVotos)*100,MAC,(MAC/contVotos)*100,Ot,(Ot/contVotos)*100,contVotos))
      
empat=False
if(maiorN==WS):
    maiorN2 = "Windows Server"
    if(maiorN2!= maior):
        empat = True
elif(maiorN==UX):
    maiorN2 = "Unix"
    if(maiorN2!= maior):
        empat = True
elif(maiorN==LX):
    maiorN2 = "Linux"
    if(maiorN2!= maior):
        empat = True
elif(maiorN==NW):
    maiorN2 = "Netware"
    if(maiorN2!= maior):
        empat = True
elif(maiorN==MAC):
    maiorN2 = "MacOs"
    if(maiorN2!= maior):
        empat = True
elif(maiorN==Ot):
    maiorN2 = "Outros"
    if(maiorN2!= maior):
        empat = True

if(empat==True and maiorN2!= maior):
    print("Ocorreu um empate entre {} e {}, com {} votos,correspondendo {:.0f}%  dos votos..".format(maior,maiorN2,maiorN,(maiorN/contVotos)*100))
else:
    print("O Sistema Operacional mais votado foi o {}, com {} votos,correspondendo {:.0f}%  dos votos..".format(maior,maiorN,(maiorN/contVotos)*100))