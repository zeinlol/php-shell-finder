import argparse

parser = argparse.ArgumentParser(description='Tool for finding possible shells.')

parser.add_argument('--no-color', default=False, action='store_const', const=True,
                    help='Print text without colors. Default is False.')
parser.add_argument('--clean-output', default=True, action='store_const', const=False,
                    help="Don't print logo and other text. Just found data. Default is False.")
parser.add_argument('-t', '--target', default='',
                    help="Target folder with files for scan.")
parser.add_argument('--json', default=False, action='store_const', const=True,
                    help='Print text without colors. Default is False.')

args = parser.parse_args()
