def limpiar_rut(rut):
    """Elimina puntos y guiones, devuelve cuerpo y dígito verificador."""
    rut = rut.replace(".", "").replace("-", "").lower()
    cuerpo = rut[:-1]
    dv = rut[-1]
    return cuerpo, dv


# -------------------------------------------------------
# ALGORITMO 1 (Oficial en Chile)
# -------------------------------------------------------
def calcular_dv_algoritmo1(rut):
    cuerpo, dv = limpiar_rut(rut)
    multiplicadores = [2, 3, 4, 5, 6, 7]
    suma = 0
    for i, digito in enumerate(reversed(cuerpo)):
        suma += int(digito) * multiplicadores[i % len(multiplicadores)]
    resto = suma % 11
    verificador = 11 - resto
    if verificador == 11:
        verificador = "0"
    elif verificador == 10:
        verificador = "k"
    else:
        verificador = str(verificador)
    return verificador


# -------------------------------------------------------
# ALGORITMO 2 (Variante alternativa)
# -------------------------------------------------------
def calcular_dv_algoritmo2(rut):
    cuerpo, dv = limpiar_rut(rut)
    multiplicadores = [9, 8, 7, 6, 5, 4]
    suma = 0
    for i, digito in enumerate(reversed(cuerpo)):
        suma += int(digito) * multiplicadores[i % len(multiplicadores)]
    resto = suma % 11
    verificador = resto
    if verificador == 10:
        verificador = "k"
    else:
        verificador = str(verificador)
    return verificador


# -------------------------------------------------------
# ALGORITMO 3 (Propiedades de división por 11)
# -------------------------------------------------------
def calcular_dv_algoritmo3(rut):
    cuerpo, dv = limpiar_rut(rut)
    multiplicadores = [9, 8, 7, 6, 5, 4]
    suma = 0
    for i, digito in enumerate(reversed(cuerpo)):
        suma += int(digito) * multiplicadores[i % len(multiplicadores)]

    # Convertimos la suma a string para obtener sus dígitos
    suma_digitos = list(map(int, str(suma)))
    # Suma alternada (como en el PDF: derecha a izquierda)
    total = 0
    signo = 1
    for d in reversed(suma_digitos):
        total += d * signo
        signo *= -1  # alterna entre + y -

    verificador = abs(total) % 11
    if verificador == 10:
        verificador = "k"
    else:
        verificador = str(verificador)
    return verificador


# -------------------------------------------------------
# FUNCIÓN DE VALIDACIÓN GENERAL
# -------------------------------------------------------
def validar_rut(rut, algoritmo=1):
    cuerpo, dv = limpiar_rut(rut)
    if not cuerpo.isdigit():
        return False

    if algoritmo == 1:
        esperado = calcular_dv_algoritmo1(rut)
    elif algoritmo == 2:
        esperado = calcular_dv_algoritmo2(rut)
    else:
        esperado = calcular_dv_algoritmo3(rut)

    return dv == esperado


# -------------------------------------------------------
# EJEMPLOS DE PRUEBA
# -------------------------------------------------------
ruts = [
    "11.222.333-9",  # ejemplo del PDF
    "18.765.432-k",
    "20.345.678-5",
    "11.222.333-8"  # incorrecto
]

for rut in ruts:
    print(f"\nRUT: {rut}")
    for i in range(1, 4):
        valido = validar_rut(rut, i)
        print(f"  Algoritmo {i} → {'✅ Válido' if valido else '❌ Inválido'} (DV esperado: {calcular_dv_algoritmo1(rut)})")
