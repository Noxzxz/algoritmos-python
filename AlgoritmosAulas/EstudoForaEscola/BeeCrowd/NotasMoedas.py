valorT = float(input())

not100 = valorT//100
not50= (valorT%100)//50 
not20= ((valorT%100)%50)//20 
not10= (((valorT%100)%50)%20)//10 
not5= ((((valorT%100)%50)%20)%10)//5 
not2= (((((valorT%100)%50)%20)%10)%5)//2 

tabMoed = ((((((valorT%100)%50)%20)%10)%5)%2.0)*100 

moe1 = (tabMoed)//100
moe5 = ((tabMoed)%100)//50
moe2 = (((tabMoed)%100)%50)//25
moe01 = ((((tabMoed)%100)%50)%25)//10
moe05 = (((((tabMoed)%100)%50)%25)%10)//5
moe100 = ((((((tabMoed)%100)%50)%25)%10)%5)/1

print("NOTAS:\n{:.0f} nota(s) de R$ 100.00\n{:.0f} nota(s) de R$ 50.00\n{:.0f} nota(s) de R$ 20.00\n{:.0f} nota(s) de R$ 10.00\n{:.0f} nota(s) de R$ 5.00\n{:.0f} nota(s) de R$ 2.00\nMOEDAS:\n{:.0f} moeda(s) de R$ 1.00\n{:.0f} moeda(s) de R$ 0.50\n{:.0f} moeda(s) de R$ 0.25\n{:.0f} moeda(s) de R$ 0.10\n{:.0f} moeda(s) de R$ 0.05\n{:.0f} moeda(s) de R$ 0.01".format(not100,not50,not20,not10,not5,not2,moe1,moe5,moe2,moe01,moe05,moe100))