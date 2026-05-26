# ============================================================
#  GESTIÓN DE PRECIOS DE MENÚ CON PROMOCIONES
#  Problema 2 - Evaluación Final POA
# ============================================================
#
#  Descripción:
#    Se gestiona el menú de un restaurante representado como
#    una matriz [Nombre, Categoría, Precio Base].
#    Se aplica un 15% de descuento si el producto pertenece
#    a la categoría objetivo Y su precio base supera el umbral.
#
#  Autor   : Estudiante POA
#  Lenguaje: Python 3
# ============================================================


# ----------------------------------------------------------
# 1. CONSTANTES DE NEGOCIO
# ----------------------------------------------------------
CATEGORIA_OBJETIVO = "Plato Principal"   # Categoría que recibe la promoción
UMBRAL_PRECIO      = 20_000              # Precio base mínimo para aplicar descuento
DESCUENTO          = 0.15               # 15 %


# ----------------------------------------------------------
# 2. MATRIZ DEL MENÚ
#    Estructura: [Nombre, Categoría, Precio Base (COP)]
# ----------------------------------------------------------
menu = [
    ["Bandeja Paisa",       "Plato Principal",  35_000],
    ["Ajiaco Bogotano",     "Plato Principal",  28_000],
    ["Empanadas (3 und)",   "Entrada",          12_000],
    ["Lulada",              "Bebida",            8_000],
    ["Churrasco a la Brasa","Plato Principal",  45_000],
    ["Ensalada César",      "Entrada",          18_000],
    ["Sancocho de Gallina", "Plato Principal",  15_000],
    ["Brownie con Helado",  "Postre",           14_000],
]


# ----------------------------------------------------------
# 3. MÓDULO (FUNCIÓN) – Calcula el precio final con promoción
# ----------------------------------------------------------
def calcular_precio_final(nombre, categoria, precio_base):
    """
    Calcula el precio final aplicando la promoción si corresponde.

    Parámetros:
        nombre      (str)   : Nombre del producto.
        categoria   (str)   : Categoría del producto.
        precio_base (float) : Precio base del producto en COP.

    Retorna:
        tuple: (precio_final, descuento_aplicado)
            precio_final       (float) : Precio después de la promoción.
            descuento_aplicado (bool)  : True si se aplicó el descuento.
    """
    if categoria == CATEGORIA_OBJETIVO and precio_base > UMBRAL_PRECIO:
        precio_final = precio_base * (1 - DESCUENTO)
        return precio_final, True
    else:
        return precio_base, False


# ----------------------------------------------------------
# 4. LÓGICA PRINCIPAL – Recorre la matriz y muestra resultados
# ----------------------------------------------------------
def mostrar_menu_con_promocion():
    """Itera el menú, calcula precios finales y los imprime."""
    ancho = 65
    linea = "=" * ancho

    print(linea)
    print(" MENÚ DEL RESTAURANTE – PROMOCIÓN APLICADA".center(ancho))
    print(f" Categoría con descuento : {CATEGORIA_OBJETIVO}".center(ancho))
    print(f" Umbral de precio        : ${UMBRAL_PRECIO:,.0f} COP".center(ancho))
    print(f" Descuento               : {int(DESCUENTO*100)}%".center(ancho))
    print(linea)
    print(f"{'Producto':<22} {'Categoría':<18} {'P.Base':>10} {'P.Final':>10} {'Desc.':>5}")
    print("-" * ancho)

    for producto in menu:
        nombre, categoria, precio_base = producto          # Desempaquetado de la matriz
        precio_final, aplico = calcular_precio_final(nombre, categoria, precio_base)

        indicador = " ✓" if aplico else "  "
        print(
            f"{nombre:<22} {categoria:<18} "
            f"${precio_base:>8,.0f} ${precio_final:>8,.0f}{indicador}"
        )

    print(linea)
    print(" ✓ = Descuento del 15% aplicado")
    print(linea)


# ----------------------------------------------------------
# 5. PUNTO DE ENTRADA
# ----------------------------------------------------------
if __name__ == "__main__":
    mostrar_menu_con_promocion()
