"""Crie um programa que liste todos os processos ativos no sistema, exibindo seus PIDs, nomes e estados (ex.: "running", "sleeping")."""

import psutil 

for proc in psutil.process_iter(['pid', 'name', 'status']):
	try:
		print(f"PID: {proc.info['pid']}, Nome: {proc.info['name']}, Status: {proc.info['status']}")
	except (psutil.NoSuchProcess):
		pass 

