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
from text_variables import logo, warning, start_scan, scan_finished, other_findings, get_target_text, args


def get_target(target: str) -> str:
    if target == '':
        target = input(get_target_text)
    if target == "":
        target = "/var/www/"
    if target[-1:] != "/":
        target += "/"
    # print(f'{target=}')
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
    # [ KNOWN ISSUES ] - [END]

    if args.clean_output:
        print(other_findings)

    os.system('find ' + target_folder + ' -name "*".php  -type f -print0  | xargs -0 grep milw0rm | uniq -c  |'
                                        ' sort -u  | cut -d":" -f1  | awk \'{print "Possible Shell [PHP]'
                                        ' --> rm -rf " $2}\' | uniq')


def main():
    if args.clean_output:
        print(logo)
        print(warning)

    target = get_target(args.target)

    if args.clean_output:
        print(start_scan)
    look_for_shells(target)

    if args.clean_output:
        print(scan_finished)


if __name__ == "__main__":
    main()
