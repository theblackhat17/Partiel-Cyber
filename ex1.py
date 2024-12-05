import subprocess
import os

def block_usb_ports():
    if os.name == 'posix':
        subprocess.run(['sudo', 'modprobe', '-r', 'usb_storage'], check=True)

def configure_firewall():
    if os.name == 'posix':
        subprocess.run(['sudo', 'iptables', '-P', 'INPUT', 'DROP'], check=True)
        subprocess.run(['sudo', 'iptables', '-P', 'OUTPUT', 'DROP'], check=True)
        subprocess.run(['sudo', 'iptables', '-P', 'FORWARD', 'DROP'], check=True)

def reset_firewall():
    if os.name == 'posix':
        subprocess.run(['sudo', 'iptables', '-P', 'INPUT', 'ACCEPT'], check=True)
        subprocess.run(['sudo', 'iptables', '-P', 'OUTPUT', 'ACCEPT'], check=True)
        subprocess.run(['sudo', 'iptables', '-P', 'FORWARD', 'ACCEPT'], check=True)

if __name__ == '__main__':
    block_usb_ports()
    configure_firewall()
    reset_firewall
