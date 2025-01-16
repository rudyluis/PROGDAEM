import os
import zipfile
### funcion de opciones
def agregar_cliente(nombre,telefono):
    with open('listaclientes.txt','a') as file:
        file.write(f'{nombre}|{telefono}\n')
    print(f"El cliente:{nombre} se ha agregado correctamente")
def eliminar_contacto(nombre):
    with open ('listaclientes.txt','r',encoding='utf-8') as archivo:
        lineas=archivo.readlines()
        with open('listaclientestemp.txt','a', encoding='utf-8') as archivo2:
            for linea in lineas:
                data=linea.strip().split("|")
                if(data[0]!=nombre):
                    archivo2.write(linea)
    os.remove('listaclientes.txt')
    os.rename('listaclientestemp.txt','listaclientes.txt')
    print('Contacto Eliminado correctamente!!!!!!')
def listar_agenda():
    print('Nombre\tTelefono\t')
    with open('listaclientes.txt','r') as file:
        for line in file:
            data=line.strip().split('|')
            print(f'{data[0]}\t {data[1]}\t')
def consultar_telefono(nombre):
    with open('listaclientes.txt','r') as file:
        for line in file:
            data=line.strip().split('|')
            if(data[0].upper()==nombre.upper()):
                return "El numero de contacto es>>>"+data[1]
        return "No se encontro el cliente buscado...."   
def modificar_contacto(nombre,telefono):
    eliminar_contacto(nombre)
    agregar_cliente(nombre,telefono)
    print('Se ha modificado el contacto correctamente')

def copia_seguridad():
    archivo_path=os.path.abspath('listaclientes.txt')
    nombre_sin_extension=os.path.splitext('listaclientes.txt')[0]
    archivo_zip_path=f"{nombre_sin_extension}.zip"
    with zipfile.ZipFile(archivo_zip_path,'w',zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(archivo_path,arcname='listaclientes.txt')
    print('Back Up archivo comprimido correctamente')

## Menu Principal
while True:
    print('Listado de Clientes')
    print('-------------------')
    print('1.Consultar telefono de un cliente')
    print('2.Agregar Telefono de un cliente')
    print('3.Eliminar el telefono de Un cliente')
    print('4.Listar Clientes')
    print('5.Modificar Cliente')
    print('6.Copia de Seguridad')
    print('0.Salir')

    opcion = input('Ingrese o selecciones una opcion: ')
    if opcion=='1':
        nombre=input('Ingrese el nombre del cliente a buscar:')
        telefono=consultar_telefono(nombre)
        print(telefono)
    elif opcion=='2':
        print('REGISTRO DE DATOS')
        nombre=input('Introduzca el nombre del cliente: ')
        telefono=input('Introduzca el telefono del cliente: ')
        agregar_cliente(nombre,telefono)
    elif opcion=='3':
        print('ELIMINACION DE DATOS')
        nombre=input('Introduzca el nombre a eliminar: ')
        eliminar_contacto(nombre)
    elif opcion=='4':
        print("--------------------")
        print('Listado de Clientes')
        listar_agenda()
        print("--------------------")
    elif opcion=='5':
        print("--------------------")
        print('Modificar Cliente')
        nombre=input('Ingrese el nombre del contacto')
        telefono=input('Ingrese el telefono del contacto')
        modificar_contacto(nombre,telefono)
        print("--------------------")
    elif opcion=='6':
        print("--------------------")
        print('Copia de Seguridad')
        copia_seguridad()
        print("--------------------")
    elif opcion=='0':
        print('Fin de Programa hassta pronto :(')
        break
    else:
        print('Opcion Invalida. Intente Nuevamente')