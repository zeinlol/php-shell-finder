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
from pprint import pprint

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


def split_lists(target_list: list[list]) -> list[str]:
    return [item for sublist in target_list for item in sublist]


def look_for_shells(target_folder: str):
    # [ KNOWN ISSUES ] - [BEGIN]
    os.system(f'find {target_folder} -name "*".php -type f -print0 | xargs -0 grep r57 | uniq -c | sort -u | uniq|'
              ' cut -d":" -f1')
    # '  | awk \'{print "R57 Shell in PHP file --> rm -rf " $2}\'| uniq')

    os.system(f'find {target_folder} -name "*".txt -type f -print0 | xargs -0 grep r57 | uniq -c | sort -u | uniq|'
              ' cut -d":" -f1  | awk \'{print "R57 Shell in TXT file --> rm -rf " $2}\' | uniq')

    os.system(f'find {target_folder} -name "*".php  -type f -print0  | xargs -0 grep c99 | uniq -c  | sort -u  | uniq|'
              ' cut -d":" -f1  | awk \'{print "Possible C99 [PHP] --> rm -rf " $2}\' | uniq')

    os.system(f'find {target_folder} -name "*".txt  -type f -print0  | xargs -0 grep c99 | uniq -c  | sort -u  | uniq|'
              ' cut -d":" -f1  | awk \'{print "Possible C99 [TXT] --> rm -rf " $2}\' | uniq')

    os.system(f'find {target_folder} -name "*".php  -type f -print0  | xargs -0 grep c100 | uniq -c  | sort -u  | uniq|'
              ' cut -d":" -f1  | awk \'{print "Possible C100 [PHP] --> rm -rf " $2}\' | uniq')

    os.system(f'find {target_folder} -name "*".txt  -type f -print0  | xargs -0 grep c100 | uniq -c  | sort -u  | uniq|'
              ' cut -d":" -f1  | awk \'{print "Possible C100 [TXT] --> rm -rf " $2}\' | uniq')

    os.system(f'find {target_folder} -name "*".php  -type f -print0  | xargs -0 grep c98 | uniq -c  | sort -u  | uniq|'
              ' cut -d":" -f1  | awk \'{print "Possible C98 [PHP] --> rm -rf " $2}\' | uniq')

    os.system(
        f'find {target_folder} -name "*".txt  -type f -print0  | xargs -0 grep -n c98 | uniq -c  | sort -u  | uniq|'
        ' cut -d":" -f1  | awk \'{print "Possible C98 [TXT] --> rm -rf " $2}\' | uniq')

    os.system(f'find {target_folder} -name "*".php  -type f -print0  | xargs -0 grep -n SE3lRVER | uniq -c  |'
              ' sort -u  | uniq| awk \'{print "Possible WEEVELY SHELL [PHP]'
              ' --> rm -rf " $2}\' | uniq')
    # [ KNOWN ISSUES ] - [END]

    if args.clean_output:
        print(other_findings)

    # [ ANOTHER ISSUES ] - [BEGIN]
    commands_for_possible_shells = [
        f'find {target_folder} -name "*".php -type f -print0 | xargs -0 grep -n shell | sort -u | uniq',
        f'find {target_folder} -name "*".php -type f -print0 | xargs -0 grep -n backdoor | sort -u | uniq',
        f'find {target_folder} -name "*".php -type f -print0 | xargs -0 grep -n stealth | sort -u | uniq',
        f'find {target_folder} -name "*".php -type f -print0 | xargs -0 grep -n exec | sort -u | uniq',
        f'find {target_folder} -name "*".php -type f -print0 | xargs -0 grep -n popen | sort -u | uniq',
        f'find {target_folder} -name "*".php -type f -print0 | xargs -0 grep -n proc_open | sort -u | uniq',
        f'find {target_folder} -name "*".php -type f -print0 | xargs -0 grep -n symlink | sort -u | uniq',
        f'find {target_folder} -name "*".php -type f -print0 | xargs -0 grep -n passthru | sort -u | uniq',
        f'find {target_folder} -name "*".php -type f -print0 | xargs -0 grep -n system | sort -u | uniq',
        f'find {target_folder} -name "*".php -type f -print0 | xargs -0 grep -n milw0rm | sort -u | uniq',
    ]
    found_data = []
    for command in commands_for_possible_shells:
        possible_shell = os.popen(command).read()
        findings = possible_shell.split('\n')
        if len(findings) > 1:
            found_data.append(findings)
    # possible_shells = split_lists(found_data)
    possible_shells = found_data

    # pprint(possible_shells)
    
    # [ ANOTHER ISSUES ] - [END]
    for el in possible_shells:
        for shell in el:
            print(shell)


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
