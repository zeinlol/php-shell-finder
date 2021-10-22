#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: @alvarodh5 | Blackdrake

#########################################################################################################
#                                            Shell Finder Python                                        #
#                                                                                                       #
#                                        coded by Blackdrake for Underc0de                              #
#                                                                                                       #
#                                                05/06/2015                                             #
#                                                                                                       #
#                                     Underc0de.org | twitter.com/alvarodh5                             #
#                                                                                                       #
#                                           Run this tool as root                                       #
#########################################################################################################

import os


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


print
color.BLUE + " __ _          _ _     ___ _           _" + color.END
print
color.BLUE + "/ _\ |__   ___| | |   / __( )_ __   __| | ___ _ __ " + color.END
print
color.BLUE + "\ \| '_ \ / _ \ | |  / _\ | | '_ \ / _` |/ _ \ '__|" + color.END
print
color.BLUE + "_\ \ | | |  __/ | | / /   | | | | | (_| |  __/ | " + color.END
print
color.BLUE + "\__/_| |_|\___|_|_| \/    |_|_| |_|\__,_|\___|_| " + color.END
print
""
print
color.YELLOW + "By Blackdrake (@alvarodh5) para Underc0de" + color.END
print
""
print
color.GREEN + "Asegurese que los ficheros que detecta son ilegitimos antes de eliminarlos" + color.END
print
color.GREEN + "Tenga en cuenta, que dependiendo de la cantidad de ficheros que tenga en su servidor, el script tardara mas o menos" + color.END
raw_input("[Pulse INTRO para continuar]")
print
color.GREEN + "Introduzca ruta del directorio donde aloja sus ficheros (Pulsa Intro para utilizar por defecto, /var/www/)" + color.END
directorio = raw_input("")
if (directorio == ""):
    directorio = "/var/www/"
else:
    longitud = len(directorio) - 1
    if not (directorio[longitud] == "/"):
        directorio += "/"

print
color.BLUE + "Buscando Shells conocidas" + color.END + "" + color.RED
os.system(
    'find ' + directorio + ' -name "*".php  -type f -print0  | xargs -0 grep r57 | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible R57 [PHP] --> rm -rf " $2}\'| uniq')

os.system(
    'find ' + directorio + ' -name "*".txt  -type f -print0  | xargs -0 grep r57 | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible R57 [TXT] --> rm -rf " $2}\' | uniq')

os.system(
    'find ' + directorio + ' -name "*".php  -type f -print0  | xargs -0 grep c99 | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible C99 [PHP] --> rm -rf " $2}\' | uniq')

os.system(
    'find ' + directorio + ' -name "*".txt  -type f -print0  | xargs -0 grep c99 | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible C99 [TXT] --> rm -rf " $2}\' | uniq')

os.system(
    'find ' + directorio + ' -name "*".php  -type f -print0  | xargs -0 grep c100 | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible C100 [PHP] --> rm -rf " $2}\' | uniq')

os.system(
    'find ' + directorio + ' -name "*".txt  -type f -print0  | xargs -0 grep c100 | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible C100 [TXT] --> rm -rf " $2}\' | uniq')

os.system(
    'find ' + directorio + ' -name "*".php  -type f -print0  | xargs -0 grep c98 | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible C98 [PHP] --> rm -rf " $2}\' | uniq')

os.system(
    'find ' + directorio + ' -name "*".txt  -type f -print0  | xargs -0 grep c98 | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible C98 [TXT] --> rm -rf " $2}\' | uniq')

os.system(
    'find ' + directorio + ' -name "*".php  -type f -print0  | xargs -0 grep SE3lRVER | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible WEEVELY SHELL [PHP] --> rm -rf " $2}\' | uniq')

print
color.END + color.BLUE + "Otros posibles casos de Shell" + color.END + "" + color.YELLOW

os.system(
    'find ' + directorio + ' -name "*".php  -type f -print0  | xargs -0 grep shell | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible Shell [PHP] --> rm -rf " $2}\' | uniq')

os.system(
    'find ' + directorio + ' -name "*".php  -type f -print0  | xargs -0 grep backdoor | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible Shell [PHP] --> rm -rf " $2}\' | uniq')

os.system(
    'find ' + directorio + ' -name "*".php  -type f -print0  | xargs -0 grep stealth | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible Shell [PHP] --> rm -rf " $2}\' | uniq')

os.system(
    'find ' + directorio + ' -name "*".php  -type f -print0  | xargs -0 grep exec | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible Shell [PHP] --> rm -rf " $2}\' | uniq')

os.system(
    'find ' + directorio + ' -name "*".php  -type f -print0  | xargs -0 grep popen | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible Shell [PHP] --> rm -rf " $2}\' | uniq')

os.system(
    'find ' + directorio + ' -name "*".php  -type f -print0  | xargs -0 grep proc_open | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible Shell [PHP] --> rm -rf " $2}\' | uniq')

os.system(
    'find ' + directorio + ' -name "*".php  -type f -print0  | xargs -0 grep symlink | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible Shell [PHP] --> rm -rf " $2}\' | uniq')

os.system(
    'find ' + directorio + ' -name "*".php  -type f -print0  | xargs -0 grep passthru | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible Shell [PHP] --> rm -rf " $2}\' | uniq')

os.system(
    'find ' + directorio + ' -name "*".php  -type f -print0  | xargs -0 grep system | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible Shell [PHP] --> rm -rf " $2}\' | uniq')

os.system(
    'find ' + directorio + ' -name "*".php  -type f -print0  | xargs -0 grep milw0rm | uniq -c  | sort -u  | cut -d":" -f1  | awk \'{print "Posible Shell [PHP] --> rm -rf " $2}\' | uniq')

print
color.END + color.GREEN + "Escaner finalizado, siguenos! @underc0de @alvarodh5 " + color.END
