def operarLista(lista1,lista2,operacion):
    if(len(lista1)!=len(lista2)):
        return None
    if(operacion=='+'):
        resultado=[a+b for a,b in zip(lista1,lista2)]
    if(operacion=="-"):
        resultado=[a-b for a,b in zip(lista1,lista2)]
    if(operacion=="*"):
        resultado=[a*b for a,b in zip(lista1,lista2)]
    if(operacion=="/"):
        resultado=[a/b for a,b in zip(lista1,lista2)]
       
    return resultado

Lista1=[1,2,3,4,5]
Lista2=[6,7,8,9,10]

###main

ListaResultado=operarLista(Lista1,Lista2,'+')
print(ListaResultado)
ListaResultado=operarLista(Lista1,Lista2,'-')
print(ListaResultado)
ListaResultado=operarLista(Lista1,Lista2,'*')
print(ListaResultado)
ListaResultado=operarLista(Lista1,Lista2,'/')
print(ListaResultado)