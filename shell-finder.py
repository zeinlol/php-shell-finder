#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: @alvarodh5 | Blackdrake | zeinlol

#########################################################################################################
#                                            Shell Finder Python                                        #
#                                                                                                       #
#                                        coded by Blackdrake for Underc0de                              #
#                                               redone by zeinlol                                       #
#                                                                                                       #
#                                                    2021                                               #
#                                                                                                       #
#                                     Underc0de.org | twitter.com/alvarodh5                             #
#                                     Zeinlol |  https://github.com/zeinlol                             #
#                                                                                                       #
#                                           Run this tool as root                                       #
#########################################################################################################

import os
import argparse

from classes import ColorCode, FakeColorCode

parser = argparse.ArgumentParser(description='Tool for finding possible shells.')
parser.add_argument('--no-color', type=bool, default=False,
                    help='Print text with colors. Default is False.')

args = parser.parse_args()

if args.no_color:
    color = FakeColorCode
else:
    color = ColorCode

logo = f"{color.BLUE} __ _          _ _     ___ _           _{color.END}\n" \
       f"{color.BLUE}/ _\ |__   ___| | |   / __( )_ __   __| | ___ _ __{color.END}\n" \
       f"{color.BLUE}\\ \| '_ \ / _ \ | |  / _\ | | '_ \ / _` |/ _ \\ '__|'{color.END}\n" \
       f"{color.BLUE}_\ \ | | |  __/ | | / /   | | | | | (_| |  __/ | {color.END}\n" \
       f"{color.BLUE}\__/_| |_|\___|_|_| \/    |_|_| |_|\__,_|\___|_| {color.END}\n" \
       f"{color.YELLOW}By Zeinlol forked from Blackdrake (@alvarodh5){color.END}"

warning = f"{color.GREEN}Make sure the files it detects are illegitimate before deleting them{color.END}" \
          f"{color.GREEN}Keep in mind, that depending on the amount of files you have on your server, the " \
          f"script will take more or less time{color.END}"


def get_target() -> str:
    target = input(f"{color.GREEN}Enter the path of the directory where you host your files "
                   f"(Press Enter to use /var/www/ by default):{color.END}")
    if target == "":
        target = "/var/www/"
    elif target[-1:] != "/":
        target += "/"
    print(f'{target=}')
    return target


def look_for_shells(target_folder: str):
    os.system('find ' + target_folder + ' -name "*".php  -type f -print0  | xargs -0 grep r57 | uniq -c  | sort -u  |'
                                        ' cut -d":" -f1  | awk \'{print "Possible R57 [PHP] --> rm -rf " $2}\'| uniq')

    os.system('find ' + target_folder + ' -name "*".txt  -type f -print0  | xargs -0 grep r57 | uniq -c  | sort -u  |'
                                        ' cut -d":" -f1  | awk \'{print "Possible R57 [TXT] --> rm -rf " $2}\' | uniq')

    os.system('find ' + target_folder + ' -name "*".php  -type f -print0  | xargs -0 grep c99 | uniq -c  | sort -u  |'
                                        ' cut -d":" -f1  | awk \'{print "Possible C99 [PHP] --> rm -rf " $2}\' | uniq')

    os.system('find ' + target_folder + ' -name "*".txt  -type f -print0  | xargs -0 grep c99 | uniq -c  | sort -u  |'
                                        ' cut -d":" -f1  | awk \'{print "Possible C99 [TXT] --> rm -rf " $2}\' | uniq')

    os.system('find ' + target_folder + ' -name "*".php  -type f -print0  | xargs -0 grep c100 | uniq -c  | sort -u  |'
                                        ' cut -d":" -f1  | awk \'{print "Possible C100 [PHP] --> rm -rf " $2}\' | uniq')

    os.system('find ' + target_folder + ' -name "*".txt  -type f -print0  | xargs -0 grep c100 | uniq -c  | sort -u  |'
                                        ' cut -d":" -f1  | awk \'{print "Possible C100 [TXT] --> rm -rf " $2}\' | uniq')

    os.system('find ' + target_folder + ' -name "*".php  -type f -print0  | xargs -0 grep c98 | uniq -c  | sort -u  |'
                                        ' cut -d":" -f1  | awk \'{print "Possible C98 [PHP] --> rm -rf " $2}\' | uniq')

    os.system('find ' + target_folder + ' -name "*".txt  -type f -print0  | xargs -0 grep c98 | uniq -c  | sort -u  |'
                                        ' cut -d":" -f1  | awk \'{print "Possible C98 [TXT] --> rm -rf " $2}\' | uniq')

    os.system('find ' + target_folder + ' -name "*".php  -type f -print0  | xargs -0 grep SE3lRVER | uniq -c  |'
                                        ' sort -u  | cut -d":" -f1  | awk \'{print "Possible WEEVELY SHELL [PHP]'
                                        ' --> rm -rf " $2}\' | uniq')
    print(f"{color.END}{color.BLUE}Other possible Shell cases:{color.END}{color.YELLOW}")
    os.system('find ' + target_folder + ' -name "*".php  -type f -print0  | xargs -0 grep shell | uniq -c  |'
                                        ' sort -u  | cut -d":" -f1  | awk \'{print "Possible Shell [PHP]'
                                        ' --> rm -rf " $2}\' | uniq')

    os.system('find ' + target_folder + ' -name "*".php  -type f -print0  | xargs -0 grep backdoor | uniq -c  |'
                                        ' sort -u  | cut -d":" -f1  | awk \'{print "Possible Shell [PHP]'
                                        ' --> rm -rf " $2}\' | uniq')

    os.system('find ' + target_folder + ' -name "*".php  -type f -print0  | xargs -0 grep stealth | uniq -c  |'
                                        ' sort -u  | cut -d":" -f1  | awk \'{print "Possible Shell [PHP]'
                                        ' --> rm -rf " $2}\' | uniq')

    os.system('find ' + target_folder + ' -name "*".php  -type f -print0  | xargs -0 grep exec | uniq -c  | '
                                        'sort -u  | cut -d":" -f1  | awk \'{print "Possible Shell [PHP] --> '
                                        'rm -rf " $2}\' | uniq')

    os.system('find ' + target_folder + ' -name "*".php  -type f -print0  | xargs -0 grep popen | uniq -c  |'
                                        ' sort -u  | cut -d":" -f1  | awk \'{print "Possible Shell [PHP]'
                                        ' --> rm -rf " $2}\' | uniq')

    os.system('find ' + target_folder + ' -name "*".php  -type f -print0  | xargs -0 grep proc_open | uniq -c  |'
                                        ' sort -u  | cut -d":" -f1  | awk \'{print "Possible Shell [PHP] --> rm -rf'
                                        ' " $2}\' | uniq')

    os.system('find ' + target_folder + ' -name "*".php  -type f -print0  | xargs -0 grep symlink | uniq -c  |'
                                        ' sort -u  | cut -d":" -f1  | awk \'{print "Possible Shell [PHP]'
                                        ' --> rm -rf " $2}\' | uniq')

    os.system('find ' + target_folder + ' -name "*".php  -type f -print0  | xargs -0 grep passthru | uniq -c  |'
                                        ' sort -u  | cut -d":" -f1  | awk \'{print "Possible Shell [PHP]'
                                        ' --> rm -rf " $2}\' | uniq')

    os.system('find ' + target_folder + ' -name "*".php  -type f -print0  | xargs -0 grep system | uniq -c  |'
                                        ' sort -u  | cut -d":" -f1  | awk \'{print "Possible Shell [PHP]'
                                        ' --> rm -rf " $2}\' | uniq')

    os.system('find ' + target_folder + ' -name "*".php  -type f -print0  | xargs -0 grep milw0rm | uniq -c  |'
                                        ' sort -u  | cut -d":" -f1  | awk \'{print "Possible Shell [PHP]'
                                        ' --> rm -rf " $2}\' | uniq')


def main():
    print(logo)
    print(warning)
    target = get_target()
    print(f'{color.BLUE}Start looking for known Shells...{color.END}{color.RED}')
    look_for_shells(target)
    print(f'{color.END}{color.GREEN}Scanner finished, follow us! @underc0de @alvarodh5 @zeinlol{color.END}')


if __name__ == "__main__":
    main()
