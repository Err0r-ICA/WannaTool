import urllib2
from urllib2 import URLError
print ""
print ""
print '""8"" 8""^" 8"^"8  8""8""8 8   8 8    8                   '
print "  8   8     8   8  8  8  8 8   8 8    8                   "
print "  8e  8eeee 8eee8e 8e 8  8 8e  8 eeeeee                   "
print "  88  88    88   8 88 8  8 88  8 88   8                   "
print "  88  88    88   8 88 8  8 88  8 88   8                   "
print "  88  88eee 88   8 88 8  8 88ee8 88   8                   "
print ''
print '8^"^"8 8"^"88 8"^"88 8^"^"8 8     8^"^"                   '
print '8    " 8    8 8    8 8    " 8     8                       '
print "8e     8    8 8    8 8e     8e    8eeee                   "
print "88  ee 8    8 8    8 88  ee 88    88                      "
print "88   8 8    8 8    8 88   8 88    88                      "
print "88eee8 8eeee8 8eeee8 88eee8 88eee 88eee                   "
print ''
print '""8"" 8"^"8  8^"^"8 8"^"8 8^"^"8 8     8^"^"8 ""8"" 8^"^" '
print "  8   8   8  8    8 8   8 8      8     8    8   8   8     "
print "  8e  8eee8e 8eeee8 8e  8 8eeeee 8e    8eeee8   8e  8eeee "
print "  88  88   8 88   8 88  8     88 88    88   8   88  88    "
print "  88  88   8 88   8 88  8 e   88 88    88   8   88  88    "
print "  88  88   8 88   8 88  8 8eee88 88eee 88   8   88  88eee "
print ""
print ''
print ''
f = open('id_country.txt','r')
lines = f.readlines()
panjang = len(lines)


for i in range(panjang/3):
    print lines[i].replace('\n', ''),'\t', lines[i + panjang/2].replace('\n', ''),'\t', lines[i + panjang/3].replace('\n', '')
if panjang%2: #if it is odd
    print lines[-1].replace('\n', '')

while True:
    try:
        print ''
        bahasa_awal = raw_input("Enter Initial Language (Ex: it): ") #auto is automatic detected language
        bahasa_tujuan = raw_input("Enter the Destination Language (Ex: en): ")
        kata = raw_input("Enter Words / Sentences: ")
        url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+")) #replace apabila terjadi kalimat
        agent = {'User-Agent':'Mozilla/5.0'}
        cari_hasil = 'class="t0">'
        request = urllib2.Request(url, headers=agent)
        page = urllib2.urlopen(request).read()
        result = page[page.find(cari_hasil)+len(cari_hasil):]
        result = result.split("<")[0]
        print "%s -> Translated into: " % kata, result

    except URLError, e:
        print "Your Connection is NOT 200OK.. Check Again!"
