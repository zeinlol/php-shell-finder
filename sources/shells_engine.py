import os

from middleware import split_lists


def look_for_shells(target_folder: str) -> list[str]:
    found_data = []
    # [ KNOWN ISSUES ] - [BEGIN]
    known_shells = [
        ["R57 Shell in PHP file: ",
         f'find {target_folder} -name "*".php -type f -print0 | xargs -0 grep -n r57 | sort -u | uniq'],
        ["R57 Shell in TXT file: ",
         f'find {target_folder} -name "*".txt -type f -print0 | xargs -0 grep -n r57 | sort -u | uniq'],
        ["C99 Shell in PHP file: ",
         f'find {target_folder} -name "*".php -type f -print0 | xargs -0 grep -n c99 | sort -u | uniq'],
        ["C99 Shell in TXT file: ",
         f'find {target_folder} -name "*".txt -type f -print0 | xargs -0 grep -n c99 | sort -u | uniq'],
        ["WEEVELY SHELL in PHP file: ",
         f'find {target_folder} -name "*".php -type f -print0 | xargs -0 grep -n SE3lRVER | sort -u | uniq'],
        ["C98 Shell in TXT file: ",
         f'find {target_folder} -name "*".txt -type f -print0 | xargs -0 grep -n c98 | sort -u | uniq'],
        ["C98 Shell in PHP file: ",
         f'find {target_folder} -name "*".php -type f -print0 | xargs -0 grep -n c98 | sort -u | uniq'],
        ["C100 in TXT file: ",
         f'find {target_folder} -name "*".txt -type f -print0 | xargs -0 grep -n c100 | sort -u | uniq'],
        ["C100 Shell in PHP file: ",
         f'find {target_folder} -name "*".php -type f -print0 | xargs -0 grep -n c100 | sort -u | uniq'],
    ]
    for command in known_shells:
        possible_shell = os.popen(command[1]).read()
        findings = possible_shell.split('\n')
        if len(findings) > 1:
            findings = [command[0] + shell for shell in findings if shell != '']
            found_data.append(findings)
    # [ KNOWN ISSUES ] - [END]

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
    for command in commands_for_possible_shells:
        possible_shell = os.popen(command).read()
        findings = possible_shell.split('\n')
        if len(findings) > 1:
            findings = ['Possible PHP shell: ' + shell for shell in findings if shell != '']
            found_data.append(findings)
    found_data = split_lists(found_data)
    # [ ANOTHER ISSUES ] - [END]
    return found_data