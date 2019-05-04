#!/usr/bin/env python
import psutil
import sys

def GetCPU():
	cpu = psutil.cpu_times()
	cpu_idle = cpu[3]
	cpu_user = cpu[0]
	cpu_guest = cpu[8]
	cpu_iowait = cpu[4]
	cpu_stolen = cpu[1]
	cpu_system = cpu[2]
	print('system.cpu.idle {0}\nsystem.cpu.user {1}\nsystem.cpu.guest {2}\nsystem.cpu.iowait {3}\nsystem.cpu.stolen {4}\nsystem.cpu.system {5}\n'.format(cpu_idle, cpu_user, cpu_guest, cpu_iowait, cpu_stolen, cpu_system))
	return;

def GetMem():
	vm = psutil.virtual_memory()
	vm_total = vm[0]
	vm_used = vm[3]
	vm_free = vm[4]
	vm_shared = vm[9]
	
	swap = psutil.swap_memory()
	swap_total = swap[0]
	swap_used = swap[1]
	swap_free = swap[2]
	print('virtual total {0}\nvirtual used {1}\nvirtual free {2}\nvirtual shared {3}\nswap total {4}\nswap used {5}\nswap free {6}\n'.format(vm_total, vm_used, vm_free, vm_shared, swap_total, swap_used, swap_free))
	return;

if len(sys.argv) > 1:
    argument = sys.argv[1]
else: argument = ''

if argument == 'cpu':
	GetCPU()
elif argument == 'mem':
	GetMem()
