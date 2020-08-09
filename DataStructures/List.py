#!/usr/bin/env python3

listStructure=list()
for i in range(10):
    listStructure.append(f'val{i+1}')

print(f'Structure List: {listStructure}')
print(f'Val 0 in list? {"val0" in listStructure}')
print(f'Val 1 in list? {"val1" in listStructure}')
listStructure.remove("val1")
print(f'Delete val1: {listStructure}')
