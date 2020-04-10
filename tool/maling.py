import base64, zlib, marshal, sys
W = '\x1b[1;97m'
RR = '\x1b[1;97m\x1b[91m'
O = '\x1b[93m'
B = '\x1b[94m'
print ("{}{}\n______                                   _                \n| ___ \\                                 | |               \n| |_/ / _   _   ___  _ __  _   _  _ __  | |_   ___   _ __ \n|  __/ | | | | / __|| '__|| | | || '_ \\ | __| / _ \\ | '__|\n| |    | |_| || (__ | |   | |_| || |_) || |_ | (_) || |   \n\\_|     \\__, | \\___||_|    \\__, || .__/  \\__| \\___/ |_|   \n         __/ |              __/ || |                      \n        |___/              |___/ |_|  - {}Coded By ERR0R\n        \n{}[++ {}Menu:\n\t\n  {}[{}01{}]{} Encrypt File With base64\n  {}[{}02{}]{} Encrypt File With base16\n  {}[{}03{}]{} Encrypt File With base32\n  {}[{}04{}]{} Encrypt File With marshal\n  {}[{}05{}]{} Encrypt File With zlib&base64\n  {}[{}06{}]{} Encrypt File With zlib&base64&marshal\n  {}[{}07{}]{} Encrypt File With zlib&base16&marshal\n  {}[{}08{}]{} Encrypt File With zlib&base32&marshal\n  {}[{}09{}]{} EXIT\n  {}[{}10{}]{} info\n").format(W, O, W, RR, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W)

def main():
    choice = raw_input(RR + '[++ ' + W + 'Choose: ')
    if choice == '1' or choice == '01':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            a = base64.b64encode(fileopen)
            b = "import base64\nexec(base64.b64decode('" + a + "'))"
            c = file.replace('.py', '_endcrypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print RR + '[*] ' + W + 'OUTPUT:', c
            main()
        except:
            print RR + '[-] ' + W + 'File NOT Found!'
            main()

    if choice == '2' or choice == '02':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            a = base64.b16encode(fileopen)
            b = "import base64\nexec(base64.b16decode('" + a + "'))"
            c = file.replace('.py', '_endcrypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print RR + '[*] ' + W + 'OUTPUT:', c
            main()
        except:
            print RR + '[-] ' + W + 'File NOT Found!'
            main()

    if choice == '3' or choice == '03':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            a = base64.b32encode(fileopen)
            b = "import base64\nexec(base64.b32decode('" + a + "'))"
            c = file.replace('.py', '_endcrypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print RR + '[*] ' + W + 'OUTPUT:', c
            main()
        except:
            print RR + '[-] ' + W + 'File NOT Found!'
            main()

    if choice == '4' or choice == '04':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            a = compile(fileopen, 'dg', 'exec')
            m = marshal.dumps(a)
            s = repr(m)
            b = 'import marshal\nexec(marshal.loads(' + s + '))'
            c = file.replace('.py', '_endcrypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print RR + '[*] ' + W + 'OUTPUT:', c
            main()
        except:
            print RR + '[-] ' + W + 'File NOT Found!'
            main()

    if choice == '5' or choice == '05':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            c = zlib.compress(fileopen)
            d = base64.b64encode(c)
            e = 'import marshal,zlib,base64\nexec(zlib.decompress(base64.b64decode("' + d + '")))'
            f = file.replace('.py', '_endcrypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print RR + '[*] ' + W + 'OUTPUT:', f
            main()
        except:
            print RR + '[-] ' + W + 'File NOT Found!'
            main()

    if choice == '6' or choice == '06':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b64encode(c)
            e = 'import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("' + str(d) + '"))))'
            f = file.replace('.py', '_endcrypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print RR + '[*] ' + W + 'OUTPUT:', f
            main()
        except:
            print RR + '[-] ' + W + 'File NOT Found!'
            main()

    if choice == '7' or choice == '07':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b16encode(c)
            e = 'import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode("' + str(d) + '"))))'
            f = file.replace('.py', '_endcrypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print RR + '[*] ' + W + 'OUTPUT:', f
            main()
        except:
            print RR + '[-] ' + W + 'File NOT Found!'
            main()

    if choice == '8' or choice == '08':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b32encode(c)
            e = 'import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode("' + str(d) + '"))))'
            f = file.replace('.py', '_endcrypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print RR + '[*] ' + W + 'OUTPUT:', f
            main()
        except:
            print RR + '[-] ' + W + 'File NOT Found!'
            main()

    if choice == '9' or choice == '09':
        sys.exit(RR + '[*] ' + W + 'SEE YA NEXT TIME!1!1')
    else:
        if choice == '10':
            print '\n\tAUTHOR\n\t===================================\n\tCREATED BY : ITALIA CYBER ARMY\n\tCODED BY   : ERR0R\n\tTELEGRAM   : https://t.me/termuxxhacking\n\tGITHUB     : https://github.com/Err0r-ICA\n\t\t     \n\tREPORT BUG ON FACEBOOK OR INSTAGRAM\n\t===================================\n\tfb : ERR0R\n\tig : R00t_\n\t===================================\n\t'
            main()
        else:
            print RR + '[-] ' + W + 'WRONG INPUT!!'
            sys.exit(RR + '[*] ' + W + 'SEE YA NEXT TIME!1!1')


if __name__ == '__main__':
    main()
