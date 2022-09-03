<!--HEADING-->

# Repaso basico, Poo en python

![Fondo1](https://static.platzi.com/cdn-cgi/image/width=1024,quality=50,format=auto/media/achievements/badge-poo-algoritmos-python-8960967b-d29a-47a6-85f6-db9b7b4dc8a9.png "Logo del curso")

---

## Lista de tareas
* [x] Averigaur acerca de decoradores en python
* [ ] Averiguar para que sirve el decorador @property

## Cosas aprendidas

### **Abstraccion**

* Nos enfocca en la informacion **relevante**, dejando de lado los detalles

### **Encapsulacion**

* Agrupa datos y controla su acceso para que no se modifique lo indebido

#### Decoradores
Son funciones que reciben como inputuna funcion y regresan otra. 
* Con decorar decimos que queremos modificar el comportamoento de una funcion existente.

```python
def function_a(function_b):

        def function_c():
            print('Antes de la operacion')
            function_b()
            print('Despues de la operacion')
            
        return function_c

@function_a
def saludar():
    print('Hola, desde una funcion')

saludar()
```

* Es necesario ejecutar la funcion fuera

Para enviar valores se usa *

```python
def decorator(funcion):
    def wrapper(*args, **kwargs):
        print('Antes de la operacion')
        resultado = funcion(*args, **kwargs)
        print('Despues de la operacion')

        return resultado

    return wrapper

@decorator
def suma(a, b):
    return a + b

print(suma(10, 20))
```

#### Getters y Setters

Sirven para poder ver (get) y modificar (set) propiedades de una clase las cuales estan encapsuladas y no podemos acceder