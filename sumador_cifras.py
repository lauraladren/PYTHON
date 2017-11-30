def sumador_cifras():
    numero=input("Dime un numero:")
    suma=0
    while numero>10:
        suma=suma+numero%10    
        numero=numero/10
    
    print "La suma de las cifras del numero vale", suma+numero

sumador_cifras()


