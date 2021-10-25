from arguments import args
from classes import FakeColorCode, ColorCode

color = FakeColorCode if args.no_color else ColorCode
logo = f"{color.BLUE} __ _          _ _     ___ _           _{color.END}\n" \
       f"{color.BLUE}/ _\ |__   ___| | |   / __( )_ __   __| | ___ _ __{color.END}\n" \
       f"{color.BLUE}\\ \| '_ \ / _ \ | |  / _\ | | '_ \ / _` |/ _ \\ '__|'{color.END}\n" \
       f"{color.BLUE}_\ \ | | |  __/ | | / /   | | | | | (_| |  __/ | {color.END}\n" \
       f"{color.BLUE}\__/_| |_|\___|_|_| \/    |_|_| |_|\__,_|\___|_| {color.END}\n" \
       f"{color.YELLOW}By Zeinlol from Blackdrake (@alvarodh5){color.END}"
warning = f"{color.GREEN}Make sure the files it detects are illegitimate before deleting them{color.END}" \
          f"{color.GREEN}Keep in mind, that depending on the amount of files you have on your server, the " \
          f"script will take more or less time{color.END}"
start_scan = f'{color.BLUE}Start looking for known Shells...{color.END}'
scan_finished = f'{color.GREEN}Scanner finished, follow us! @underc0de @alvarodh5 @zeinlol{color.END}'
get_target_text = f"{color.GREEN}Enter the path of the directory where you host your files " \
                  f"(Press Enter to use /var/www/ by default):{color.END}"
