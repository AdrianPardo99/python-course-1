# Curso básico de algunos modulos de Python 3 #

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

# Modulo SQLite3 #
Es un modulo para manejar/crear bases de datos las cuales son accesibles por el mismo lenguaje
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

```
