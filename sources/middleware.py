import json
from typing import Union

from sources.arguments import args
from sources.text_variables import get_target_text, color


def get_target(target: str) -> str:
    if not target:
        target = input(get_target_text)
    if target == "":
        target = "/var/www/"
    if target[-1:] != "/":
        target += "/"
    print(f'{target=}')
    return target


def split_lists(target_list: list[list]) -> list[str]:
    return [item for sublist in target_list for item in sublist]


def print_found_data(shells: list[str]) -> None:
    for shell in shells:
        if 'Possible' in shell:
            shell = color.YELLOW + shell + color.END
        else:
            shell = color.RED + shell + color.END
        print(shell)


def convert_data_to_dict(shells: list[str]) -> list[dict]:
    formatted_shells = []
    for shell in shells:
        shell = shell.split(':')

        if len(shell) > 4:  # if ':' in code script will cat part of code, this IF fix this issue
            shell[3] = ''.join(shell[3:])

        dict_shell = {
            'title': shell[0],
            'file': shell[1][1:],
            'code_line': shell[2],
            'code': shell[3],
        }
        formatted_shells.append(dict_shell)
    # print(formatted_shells)

    return formatted_shells


def print_data_as_json(shells: list[str]) -> None:
    shells = convert_data_to_dict(shells)
    print(json.dumps(shells))


def print_data_to_file(data: Union[list[str], list[dict]], output_file: str) -> None:

    with open(output_file, 'w') as file:
        if args.json:
            data = convert_data_to_dict(data)
            json.dump(data, file, indent=2)
        else:
            data = '\n'.join(data)
            file.write(str(data))
        file.close()
