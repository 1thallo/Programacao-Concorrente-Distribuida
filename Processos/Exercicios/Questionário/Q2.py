"""Desenvolva um script que identifique o processo que está consumindo mais CPU no momento."""
import psutil
import time

def top_cpu_process():
    # inicializa
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent(interval=None)
        except Exception:
            pass

    time.sleep(0.01)

    max_cpu = 0
    top_proc = None

    # verifica
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            cpu = proc.cpu_percent(interval=None)
        except Exception:
            continue
        top_proc, max_cpu = (proc, cpu) if cpu > max_cpu else (top_proc, max_cpu)  # operador ternário

    return top_proc, max_cpu

proc, cpu_usage = top_cpu_process()
print(f"Processo: PID={proc.pid}, Nome={proc.name()}, Uso de CPU={cpu_usage}%") if proc else print("Nenhum processo encontrado.")
