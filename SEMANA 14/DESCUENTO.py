# Definición de la función calcular_descuento
def calcular_descuento(monto_compra, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando el porcentaje especificado al monto de la compra.

    Parámetros:
    monto_compra (float): El monto total de la compra.
    porcentaje_descuento (float, opcional): El porcentaje de descuento a aplicar (por defecto es 10%).

    Retorna:
    float: El monto del descuento calculado.
    """
    descuento = (monto_compra * porcentaje_descuento) / 100
    return descuento

# Programa principal

# Primera llamada con el monto de la compra solamente (10% de descuento por defecto)
monto1 = 100.00  # Ejemplo de monto de compra
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1
print(f"Monto de la compra: ${monto1:.2f}")
print(f"Descuento aplicado: ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}")
print()

# Segunda llamada con el monto de la compra y el porcentaje de descuento especificado (por ejemplo, 15%)
monto2 = 200.00  # Otro ejemplo de monto de compra
porcentaje_descuento2 = 15  # Descuento del 15%
descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
monto_final2 = monto2 - descuento2
print(f"Monto de la compra: ${monto2:.2f}")
print(f"Descuento aplicado: ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")
