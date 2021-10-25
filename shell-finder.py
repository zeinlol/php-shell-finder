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

from sources.arguments import args
from sources.middleware import get_target, print_found_data
from sources.shells_engine import look_for_shells
from sources.text_variables import logo, warning, start_scan, scan_finished


def main():
    if args.clean_output:
        print(logo)
        print(warning)

    target = get_target(args.target)

    if args.clean_output:
        print(start_scan)
    shells = look_for_shells(target)
    if args.json:
        ...
    else:
        print_found_data(shells)

    if args.clean_output:
        print(scan_finished)


if __name__ == "__main__":
    main()
