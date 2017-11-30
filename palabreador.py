def palabreador():
    palabra=raw_input("dime una palabra: ")
    suma=0
    for cont in range(0,len(palabra),1):
        if palabra[cont]=="a":
           suma=suma+1
    print"en la palabra",palabra,"hay",suma,"a"

palabreador()


def palabrador():
    palabra=raw_input("dime una palabra: ")
    suma=0
    a=0
    e=0
    i=0
    o=0          
    u=0
    for cont in range(0,len(palabra),1):
        if palabra[cont]=="a":                   
           suma=suma+1
           a=a+1
           
        if palabra[cont]=="e":
           suma=suma+1
           e=e+1
           
        if palabra[cont]=="i":
           suma=suma+1
           i=i+1
           
        if palabra[cont]=="o":
           suma=suma+1
           o=o+1
           
        if palabra[cont]=="u":
           suma=suma+1
           u=u+1

   print "en la palabra", palabra, "hay", suma, "a:", a, "e:", e, "i:", i,"o:", o, "u:", u    

palabreador()
                
                       

                       
