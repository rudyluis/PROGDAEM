import requests
def obtener_pais_nombre(nombre_pais):
    url=f"https://restcountries.com/v3.1/name/{nombre_pais}"
    response=requests.get(url)
    data= response.json()
    nombre= data[0]['name']['common']
    capital=data[0]['capital']
    poblacion=data[0]['population']
    map= data[0]['maps']['googleMaps']

    print(f'Pais:{nombre}')
    print(f'Capital:{capital}')
    print(f'Poblacion:{poblacion}')
    print(f'Mapa:{map}')

def obtener_lista_paises():
    url=f"https://api.worldbank.org/v2/country?format=json"
    response=requests.get(url)
    data= response.json()
    paises=[(d['name'],d['id']) for d in data[1]]
    for nombre,codigo in paises:
        print(f"Pais:{nombre} Codigo{codigo}" )

def PIB_por_gestion(nombre_pais,gestion):
    url = f"https://api.worldbank.org/v2/country/{nombre_pais}/indicator/NY.GDP.MKTP.CD?date={gestion}&format=json"
    response=requests.get(url)
    data= response.json()
    ##print(data)
    print(f"PIB por pais: {pais} gestion: {gestion} Monto: {data[1][0]['value']}")
    return 0
def PIB_por_pais(nombre_pais,gestion):
    return 0
##Main Principal####
print('Datos Externos')

while True:
    print('Datos Externos')
    print('--------------')
    print('1.Datos Pais')
    print('2.Listado de Paises')
    print('3.PIB por gestion')
    print('4.PIB por Pais')
    print('0.Salir')

    opcion = input('Ingrese o selecciones una opcion: ')
    if opcion=='1':
        print('Obtener Datos Pais')
        pais= input('Introduzca el nombre del pais: ')
        obtener_pais_nombre(pais)
    elif opcion=='2':
        print('Obtener Lista Paises')
        obtener_lista_paises()
    elif opcion=='3':
        print('PIB por Gestion')
        pais= input('Introduzca el nombre del pais: ')
        gestion= input('Introduzca la gestion: ')
        PIB_por_gestion(pais,gestion)

    elif opcion=='0':
        print('Fin de Programa hassta pronto :(')
        break
    else:
        print('Opcion Invalida. Intente Nuevamente')





