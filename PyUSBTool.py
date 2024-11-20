


#-------------------
import os          
import subprocess   
import shutil       
import psutil       
import progressbar  
import time         
#-------------------
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
#------------------
def print_banner():
    banner = f"""
    {BOLD}{CYAN}########################################
    #         PyUSBTool - USB Formatter    #
    #        A simple and powerful tool    #
    #         for USB drive formatting     #
    ########################################{RESET}
    [+]created by i-100-user
    [+]https://github.com/i-100-user
    """
    print(banner)

print_banner()
#-----------------
def list_usb_drives():
    drives = psutil.disk_partitions()
    usb_drives = []
    for drive in drives:
        if ('sda' in drive.device or 'sdb' in drive.device) and 'loop' not in drive.device:
            usb_drives.append(drive)
#----------------



    print(f"\n{BOLD}{CYAN}--------- Dispositivos USB conectados ---------{RESET}")
    if usb_drives:
        print(f"{'Nº':<5} {'Dispositivo':<15} {'Ruta de montaje':<30}")
        print("-" * 50)
        for index, drive in enumerate(usb_drives, start=1):
            print(f"{index:<5} {drive.device:<15} {drive.mountpoint:<30}")
    else:
        print(f"{RED}[INFO] No se encontraron unidades USB conectadas.{RESET}")

    return usb_drives
#---------------



def select_usb_to_format(usb_drives):
    while True:
        try:
            choice = int(input(f"{YELLOW}[INFO] Elige el número del dispositivo USB a formatear: {RESET}"))
            if 1 <= choice <= len(usb_drives):
                selected_drive = usb_drives[choice - 1]
                print(f"{GREEN}[INFO] Has seleccionado: {selected_drive.device} ({selected_drive.mountpoint}){RESET}")
                return selected_drive
            else:
                print(f"{RED}[ERROR] Opción no válida. Intenta de nuevo.{RESET}")
        except ValueError:
            print(f"{RED}[ERROR] Por favor, ingresa un número válido.{RESET}")
#---------------


def confirm_and_format(drive):
    
    print(f"\n{YELLOW}[WARNING] ¡Advertencia! Todo el contenido de {drive.device} será borrado.{RESET}")
    confirmation = input(f"{CYAN}[INFO] ¿Estás seguro de que deseas continuar? (Y/N): {RESET}").strip().upper()

#--------------


    if confirmation == 'Y':
        print(f"{GREEN}[INFO] Formateando {drive.device}... Esto eliminará todos los datos.{RESET}")
        
        
        try:
            if drive.device in [part.device for part in psutil.disk_partitions()]:
                print(f"{CYAN}[INFO] Desmontando {drive.device}...{RESET}")
                subprocess.run(["sudo", "umount", "-l", drive.device], check=True)
                print(f"{GREEN}[INFO] {drive.device} desmontado con éxito.{RESET}")
            else:
                print(f"{GREEN}[INFO] {drive.device} ya está desmontado.{RESET}")
        except subprocess.CalledProcessError:
            print(f"{RED}[ERROR] No se pudo desmontar {drive.device}. Es posible que esté ocupado por un proceso.{RESET}")
            return

#--------------


        
        widgets = ['Formateando: ', progressbar.Percentage(), ' ', progressbar.Bar()]
        bar = progressbar.ProgressBar(widgets=widgets, maxval=100).start()
        
        for i in range(100):
            bar.update(i + 1)  
            time.sleep(0.05)  

        bar.finish()


        try:
            subprocess.run(["sudo", "mkfs.vfat", "-F", "32", drive.device], check=True)
            print(f"{GREEN}[INFO] {drive.device} ha sido formateado exitosamente.{RESET}")
        except subprocess.CalledProcessError:
            print(f"{RED}[ERROR] Ocurrió un error al formatear {drive.device}.{RESET}")
    elif confirmation == 'N':
        print(f"{YELLOW}[INFO] El formateo ha sido cancelado.{RESET}")
    else:
        print(f"{RED}[ERROR] Opción no válida. El formateo ha sido cancelado.{RESET}")

#----------------



def main():
    usb_drives = list_usb_drives()
    if usb_drives:
        selected_drive = select_usb_to_format(usb_drives)
        confirm_and_format(selected_drive)
    else:
        print(f"{RED}[INFO] No se encontraron unidades USB conectadas.{RESET}")


if __name__ == "__main__":
    main()
#----------------
