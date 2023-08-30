
import sys
print("Versión de Python:", sys.version)

import sys
print("Antes de la terminación")
sys.exit()  
print("Después de la terminación") 

import sys
original_stdout = sys.stdout
with open('output.txt', 'w') as f:
    sys.stdout = f
    print("Este texto se escribirá en output.txt en lugar de la consola.")
sys.stdout = original_stdout