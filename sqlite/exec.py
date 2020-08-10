#!/usr/bin/env python3
from databaseController import *

con=create_database("example.db")
create_table_with_params(con,"persona","nombre TEXT,apellidos TEXT,edad INTEGER")
listaDatos=[("Juan","Martinez",19),("Raymundo","Pulido",21),("Melani","Valdez",22)]
#print(f'{type(listaDatos) is list}\n{type(listaDatos[0])}')
#insert_into_table(con,"persona","?,?,?",listaDatos)
for row in select_query_all(con,"persona"):
    print(f'{row}')

print("\n\n")
for row in select_query_all_with_where(con,"persona","edad>=?",(20,)):
    print(f'{row}')

print("\n\n\n")
for row in select_query_2_with_where(con,"edad","persona","edad>=?",(20,)):
    print(f'{row}')

print("\n\n\n")
delete_from(con,"persona","edad=?",(19,))
for row in select_query_all(con,"persona"):
    print(f'{row}')

print("\n\n\n")
update_data(con,"persona","apellidos=?","nombre=?",("González Pardo","Adrian"))
for row in select_query_all(con,"persona"):
    print(f'{row}')
close_database(con)
