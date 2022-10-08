# ejercicio 4

print("-----------------")
print("-----cajero------")
print("-----------------")

B10k=0
B2k=0
M100=0
Total_B10k=0
Total_B2k=0
Total_M100=0

#input
cheque=int(input("\n Ingrese el valor del cheque : "))

#processing
while cheque!=0:
    B10k=cheque//10000
    B2k=(cheque-(B10k*10000))//2000
    M100=((cheque-(B10k*10000))-(B2k*2000))//100
    Total_B10k=Total_B10k+B10k
    Total_B2k=Total_B2k+B2k
    Total_M100=Total_M100+M100
    cheque=int(input("\n Ingrese el valor del cheque : "))

#output
print("------------------------------------------------------------------------")
print("\n EL total de billetes de 10.000 fue de: "+str(Total_B10k))
print(" El total de billetes de 2.000 fue de:  "+str(Total_B2k))
print(" El total de monedas de 100 fue de: "+str(Total_M100))


