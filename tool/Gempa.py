#!/usr/bin/python
# Data Gempa Terkini
# Coded by Rafsanzani Suhada
# ZeroByte.ID
import requests
import xml.dom.minidom as xmlget
import os
class bcolors:
    HIJAU='\033[1;92m'
    MERAH='\033[01;91m'
    NORMAL='\033[0m'
    CYAN='\033[1;96m'
    BIRU='\033[1;94m'
    PUTIH='\033[1;97m'

def main():
    response = requests.get('http://data.bmkg.go.id/autogempa.xml')
    result = (response.text)
    save = open('result.xml','w')
    save.write('%s' %result,)
    save.close()
    rxml = xmlget.parse("result.xml")

    
    Tanggal = rxml.getElementsByTagName("Tanggal")[0].firstChild.data
    Jam = rxml.getElementsByTagName("Jam")[0].firstChild.data
    Lintang = rxml.getElementsByTagName("Lintang")[0].firstChild.data
    Bujur = rxml.getElementsByTagName("Bujur")[0].firstChild.data
    Magnitude = rxml.getElementsByTagName("Magnitude")[0].firstChild.data
    Kedalaman = rxml.getElementsByTagName("Kedalaman")[0].firstChild.data
    Wilayah = rxml.getElementsByTagName("Wilayah1")[0].firstChild.data
    Potensi = rxml.getElementsByTagName("Potensi")[0].firstChild.data

    print " DATE       : {}".format(Tanggal)
    print " HOUR       : {}".format(Jam)
    print bcolors.CYAN
    print " LATUTUDE   : {}".format(Lintang)
    print " LONGITUDE  : {}".format(Bujur)
    print " MAGNITUDE  : {}".format(Magnitude)
    print " DEPTH      : {}".format(Kedalaman)
    print bcolors.HIJAU
    print " REGION     : {}".format(Wilayah)
    print " POTENCY    : {}".format(Potensi)


# Clear layar
os.system('cls' if os.name == 'nt' else 'clear')

print bcolors.MERAH
print ""
print '8   8  8 8   8 8^"^" 8"^"8  8^"^"    '
print "8   8  8 8   8 8     8   8  8        "
print "8e  8  8 8eee8 8eeee 8eee8e 8eeee    "
print "88  8  8 88  8 88    88   8 88       "
print "88  8  8 88  8 88    88   8 88       "
print "88ee8ee8 88  8 88eee 88   8 88eee    "
print ''
print "                  0"
print ""
print '8^"^"8 8""8""8    8    8^"^"8          '
print "8    8 8  8  8    8         8          "
print "8eeee8 8e 8  8    8e   eeeee8          "
print "88   8 88 8  8    88   88              "
print '88   8 88 8  8    88   ""              '
print "88   8 88 8  8    88   00              "
print ''
print bcolors.NORMAL
print 
if __name__ == "__main__":
    main()
    # Remove file result.xml
    if os.path.exists("result.xml"):
        os.remove("result.xml")
    else:
        print("The File Does NOT Exists")
    print bcolors.NORMAL
