# Curso básico de algunos módulos de Python 3 #

__Nota: En linux hay un header el cual permite ejecutar tipo binario los archivos el cual esta acompañado en el inicio del archivo e incluso bajo el comando "file" la descripción del archivo es "Archivo.py: Python script, ASCII text executable"__

Esta directiva o header es:
```python
  #!/usr/bin/env python3

# O
  #!/bin/python3
```
# Print con distintas clase de variable #
```python

  var=Integer
  var1=Float
  var2=String/Whatever

  print(f'Description or anything {var}.... bla bla bla {var1}... more more more {var2}')

# Para conocer la clase del tipo de dato en Python:
  type(var)

# Casting/Parsing variable a otra

  var3=str(231223213213)  # -> Anything to String
  var1=int(var3)          # -> String to int
```

# Input de teclado #
```python
  variable=input()
  print(variable)
```

# Operaciones con String #

```python
  variable="Value or anything in string"
  print(variable.upper())     # ->  Upper case
  print(variable.lower())     # ->  Lower case

  variable.split()            # -> Separa el string y retorna una lista por cada espacio
  variable.split('character') # -> Los mismo, pero al carácter de separación
  # More and more
```

# Estructuras de datos #
## Listas ##
```python
# Creación
  lista=[foo, foo1, foo2, ... , fooN]
  lista=list(value)

# Añadir otro valor
  lista.append(val)

# Eliminar valor
  lista.remove("fooM")

# Verifica si el elemento existe en la lista o cualquier estructura
  valueOrStructure in lista   # -> True or False
```
## Tuplas ##
Estructura constante no mutable.
```python
# Creación
  tupla=(foo, foo1, foo2, ... , fooN)
  tupla=tuple(value)
```
## Conjuntos / Sets ##
```python
# Creación
  conjunto={foo, foo1, foo2, ... , fooN}
  conjunto=set(valueOrTuple)

# Añadir
  conjunto.add(value)

# Eliminar valor
  conjunto.remove(valueN)

```
## Diccionario (Like Hash table) ##
```python
# Creación
  dic={key0:value0, key1:value1, ..., keyN:valueN}

# Añadir
  dic[keyM]=valueM

# Eliminar
  del(dic[keyS])

  dic.pop(keyS)
```

### Algunas cosas útiles de los diccionarios ###
Los diccionarios también pueden ser útiles para usar el estándar de JSON el cual en algunas cosas puede interactuar con aplicaciones que usen este estándar.

```python
import json
# Dictionary to JSON
  varJSON=json.dump(dictionary)

# JSON to Dictionary
  varDic=json.loads(jsonVariable)
```

# Definición de métodos y funciones, Funciones Lambda #
En python los métodos y funciones son fragmentos de código los cuales permiten realizar operaciones que tengan diversa repetitividad a la hora de trabajar
```python
# Definicion de método o función
  def nameMethodOrFunc(params=""):
    #code and more code if you want to save the return value you only need to save the value
      # in another variable
    return value

# Lambda
  variable= lambda param1,param2: param1+param2 # operation_code_example

```

# Docstring #
En python es sencillo crear pequeña documentación de los métodos, funciones y clases los cuales pueden ir acompañados de la siguiente estructura y pueden ser obtenidos con un método específico
```python
  def method():
    """
    Doc about method()
    Description, etc.
    """
    # Code and more code
  help(method)
```
Por otro lado en la consola de Windows, Linux o MAC es posible generar o ver la documentación de un archivo a través de los siguientes comandos
```bash
  pydoc <Path>/file.py
```

# módulo Doctest #
Es un módulo que permite realizar pruebas automáticas las cuales permiten hacer un test del código escrito:
```python
  def method(params):
    """
    Doc and description
    >>> method(paramsPrube1)
    result

    >>> method(paramsPrube2)
    result-2

    >>> method(paramsPrube3)
    result-3

    """
    # Code and more code
    return something
  import doctest
  doctest.testmod()
```
Al realizar esto nos permitirá realizar el test de method el cual según nuestra descripción es que espera como valor de retorno result y el módulo buscara que coincida con el con lo que tienes escrito, para finalmente mostrar en pantalla si el test fue correcto o no

# módulo Unittest #
Parecido a Doctest es un módulo que permite realizar pruebas automáticas, con la diferencia que estos test pueden ser programados sin que estos se encuentren en el apartado de la documentación.
```python
  def method(params):
    """
    Doc and description
    """
    # Code and more code
    return something

  import unittest
  class pruebas(unittest.TestCase):
    def test(self):
      self.assertEqual(method(paramsPrube1),result)
      self.assertEqual(method(paramsPrube2),result-2)
      self.assertEqual(method(paramsPrube3),result-3)

  if __name__ == '__main__':
    unittest.main()
```
Con esto en la ejecución de nuestro código nos dirá los test de éxito y los test de fallo.

# módulo SQLite3 #
Es un módulo para manejar/crear bases de datos las cuales son accesibles por el mismo lenguaje
```python
  import sqlite3

# Creación de la base de datos
  conexion=sqlite3.connect(name)    # Retorna el manejador de la conexión a la base de datos


# Creación de tablas
  cursor=conexion.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS {} VALUES ({})".format(nameTable,attrTable))
  conexion.commit()


# Inserción de datos sin HARDCODING
  cursor=conexion.cursor()
  tuplaData=(param1,param2,param3)
  # Si la tabla tiene 3 valores
  cursor.execute("INSERT INTO {} VALUES (?,?,?)".format(nameTable),tuplaData)

# Inserción multiple sin HARDCODING
  listaData=[(param1,param2,param3),(param4,param5,param6),(param7,param8,param9)]
  cursor.executemany("INSERT INTO {} VALUES (?,?,?)".format(nameTable),listaData)

# Al final de la inserción
  conexion.commit()


# Consultar todos los datos
  cursorTable=conexion.cursor()
  cursorTable.execute("SELECT*FROM {}".format(nameTable))
  rows=cursorTable.fetchall()

# Consultar todos los datos con sentencia where sin HARDCODING
  cursorTable=conexion.cursor()
  cursorTable.execute("SELECT*FROM {} WHERE {}".format(table,whereTab),dataWhere)
  # @whereTab viene construido de la siguiente forma parameter_value = ?
  # @dataWhere es una tupla de datos que llenan los parametros de '?'
  rows=cursorTable.fetchall()

    # Nota el comodin '*' puede ser cambiado por atributos específicos,
    # @whereTab puede ir acompañado por comodines de orden y de álgebra relacional

# Print rows de fetchall()
  for row in rows:
    print(f'{row}')


# Borrar datos
  cursorTable=conexion.cursor()
  cursorTable.execute("DELETE FROM {} where {}".format(table,whereTab),dataWhere)
  conexion.commit()


# Actualización de datos
  cursorTable=conexion.cursor()
  cursorTable.execute("UPDATE {} SET {} where {}".format(table,dataSet,whereTab),data)
  # @dataSet: Son los datos que van a ser modificados param = ?, param2 = ?
  # @data:  Es la tupla de datos que van a llenarse desde los parametros de @dataSet y @whereTab
  conexion.commit()


# Cerrar conexión de la base de datos
  conexion.close()
```
# módulo tkinter #
El módulo tkinter es un módulo gráfico que permite crear interfaces de usuario
