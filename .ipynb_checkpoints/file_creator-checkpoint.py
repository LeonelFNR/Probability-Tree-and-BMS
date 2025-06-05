import inspect
import re
import numpy as np

def get_function_expression(func):
    #aconseguim codi de la funció
    source = inspect.getsource(func)

    #extraiem el que retorna a partir del "return" de funció original
    match = re.search(r'return (.+)', source)
    if match:
        expression = match.group(1)
        return expression
    return None
def sanitize_filename(filename):
    #substituïm els caràcters invàlids pel nom del fitxer
    filename = filename.replace('np.', '')
    #filename = filename.replace('*','.')
    
    filename = re.sub(r'[^a-zA-Z0-9\s\-_.()]+', '', filename)
    #filename = filename.replace('','')
    return filename