#!/usr/bin/env python3
from databaseController import *

con=create_database("example.db")
create_table_with_params(con,"persona","nombre TEXT,apellidos TEXT,edad INTEGER")
listaDatos=[("Juan","Martinez",19),("Raymundo","Pulido",21),("Melani","Valdez",22)]
#print(f'{type(listaDatos) is list}\n{type(listaDatos[0])}')
insert_into_table(con,"persona","?,?,?",listaDatos)
close_database(con)
