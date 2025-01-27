class gato:
    tipo='mamifero'
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        self.alimentos=[]
        
    def habla(self):
        print('Maulla')
    def esAdulto(self):
        if(self.edad>1):
            print(self.nombre,"es adulto")
        else:
            print(self.nombre,'Minino')
    def come(self, alimento):
        return alimento in self.alimentos

p=gato('Misifuz',12)

print('El nombre de mi gato es '+p.nombre)


p.esAdulto()

p.edad=1

p.esAdulto()

print(p.habla())


p.raza='persa';

print(p.nombre,p.raza)

print(p.nombre,p.tipo)

p.alimentos.append('atun')
p.alimentos.append('pollo')
p.alimentos.append('croquetas')
print(p.alimentos)
alimentos_gato=['atun','pollo']

print(p.come('ratones'))

print(p.alimentos)

