# ejecercio 

print("-------------------------")
print("---suma de sus digitos---")
print("-------------------------")

#input
n=int(input("Digite un numero : "))
sum=0
#processing
while(n!=0):
    d=(n%10)
    n=(n-d)//10
    sum=sum +d
    
   
print("la suma de cada de sus digitos es : " +str(sum))
    

    
    
    