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
