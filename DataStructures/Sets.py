#!/usr/bin/env python3

setStructure=set()
for i in range(10):
    setStructure.add(f'value {i+1}')

print(f'Set structure: {setStructure}\nDelete value value 5')
setStructure.remove("value 5")
print(f'Set structure modify: {setStructure}')
