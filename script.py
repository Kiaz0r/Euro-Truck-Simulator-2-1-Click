import os
import subprocess
import time
import psutil
from colorama import init, Fore

init()

multimonitortool_path = "C:\\Programas\\MultiMonitorTool\\MultiMonitorTool.exe"
fanaleds_path = "C:\\Programas\\FanaLEDs\\FanaLEDs.exe"
simdashboard_path = "C:\\Programas\\SIM Dashboard Server\\SIMDashboardServer.exe"


def print_with_dots(message, monitor_name=None, color=None):
    if monitor_name is not None:
        message = f"{message} {monitor_name}"
    if color:
        print(color + message, end="")
    else:
        print(message, end="")
    for _ in range(3):
        time.sleep(0.5)
        if color:
            print(color + ".", end="", flush=True)
        else:
            print(".", end="", flush=True)
    if color:
        print(Fore.RESET)
    else:
        print()


def set_primary_monitor(monitor_number):
    monitor_name = "LG UltraWide" if monitor_number == 2 else "LG UltraGear"
    print_with_dots("Alterando para monitor", monitor_name)
    try:
        subprocess.run([multimonitortool_path, "/SetPrimary",
                       str(monitor_number)], check=True)
    except subprocess.CalledProcessError:
        pass


def start_application(app_path, minimized=False):
    print_with_dots(f"Iniciando {app_path}")
    try:
        if minimized:
            subprocess.Popen(
                app_path, creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            return subprocess.Popen(app_path)
    except Exception:
        pass


def is_process_running(process_name):
    try:
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == process_name:
                return proc
    except Exception:
        pass
    return False


def stop_process(process_name):
    print_with_dots(f"Finalizando {process_name}")
    process = is_process_running(process_name)
    if process:
        try:
            process.terminate()
            process.wait()
        except psutil.NoSuchProcess:
            pass
        except Exception:
            pass


set_primary_monitor(2)

fanaleds_process = start_application(fanaleds_path)
simdashboard_process = start_application(simdashboard_path, minimized=True)

ets2_process = None
print_with_dots("Iniciando Euro Truck Simulator 2")
try:
    ets2_process = subprocess.Popen(
        "cmd /c start steam://rungameid/227300", shell=True)
except Exception:
    pass

timeout = 60
interval = 5
elapsed = 0
ets2_process_check = False

while elapsed < timeout:
    ets2_process_check = is_process_running("eurotrucks2.exe")
    if ets2_process_check:
        print_with_dots(
            "Não feche essa janela enquanto o jogo estiver em execução", color=Fore.GREEN)
        break
    time.sleep(interval)
    elapsed += interval

if ets2_process_check:
    ets2_process_check.wait()

stop_process("FanaLEDs.exe")
stop_process("SIMDashboardServer.exe")

set_primary_monitor(1)

print_with_dots("Configurações restauradas")
