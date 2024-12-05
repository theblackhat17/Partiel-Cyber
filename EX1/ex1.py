import subprocess
import os

def block_usb_ports():
    if os.name == 'posix':
        print("Tentative de blocage des ports USB...")
        try:
            result = subprocess.run(['sudo', 'modprobe', '-r', 'usb_storage'], check=True, capture_output=True, text=True)
            print("Les ports USB ont été bloqués avec succès")
            print("Sortie de la commande :", result.stdout)
        except subprocess.CalledProcessError as e:
            print("Erreur lors du blocage des ports USB :", e.stderr)

def configure_firewall():
    if os.name == 'posix':
        print("Configuration du pare-feu pour bloquer tout le trafic réseau...")
        try:
            subprocess.run(['sudo', 'iptables', '-P', 'INPUT', 'DROP'], check=True)
            subprocess.run(['sudo', 'iptables', '-P', 'OUTPUT', 'DROP'], check=True)
            subprocess.run(['sudo', 'iptables', '-P', 'FORWARD', 'DROP'], check=True)
            print("Le pare-feu a été configuré pour bloquer tout le trafic")
        except subprocess.CalledProcessError as e:
            print("Erreur lors de la configuration du pare-feu :", e)

def reset_firewall():
    if os.name == 'posix':
        print("Réinitialisation du pare-feu...")
        try:
            subprocess.run(['sudo', 'iptables', '-P', 'INPUT', 'ACCEPT'], check=True)
            subprocess.run(['sudo', 'iptables', '-P', 'OUTPUT', 'ACCEPT'], check=True)
            subprocess.run(['sudo', 'iptables', '-P', 'FORWARD', 'ACCEPT'], check=True)
            print("Le pare-feu a été réinitialisé avec succès.")
        except subprocess.CalledProcessError as e:
            print("Erreur lors de la réinitialisation du pare-feu :", e)

if __name__ == '__main__':
    block_usb_ports()
    configure_firewall()