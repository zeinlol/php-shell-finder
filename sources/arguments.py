import argparse

parser = argparse.ArgumentParser(description='Tool for finding possible shells.')

parser.add_argument('--no-color', default=False, action='store_const', const=True,
                    help='Print text without colors')
parser.add_argument('--clean-output', default=False, action='store_const', const=True,
                    help="Don't print logo and other text. Just found data")
parser.add_argument('-t', '--target', default='',
                    help="Target folder with files for scan. If not indicated tool will ask to specify folder")
parser.add_argument('--json', default=False, action='store_const', const=True,
                    help='Print output as json')
parser.add_argument('-o', '--output', default='',
                    help='Print output to OUTPUT file')

args = parser.parse_args()
