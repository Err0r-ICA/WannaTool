import os, sys, fileinput, time, socket, random, time, sys, platform, os

def tampil(x):
    w = {'m': 31, 'h': 32, 'k': 33, 'b': 34, 'p': 35, 'c': 36}
    for i in w:
        x = x.replace('\r%s' % i, '\x1b[%s;1m' % w[i])

    x += '\x1b[0m'
    x = x.replace('\r0', '\x1b[0m')
    print x


N = '\x1b[0m'
D = '\x1b[90m'
W = '\x1b[1;37m'
B = '\x1b[1;34m'
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
C = '\x1b[1;36m'
ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '\xe2\x88\x9a' + G + '] '
eror = R + '[' + W + '!' + R + ']'
print
print '\x1b[91m _____ _      ____  ____  _  ____  _____'
print '\x1b[91m*  __****  *|*   _**  __** **  __**__ __*'
print '\x1b[91m|  *  | |* |||  *  |  **|| ||  **|  * *'
print '\x1b[91m|  /_ | | \\|||  \\_ |    /| ||  __/  | |'
print '\x1b[91m\\____\\_/  \\|\\____/\\_/\\_\\_/\\_/     \\_/'
print '                                 \x1b[91m*\x1b[95mScript Bash'
print
print '\x1b[94m===================== \x1b[91m====================='
print
print '\x1b[91m[1]\x1b[97mEncrypt   #\x1b[92mAuthor    :\x1b[96;1mAsecC -  ERR0R'
print '\x1b[91m[0]\x1b[97mEXIT      #\x1b[92mTeam      :\x1b[96;1mITALIA CYBER ARMY'
print '\x1b[91m[2]\x1b[97mDecrypt   #\x1b[92mGithub    :\x1b[96;1mhttps://github.com/Err0r-ICA'
print '             #\x1b[92mInstagram :\x1b[96;1mhttps://www.instagram.com/termux_hacking'
print
print '\x1b[92m===================== \x1b[95m====================='
print

def keluar():
    tampil('\rm[!]BY~~~ERR0R')
    os.sys.exit()


def dekrip():
    try:
        sc = raw_input(ask + W + 'Enter Address Script ' + G + '> ' + W)
        f = open(sc, 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace('eval', 'echo')
        out = raw_input(ask + W + 'Enter Address Output' + G + ' > ' + W)
        f = open(out, 'w')
        f.write(newdata)
        f.close()
        os.system('touch decript.sh')
        os.system('bash ' + out + ' > decript.sh')
        os.remove(out)
        os.rename('tes.sh', out)
        print sukses + 'SUCCESFULL..'
    except KeyboardInterrupt:
        print eror + ' FAILED'
    except IOError:
        print eror + ' File Not Detected!'


def enkrip():
    try:
        script = raw_input(ask + W + 'Enter Address Script ' + G + '|> ' + W)
        output = raw_input(ask + W + 'Enter Address Output ' + G + '|> ' + W)
        os.system('bash-obfuscate ' + script + ' -o ' + output)
        print sukses + 'SUCCESFULL..'
    except KeyboardInterrupt:
        print eror + ' FAILED!'
    except IOError:
        print eror + ' File Not Detected!'


takok = raw_input(W + 'Encript' + G + ' |> ')
if takok == '1' or takok == '01':
    enkrip()
else:
    if takok == '2' or takok == '02':
        dekrip()
    else:
        if tatok == '0' or tatok == '00':
            keluar()
        else:
            print eror + ' Wrong input'
            keluar()
