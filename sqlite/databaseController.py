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

"""
    @conexion   ->  Es la conexion a la base de datos existente gracias al create_database
    @table      ->  Es el nombre de la tabla que se accedera con el query select*from
"""
def select_query_all(conexion,table):
    cursorTable=conexion.cursor()
    cursorTable.execute(f'SELECT*FROM {table}')
    return cursorTable.fetchall()

"""
    @conexion   ->  Es la conexion a la base de datos existente gracias al create_database
    @table      ->  Es el nombre de la tabla que se accedera con el query select*from
    @whereTab   ->  Datos que van en la sentencia where sin hardcoding,
                    puede igual ponerse operaciones de orden
    @dataWhere  ->  Tupla de datos que van en el where
"""
def select_query_all_with_where(conexion,table,whereTab,dataWhere):
    cursorTable=conexion.cursor()
    cursorTable.execute(f'SELECT*FROM {table} WHERE {whereTab}',dataWhere)
    return cursorTable.fetchall()

"""
    @conexion   ->  Es la conexion a la base de datos existente gracias al create_database
    @selectArg  ->  Puede seleccionarse que elementos seran vistos en la consulta
    @table      ->  Es el nombre de la tabla que se accedera con el query select*from
"""
def select_query_2_all(conexion,selectArg,table):
    cursorTable=conexion.cursor()
    cursorTable.execute(f'SELECT {selectArg} FROM {table}')
    return cursorTable.fetchall()

"""
    @conexion   ->  Es la conexion a la base de datos existente gracias al create_database
    @selectArg  ->  Puede seleccionarse que elementos seran vistos en la consulta
    @table      ->  Es el nombre de la tabla que se accedera con el query select*from
    @whereTab   ->  Datos que van en la sentencia where sin hardcoding,
                    puede igual ponerse operaciones de orden
    @dataWhere  ->  Tupla de datos que van en el where
"""
def select_query_2_with_where(conexion,selectArg,table,whereTab,dataWhere):
    cursorTable=conexion.cursor()
    cursorTable.execute(f'SELECT {selectArg} FROM {table} WHERE {whereTab}',dataWhere)
    return cursorTable.fetchall()

"""
    @conexion   ->  Es la conexion a la base de datos existente gracias al create_database
    @table      ->  Es el nombre de la tabla que se accedera con el query select*from
    @whereTab   ->  Datos que van en la sentencia where sin hardcoding
    @dataWhere  ->  Tupla de datos que van en el where
"""
def delete_from(conexion,table,whereTab,dataWhere):
    cursorTable=conexion.cursor()
    cursorTable.execute(f'DELETE FROM {table} where {whereTab}',dataWhere)
    conexion.commit()


def update_data(conexion,table,dataSet,whereTab,data):
    cursorTable=conexion.cursor()
    cursorTable.execute(f'UPDATE {table} SET {dataSet} where {whereTab}',data)
    conexion.commit()
