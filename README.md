# PHP Shell Finder
Shell finder for PHP projects on python3

Forked from [alvarodh5/Shell-Finder](https://github.com/alvarodh5/Shell-Finder)

Updated for python3.9

Tool is rewrote for a better experience

## About
This is Python3.9 script that is in charge of searching all type of backdoors in the directory that you indicate (by default it will be /var/www/), I have not been able to dedicate all the time that I would like, but I think it works quite well and it is very simple to add more search values.

## Installing
```git
git clone https://github.com/zeinlol/php-shell-finder
```

## Run
```angular2html
python3 shell-finder.py [-h] [--no-color] [--clean-output] [-t TARGET] [--json]

Tool for finding possible shells.

optional arguments:
  -h, --help            show this help message and exit
  --no-color            Print text without colors
  --clean-output        Don't print logo and other text. Just found data
  -t TARGET, --target TARGET
                        Target folder with files for scan. If not indicated
                        tool will ask to specify folder
  --json                Print output as json
  -o OUTPUT, --output OUTPUT
                        Print output to OUTPUT file
```
Use sudo, if you are going to scan directories that do not belong to the user running it.
