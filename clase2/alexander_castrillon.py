# ejercicio

class Producto:
    def __init__(self, nombre, precio, id, stock):
        self.nombre = nombre
        self.precio = precio
        self.id = id
        self.stock = stock
    
    def informacion(self):
        print(f'| ID: {self.id} | Nombre: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock} |')


class Tienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.inventario = {}
        print(f'¡Bienvenido a {self.nombre_tienda}!') 
        
    def agregar_productos(self, producto):
        if not isinstance(producto, Producto):
            print("solo se pueden agregar objetos de tipo 'Producto'.")
            return

        if producto.id in self.inventario:
            self.inventario[producto.id].stock += producto.stock
            print(f"Stock de '{producto.nombre}' (ID: {producto.id}) actualizado. Nuevo stock: {self.inventario[producto.id].stock}")
        else:
            self.inventario[producto.id] = producto
            print(f"Producto '{producto.nombre}' (ID: {producto.id}) agregado al inventario con {producto.stock} unidades.")

    def vender(self, id_producto, cantidad):
        if id_producto not in self.inventario:
            print(f"Error: Producto con ID '{id_producto}' no encontrado en el inventario.")
            return None

        producto_a_vender = self.inventario[id_producto]

        if cantidad <= 0:
            print("La cantidad a vender debe ser mayor que cero.")
            return None

        if cantidad > producto_a_vender.stock:
            print(f" No hay suficiente stock de '{producto_a_vender.nombre}'. Stock actual: {producto_a_vender.stock}")
            return None
        
        producto_a_vender.stock -= cantidad
        costo_total = producto_a_vender.precio * cantidad
        
        print(f"Venta exitosa: Se vendieron {cantidad} unidades de '{producto_a_vender.nombre}'.")
        print(f"Costo total de la venta: ${costo_total:.2f}")

        if producto_a_vender.stock == 0:
            print(f"¡Advertencia! '{producto_a_vender.nombre}' (ID: {producto_a_vender.id}) se ha agotado.")

        return costo_total
    
    def mostrar_inventario(self):
        print(f"\n--- Inventario actual de {self.nombre_tienda} ---")
        if not self.inventario:
            print("El inventario está vacío.")
            return

        print(f"{'| ID':<5} | {'Nombre':<20} | {'Precio':<8} | {'Stock':<6} |")
        print("-" * 55)

        for producto_id, producto_obj in self.inventario.items():
            producto_obj.informacion()
        print("--------------------------------------")

    def eliminar_producto(self, id_producto):
        if id_producto in self.inventario:
            producto_eliminado = self.inventario.pop(id_producto)
            print(f"'{producto_eliminado.nombre}' (ID: {id_producto}) ha sido eliminado del inventario.")
        else:
            print(f"Error: Producto con ID '{id_producto}' no encontrado para eliminar.")


  

# aumentar productos
producto1 = Producto('jarro', 2.5, 123, 20)
producto2 = Producto('plato', 4, 124, 25)
producto3 = Producto('cuchara', 1, 125, 12)
producto4 = Producto('tenedor', 1, 126, 22)
producto5 = Producto('vaso', 1.5, 127, 30)



if __name__ == "__main__":
    mi_tienda = Tienda('María Sol')

    print("\n--- Agregando productos al inventario ---")
    mi_tienda.agregar_productos(producto1)
    mi_tienda.agregar_productos(producto2)
    mi_tienda.agregar_productos(producto3)
    mi_tienda.agregar_productos(producto4)
    mi_tienda.agregar_productos(producto5)
    
    producto1_extra_stock = Producto('jarro', 2.5, 123, 10) 
    mi_tienda.agregar_productos(producto1_extra_stock)

    mi_tienda.mostrar_inventario()

    print("\n--- Realizando ventas ---")
    venta1_costo = mi_tienda.vender(123, 5)
    venta2_costo = mi_tienda.vender(124, 10)
    venta3_costo = mi_tienda.vender(126, 25)
    venta4_costo = mi_tienda.vender(999, 2)
    venta5_costo = mi_tienda.vender(125, 12)

    mi_tienda.mostrar_inventario()

    print("\n--- Eliminando productos ---")
    mi_tienda.eliminar_producto(124)
    mi_tienda.eliminar_producto(999)

    mi_tienda.mostrar_inventario()