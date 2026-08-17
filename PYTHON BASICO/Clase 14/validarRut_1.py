
def validar_rut(rut):
    """
    Valida un RUT chileno básico.
    Formato esperado: '12345678-5' o '12.345.678-5'
    """

    #  limpiar el RUT (quitar puntos y guiones)
    rut = rut.replace(".", "").replace("-", "").lower()

    #  separar número y dígito verificador
    cuerpo = rut[:-1]
    dv = rut[-1]

    # Validar que el cuerpo sea numérico
    if not cuerpo.isdigit():
        return False

    # Multiplicadores 2,3,4,5,6,7 (repetidos de derecha a izquierda)
    multiplicadores = [2, 3, 4, 5, 6, 7]
    suma = 0
    for i, digito in enumerate(reversed(cuerpo)):
        suma += int(digito) * multiplicadores[i % len(multiplicadores)]

    # calcular el dígito verificador esperado
    resto = suma % 11
    verificador = 11 - resto

    if verificador == 11:
        verificador = "0"
    elif verificador == 10:
        verificador = "k"
    else:
        verificador = str(verificador)

    #Comparar con el dígito entregado
    return dv == verificador


rut_correcto = "11.222.333-9"
rut_incorrecto = "11.222.333-8"

print(f"{rut_correcto} →", "Válido ✅" if validar_rut(rut_correcto) else "Inválido ❌")
print(f"{rut_incorrecto} →", "Válido ✅" if validar_rut(rut_incorrecto) else "Inválido ❌")