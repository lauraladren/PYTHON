def sumador_cifras():
    numero=input("Dime un numero:")
    numerocifras=0
    while numero>0:
        numerocifras=numerocifras+1
        numero=numero/10

    print "El numero tendra", numerocifras , "cifras"

sumador_cifras()
