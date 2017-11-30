def sumador_cifras():
    numero=input("Dime un numero:")
    mayor=0
    cifra=0
    while numero>0:
        cifra=numero%10
        numero=numero/10
        if(cifra>mayor):
            mayor=cifra
        
    print "La cifra mayor sera", mayor 
          
sumador_cifras()

