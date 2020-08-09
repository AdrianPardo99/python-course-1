#!/usr/bin/env python3
from databaseController import *

con=create_database("example.db")
create_table_with_params(con,"persona","nombre TEXT,apellidos TEXT,edad INTEGER")
insert_into_table(con,"persona","?,?,?",("Adrian","Gonzalez Pardo",21))
close_database(con)
