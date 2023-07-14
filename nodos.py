import random


class Producto:
  codigo = 100

  def __init__(self, nombre, cantidad, precio):
    self.codigo = Producto.codigo
    Producto.codigo += 1
    self.nombre = nombre
    self.cantidad = cantidad
    self.precio = precio

  def __str__(self):
    return f"{self.codigo}: {self.nombre} - Cantidad: {self.cantidad} - Precio: {self.precio}"


class Nodo:

  def __init__(self, producto):
    self.producto = producto
    self.siguiente = None


class Lista:

  def __init__(self):
    self.cabeza = None
    self.cola = None
    self.tamano = 0

  def agregar(self, producto):
    nodo = Nodo(producto)
    if self.cabeza is None:
      self.cabeza = nodo
      self.cola = nodo
    else:
      self.cola.siguiente = nodo
      self.cola = nodo
    self.tamano += 1

  def obtener(self, codigo):
    nodo_actual = self.cabeza
    while nodo_actual is not None:
      if nodo_actual.producto.codigo == codigo:
        return nodo_actual.producto
      nodo_actual = nodo_actual.siguiente
    return None

  def __len__(self):
    return self.tamano


class Pila:

  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[-1]

  def isEmpty(self):
    return len(self.items) == 0


# Crear la lista de productos
cantidad_productos = random.randint(10, 30)
lista_productos = Lista()
for i in range(cantidad_productos):
  nombre = f"producto{i+1}"
  cantidad = random.randint(1, 10)
  precio = round(random.uniform(1.0, 100.0), 2)
  producto = Producto(nombre, cantidad, precio)
  lista_productos.agregar(producto)

# Crear una pila con 10 productos extraídos de la lista
pila = Pila()
for i in range(10):
  codigo = random.randint(100, 130)
  producto = lista_productos.obtener(codigo)
  if producto is not None:
    pila.push(producto)

# Mostrar por consola los datos de los productos contenidos en la pila y calcular el valor total a pagar por cada producto
total_pagar = 0
while not pila.isEmpty():
  producto = pila.pop()
  precio = producto.cantidad * producto.precio
  total_pagar += precio
  print(producto)
  print(f"Total a pagar: {precio}\n")

# Mostrar el valor total a pagar por los productos en la pila y vaciar la pila
print(f"Total a pagar por los productos en la pila: {total_pagar}")
while not pila.isEmpty():
  pila.pop()

# Calcular el precio medio de todos los productos y mostrar la cantidad de productos en la lista
total_precio = 0
n_productos = len(lista_productos)
nodo_actual = lista_productos.cabeza
while nodo_actual is not None:
  total_precio += nodo_actual.producto.precio
  nodo_actual = nodo_actual.siguiente
precio_medio = total_precio / n_productos
print(f"Precio medio de todos los productos: {precio_medio}")
print(f"Cantidad de productos en la lista: {n_productos}")