c1 = float(input("Ingrese la calificación 1: "))
c2 = float(input("Ingrese la calificación 2: "))
c3 = float(input("Ingrese la calificación 3: "))

prom = (c1 + c2 + c3) / 3

if prom >= 70:
    print(f"Promedio: {prom:.2f} → APROBADO")
else:
    print(f"Promedio: {prom:.2f} → REPROBADO")
