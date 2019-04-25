#Sorteo para 5 personas, hay 3 premios
#OJO: una persona no puede ganar dos veces

from random import randint
pipol = ["Pepito", "Shitz", "Luis", "RoDi", "Filomeno"]
for sorteo in range(3):
    ganador = pipol[randint(0,len(pipol)-1)]
    print("Ganador", sorteo + 1,":", ganador)
    pipol.remove(ganador)
