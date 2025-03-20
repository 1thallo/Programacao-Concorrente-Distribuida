"""Programa que recebe o PID de um processo e exibe
seu estado atual (ex.: em execução, parado, suspenso)"""
import psutil

def estado_processo(pid):
    try:
        processo = psutil.Process(pid)
        estado = processo.status()
        return estado
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
        return "Processo nao encontrado"
    
pid = int(input("Digite o numero do processo: "))

estado = estado_processo(pid)

print(f"O estado do processo com PID {pid} é {estado}!")