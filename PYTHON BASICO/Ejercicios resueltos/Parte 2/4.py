p1 = float(input("Ingrese la calificación parcial 1: "))
p2 = float(input("Ingrese la calificación parcial 2: "))
p3 = float(input("Ingrese la calificación parcial 3: "))
examen = float(input("Ingrese la calificación del examen final: "))
trabajo = float(input("Ingrese la calificación del trabajo final: "))

prom_parciales = (p1 + p2 + p3) / 3
final = prom_parciales*0.55 + examen*0.30 + trabajo*0.15

print(f"Calificación final: {final:.2f}")
