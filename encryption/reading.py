from data import sql

def get_password_by_title(title):
    conn = sql.conn
    c = sql.c

    c.execute("SELECT ad, password FROM secret WHERE info = ?", (title,))
    result = c.fetchone()

    if result:
        username, password_red = result
        password = calculate_original_password(password_red)
        return f"\n\nKullanıcı Adı: {username}\nŞifre: {password}\n"
    else:
        return "Şifre başlığı bulunamadı."

def calculate_original_password(password_red):
    original_password = ""
    i = 0
    while i < len(password_red):
        if password_red[i:i + 3] == "xyz":
            original_password += 'A'
            i += 3
        elif password_red[i:i + 3] == "kfe":
            original_password += 'a'
            i += 3
        elif password_red[i:i + 3] == "ğpg":
            original_password += 'B'
            i += 3
        elif password_red[i:i + 3] == "abc":
            original_password += 'b'
            i += 3
        elif password_red[i:i + 3] == "def":
            original_password += 'C'
            i += 3
        elif password_red[i:i + 3] == "ghi":
            original_password += 'c'
            i += 3
        elif password_red[i:i + 3] == "jkl":
            original_password += 'D'
            i += 3
        elif password_red[i:i + 3] == "mno":
            original_password += 'd'
            i += 3
        elif password_red[i:i + 3] == "prs":
            original_password += 'E'
            i += 3
        elif password_red[i:i + 3] == "tuv":
            original_password += 'e'
            i += 3
        elif password_red[i:i + 3] == "wxy":
            original_password += 'F'
            i += 3
        elif password_red[i:i + 3] == "zab":
            original_password += 'f'
            i += 3
        elif password_red[i:i + 3] == "cde":
            original_password += 'G'
            i += 3
        elif password_red[i:i + 3] == "fgh":
            original_password += 'g'
            i += 3
        elif password_red[i:i + 3] == "ijk":
            original_password += 'H'
            i += 3
        elif password_red[i:i + 3] == "lmn":
            original_password += 'h'
            i += 3
        elif password_red[i:i + 3] == "opq":
            original_password += 'I'
            i += 3
        elif password_red[i:i + 3] == "rst":
            original_password += 'i'
            i += 3
        elif password_red[i:i + 3] == "uvw":
            original_password += 'J'
            i += 3
        elif password_red[i:i + 3] == "üği":
            original_password += 'j'
            i += 3
        elif password_red[i:i + 3] == "üüz":
            original_password += 'K'
            i += 3
        elif password_red[i:i + 3] == "ttr":
            original_password += 'k'
            i += 3
        elif password_red[i:i + 3] == "hhr":
            original_password += 'L'
            i += 3
        elif password_red[i:i + 3] == "çşp":
            original_password += 'l'
            i += 3
        elif password_red[i:i + 3] == "aqw":
            original_password += 'M'
            i += 3
        elif password_red[i:i + 3] == "sxü":
            original_password += 'm'
            i += 3
        elif password_red[i:i + 3] == "sex":
            original_password += 'N'
            i += 3
        elif password_red[i:i + 3] == "ana":
            original_password += 'n'
            i += 3
        elif password_red[i:i + 3] == "zab":
            original_password += 'O'
            i += 3
        elif password_red[i:i + 3] == "iği":
            original_password += 'o'
            i += 3
        elif password_red[i:i + 3] == "çol":
            original_password += 'P'
            i += 3
        elif password_red[i:i + 3] == "iwe":
            original_password += 'p'
            i += 3
        elif password_red[i:i + 3] == "dzz":
            original_password += 'Q'
            i += 3
        elif password_red[i:i + 3] == "aaq":
            original_password += 'q'
            i += 3
        elif password_red[i:i + 3] == "ass":
            original_password += 'R'
            i += 3
        elif password_red[i:i + 3] == "nic":
                    original_password += 'r'
                    i += 3
        elif password_red[i:i + 3] == "neg":
            original_password += 'S'
            i += 3
        elif password_red[i:i + 3] == "hjı":
            original_password += 's'
            i += 3
        elif password_red[i:i + 3] == "pğx":
            original_password += 'T'
            i += 3
        elif password_red[i:i + 3] == "xxd":
            original_password += 't'
            i += 3
        elif password_red[i:i + 3] == "ffe":
            original_password += 'U'
            i += 3
        elif password_red[i:i + 3] == "ççk":
            original_password += 'u'
            i += 3
        elif password_red[i:i + 3] == "ssk":
            original_password += 'V'
            i += 3
        elif password_red[i:i + 3] == "tgg":
            original_password += 'v'
            i += 3
        elif password_red[i:i + 3] == "aba":
            original_password += 'W'
            i += 3
        elif password_red[i:i + 3] == "uwu":
            original_password += 'w'
            i += 3
        elif password_red[i:i + 3] == "idk":
            original_password += 'X'
            i += 3
        elif password_red[i:i + 3] == "wow":
            original_password += 'x'
            i += 3
        elif password_red[i:i + 3] == "dde":
            original_password += 'Y'
            i += 3
        elif password_red[i:i + 3] == "bbü":
            original_password += 'y'
            i += 3
        elif password_red[i:i + 3] == "ğğw":
            original_password += 'Z'
            i += 3
        elif password_red[i:i + 3] == "ffş":
            original_password += 'z'
            i += 3
        elif password_red[i:i + 3] == "sss":
            original_password += 'Ü'
            i += 3
        elif password_red[i:i + 3] == "jhj":
            original_password += 'ü'
            i += 3
        elif password_red[i:i + 3] == "php":
            original_password += 'Ç'
            i += 3
        elif password_red[i:i + 3] == "qqw":
            original_password += 'ç'
            i += 3
        elif password_red[i:i + 3] == "pep":
            original_password += 'Ö'
            i += 3
        elif password_red[i:i + 3] == "crt":
            original_password += 'ö'
            i += 3
        elif password_red[i:i + 3] == "msn":
            original_password += 'Ğ'
            i += 3
        elif password_red[i:i + 3] == "üit":
            original_password += 'ğ'
            i += 3
        elif password_red[i:i + 3] == "qqf":
            original_password += 'Ş'
            i += 3
        elif password_red[i:i + 3] == "bbc":
            original_password += 'ş'
            i += 3
        elif password_red[i:i + 3] == "aaa":
            original_password += '1'
            i += 3
        elif password_red[i:i + 3] == "bbb":
            original_password += '2'
            i += 3
        elif password_red[i:i + 3] == "ccc":
            original_password += '3'
            i += 3
        elif password_red[i:i + 3] == "ddd":
            original_password += '4'
            i += 3
        elif password_red[i:i + 3] == "eee":
            original_password += '5'
            i += 3
        elif password_red[i:i + 3] == "fff":
            original_password += '6'
            i += 3
        elif password_red[i:i + 3] == "ggg":
            original_password += '7'
            i += 3
        elif password_red[i:i + 3] == "hhh":
            original_password += '8'
            i += 3
        elif password_red[i:i + 3] == "ppp":
            original_password += '9'
            i += 3
        elif password_red[i:i + 3] == "mmm":
            original_password += '0'
            i += 3
        elif password_red[i:i + 3] == "qqq":
            original_password += '*'
            i += 3
        elif password_red[i:i + 3] == "www":
            original_password += '-'
            i += 3
        elif password_red[i:i + 3] == "ttt":
            original_password += '+'
            i += 3
        elif password_red[i:i + 3] == "ööö":
            original_password += '_'
            i += 3
        else:
            original_password += password_red[i]
            i += 1
    return original_password


