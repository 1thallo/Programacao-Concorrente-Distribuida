""" 
Escreva código-fonte em python para determinar, em MB, quanto de memória física e quanto de
memória virtual está consumindo o processo cujo PID é igual a 0.
"""

import psutil
def obter_memoria_processo(pid):
    try:
        # Obter informações do processo
        processo = psutil.Process(pid)
        memoria_info = processo.memory_info()
        # Converter para MB
        memoria_fisica_mb = memoria_info.rss / (1024 * 1024) # Resident Set Size
        memoria_virtual_mb = memoria_info.vms / (1024 * 1024) # Virtual Memory Size
        return memoria_fisica_mb, memoria_virtual_mb
    except psutil.NoSuchProcess:
        return None, None