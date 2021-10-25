from text_variables import get_target_text, color


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


def print_found_data(shells: list[str]) -> None:
    for shell in shells:
        if 'Possible' in shell:
            shell = color.YELLOW + shell + color.END
        else:
            shell = color.RED + shell + color.END
        print(shell)
