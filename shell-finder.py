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
from sources.middleware import get_target, print_found_data, print_data_as_json, print_data_to_file
from sources.shells_engine import look_for_shells
from sources.text_variables import logo, warning, start_scan, scan_finished


def main():
    if not args.clean_output or args.output == '':
        print(logo)
        print(warning)

    target = get_target(args.target)

    if not args.clean_output or args.output == '':
        print(start_scan)
    shells = look_for_shells(target)
    if args.output == '':
        if args.json:
            print_data_as_json(shells)
        else:
            print_found_data(shells)
    else:
        print_data_to_file(data=shells, output_file=args.output)

    if not args.clean_output or args.output == '':
        print(scan_finished)


if __name__ == "__main__":
    main()
