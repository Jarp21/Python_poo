<!--HEADING-->

# Repaso basico, Poo en python

![Fondo1](https://static.platzi.com/cdn-cgi/image/width=1024,quality=50,format=auto/media/achievements/badge-poo-algoritmos-python-8960967b-d29a-47a6-85f6-db9b7b4dc8a9.png "Logo del curso")

---

## Lista de tareas
* [x] Averigaur acerca de decoradores en python
* [ ] Averiguar para que sirve el decorador @property
* [ ] Averiguar acerca de Big O
* [ ] Buscar mas acerca del ordenamiento por mezcla
* [ ] Mirar de nuevo el video 23

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

### Herencia
Sirve para modelar jerarquias

### Polimorfismo

Es la habilidad de tomar varias formas

## Notacion asintotica
### Crecimiento asintotico

Es el como las cosas se van hacia el infinito

* Big O notation, sirve para ver el mayor de los casos
    * En Big O solo  nos importa el termino independiente desconectado con mayor valor

### Clases de complejidad algoritmica

* O(1) Constante
* O(n) Lineal
* O(Log n) Logaritmica
* O(n Log n) Log lineal
* O(n**2) Polinomial
* O(2**n) Exponencial
* O(n!) Factorial

### Busqueda lineal
Trata de tomar cada conceptoopr si solo
* Es buena si se usa una o pocas veces

### Busqueda binaria

> Divide y venceras
Trata de tomar un problema e la forma mas simple posible
* divide en 2 en cada iteracion
* Asimila que la lista esta ordenada

### Ordenamiento de burbuja
#### O(n ** 2)
Algoritmo que recorre una lista para organizarla

### Ordenamiento por mezcla
Divide la lista en subfactores hasta que son listas de 1 y las compara

## Ambientes virtuales

Permite probar paquetes o versiones y nos permite no contaminer nuestro ambiente global

### pip

Es una seccion de librerias que pueden ser descargadas para distintos usos

#### Comandos utiles con pip
SS
* python -m venv name ~~Creacion~~
* env/bin/activate ~~Activa~~
* source env/bin/activate ~~Entrada~~
* pip install name ~~Instalacion de librerias~~
* pip freeze  ~~Sirve ;ara ver lo instalado~~
* deactivate ~~Sale del ambiente virtual~~

## Graficado con Bokeh

Es una libreria que tiene muchas utilidades y se deja exportar a html o dentro de django