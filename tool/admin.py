#/usr/bin/python

# This was written for educational purpose only. Use it at your own risk.
# Author will be not responsible for any damage!
# !!! Special greetz for my friend  !!!
# !!! Special thanx for my team  !!! 
#
################################################################ 
# --- ERR0R ./Chu404  ~ Reentz ~ Zx'Phoenix ~ RC_Hunter.   --- #
# --- Pandora ~ Mr.Dongkrak ~./F4LL ~ Mr.Yazz.             --- #
# ---- Mr.Agency ~ Floxytru3 ~ Zona Nolep ~ Mr. Faino      --- #
# --- Gatra ~ IM ./PanjulL21 ~ Mr.s3lf ~ Mr.White.         --- #
# --- w4rnetx ~ Blue Dragon.                               --- # 
# ---   https://www.ITALIA-CYBER-ARMY.blogspot.com.        --- # 
################################################################ 
#
#
# Based on Web admin locator by ERR0R
#
#
#



import sys, os, time, httplib

if sys.platform == 'linux' or sys.platform == 'linux2':
	clearing = 'clear'
else:
	clearing = 'cls'
os.system(clearing)


if len(sys.argv) != 2:
	print "\n|---------------------------------------------------|"
        print "|      termuxx[@]gmail[dot]com                      |"
        print "|   04/2k20     Admin login finder v2.0             |"
	print "| Help: python2 admin.py -h                         |"
	print "| Visit https://www.instagram.com/termux_hacking    |"
        print "|---------------------------------------------------|\n"
	sys.exit(1)
	
for arg in sys.argv:
	if arg == '-h':
		print "\n|--------------------------------------------------|"
                print "|      termuxx[@]gmail[dot]com                     |"
                print "|   04/2k20      Admin login finder  v2.0          |"
                print "| Usage: python2 admin.py www.site.com             |"
	        print "| Example: python2 admin.py site.com               |"
	        print "| Visit https://www.instagram.com/termux_hacking   |"
                print "|--------------------------------------------------|\n"
		sys.exit(1)
	
	

site = sys.argv[1].replace("http://","").rsplit("/",1)[0] 
site = site.lower()

admin_path = ['admin.php','admin/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php','joomla/administrator','login.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html','admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html','admin/controlpanel.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html','webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html','admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php','administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php','bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','modelsearch/login.php','moderator.php','moderator/login.php','moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html','webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html','administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html','panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','adminarea/index.php','adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php','modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']


print "\n|---------------------------------------------------|"
print "|      termuxx[@]gmail[dot]com                      |"
print "|   Author : *ERR0R*                                |"
print "|   04/2k20      Admin login finder     v2.0        |"
print "| Visit https://www.instagram.com/termux_hacking    |"
print "|---------------------------------------------------|\n"
print "\n[-] %s" % time.strftime("%X")
		
print "[+] Target:",site
print "[+] Checking Paths..."
print


try:
	for admin in admin_path:
		admin = admin.replace("\n","")
		admin = "/" + admin
		connection = httplib.HTTPConnection(site)
		connection.request("GET",admin)
		response = connection.getresponse()
		print "%s %s %s" % (admin, response.status, response.reason)
except(KeyboardInterrupt,SystemExit):
		raise
except:
		pass	
