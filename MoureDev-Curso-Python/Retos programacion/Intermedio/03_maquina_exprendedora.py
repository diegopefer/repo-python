# reto 03
# Nivel: Medio
# Reto: MÁQUINA EXPENDEDORA
# Enunciado: /*
#  * Simula el funcionamiento de una máquina expendedora creando una operación
#  * que reciba dinero (array de monedas) y un número que indique la selección
#  * del producto.
#  * - El programa retornará el nombre del producto y un array con el dinero
#  *   de vuelta (con el menor número de monedas).
#  * - Si el dinero es insuficiente o el número de producto no existe,
#  *   deberá indicarse con un mensaje y retornar todas las monedas.
#  * - Si no hay dinero de vuelta, el array se retornará vacío.
#  * - Para que resulte más simple, trabajaremos en céntimos con monedas
#  *   de 5, 10, 50, 100 y 200.
#  * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge28.kt
# --------------------------------------------------

def comprobar_monedas(monedas_introducidas, monedas_validas):
    # Verifica que todas las monedas introducidas sean válidas
    for moneda in monedas_introducidas:
        if moneda not in monedas_validas:
            print("Hay monedas que no son válidas. Retornamos el dinero introducido:")
            return monedas_introducidas
    return True

def validar_dinero(selector_producto, monedas_introducidas, productos):
    # Verifica que el dinero introducido sea suficiente para el producto seleccionado
    if sum(monedas_introducidas) < productos[int(selector_producto)][1]:
        print("La cantidad de dinero no es suficiente. Retornamos el dinero introducido:")
        return monedas_introducidas
    return True

def operacion_producto(selector_producto, monedas_introducidas, productos, monedas_validas):
    # Calcula el cambio y entrega el producto
    coste_producto = productos[int(selector_producto)][1]
    total_introducido = sum(monedas_introducidas)
    cambio_devolver = total_introducido - coste_producto
    cambio = []

    # Calcula el cambio con las monedas válidas, usando las mayores primero
    for moneda in sorted(monedas_validas, reverse=True):
        while cambio_devolver >= moneda:
            cambio.append(moneda)
            cambio_devolver -= moneda

    print("Producto entregado:", productos[int(selector_producto)][0])
    if cambio:
        print("Cambio devuelto:", cambio)
    else:
        print("No hay cambio que devolver.")

def main():
    monedas_validas = {5, 10, 50, 100, 200}
    productos = {
        1: ("Agua", 100),
        2: ("Refresco", 150),
        3: ("Jugo", 200)
    }

    monedas_introducidas = [int(m) for m in input("Introduce las monedas separadas por comas: ").split(",")]
    selector_producto = input("Selecciona el número del producto que quieres comprar (1.Agua:100, 2.Refresco:150, 3.Jugo:200): ").strip()

    while True:
        if comprobar_monedas(monedas_introducidas, monedas_validas):
            if selector_producto == "1":
                print(f"Has seleccionado: {productos[1]}")
                if validar_dinero(selector_producto, monedas_introducidas, productos):
                    operacion_producto(selector_producto, monedas_introducidas, productos, monedas_validas)
                break
            else:
                print("Selección inválida, vuelve a intentarlo")
                break
        else:
            break

main()
