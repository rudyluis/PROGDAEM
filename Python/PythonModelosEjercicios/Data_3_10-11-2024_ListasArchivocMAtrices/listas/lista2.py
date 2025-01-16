subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for subject in subjects:
    print("Yo estudio " + subject)

n=int(input('n>>>>'))
nombres=[]
for i in range(1,n+1,1):
    nom=input('nombre >>>'+str(i))
    nombres.append(nom)
print(nombres);

################################################
##########EJERCICIO2

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])

