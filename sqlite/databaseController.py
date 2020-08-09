#!/usr/bin/env python3
import sqlite3
"""
    Author: Adrian González Pardo
    Email: gozapaadr@gmail.com
    A.k.a: d3vcr4ck / DevCrack
    Fecha de modificación: 09/08/2020
    GitHub: AdrianPardo99
    Licencia Creative Commons CC BY-SA

    @name       ->  Es el nombre bajo el cual se resguardara el archivo de sqlite3
"""
def create_database(name):
    return sqlite3.connect(name)

"""
    @conexion   ->  Es la conexion a la base de datos existente gracias al create_database
"""
def close_database(conexion):
    conexion.close()

"""
    @conexion   ->  Es la conexion a la base de datos existente gracias al create_database
    @table      ->  Es el nombre de la tabla que se almacenara de acuerdo a la variable @name
    @params     ->  Son los campos/parametros que componen a la tabla
"""

def create_table_with_params(conexion,table,params):
    cursorTable=conexion.cursor()
    print(f'Query execute:\nCREATE TABLE IF NOT EXISTS {table} ({params})')
    cursorTable.execute(f'CREATE TABLE IF NOT EXISTS {table} ({params})')
    conexion.commit()

"""
    @conexion   ->  Es la conexion a la base de datos existente gracias al create_database
    @table      ->  Es el nombre de la tabla que se accedera
    @params     ->  Son los campos/parametros que componen a la tabla
    @tuple      ->  Es la tupla de datos que evitaran un hardcoding de los mismo y añadiran una capa de seguridad
"""
def insert_into_table(conexion,table,params,data):
    cursorTable=conexion.cursor()
    print(f'Query execute: \n INSERT INTO {table} VALUES ({params})')
    if type(data) is list:
        cursorTable.executemany(f'INSERT INTO {table} VALUES ({params})',data)
    elif type(data) is tuple:
        cursorTable.execute(f'INSERT INTO {table} VALUES ({params})',data)
    conexion.commit()
